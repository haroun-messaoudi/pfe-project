from rest_framework import serializers
from .models import Review, ReviewQuestion, ReviewAnswer
from django.db import transaction


class ReviewQuestionSerliazer(serializers.ModelSerializer):
    class Meta:
        model = ReviewQuestion
        fields = ["id", "question", "type"]

class ReviewAnswerSerializer(serializers.ModelSerializer):
    question = serializers.PrimaryKeyRelatedField(queryset=ReviewQuestion.objects.all())

    class Meta:
        model = ReviewAnswer
        fields = ["question", "rating"]
        extra_kwargs = {
            "rating": {"required": True}
        }



class ListReviewSerializer(serializers.ModelSerializer):
    answers = ReviewAnswerSerializer(many=True, read_only=True)
    date_posted = serializers.SerializerMethodField()
    profile = serializers.SerializerMethodField()
    establishement = serializers.SerializerMethodField()
    class Meta:
        model = Review
        fields = ['id', 'title', 'content', 'answers', 'date_posted', 'profile', 'establishement', 'rating']
        read_only_fields = ['date_posted', 'profile', 'establishement', 'rating']
        
    def get_profile(self, obj):
        first_name = obj.profile.first_name or ""
        last_name = obj.profile.last_name or ""
        return f"{first_name} {last_name}".strip()

    def get_establishement(self,obj):
        return obj.establishement.name

    def get_date_posted(self, obj):
        return obj.date_posted.strftime('%Y-%m-%d')

class ReviewSerializer(serializers.ModelSerializer):
    answers = ReviewAnswerSerializer(many=True)

    class Meta:
        model = Review
        fields = ['id', 'title', 'content', 'answers', 'date_posted', 'profile', 'establishement', 'rating']
        read_only_fields = ['date_posted', 'profile', 'establishement', 'rating']

    def validate(self, data):
        establishment = self.context.get('establishement')
        request = self.context.get('request')
        
        if not establishment or not request:
            raise serializers.ValidationError("Missing context data")

        # Check for existing review
        if Review.objects.filter(
            profile=request.user.profile,
            establishement=establishment
        ).exists():
            raise serializers.ValidationError(
                {"detail": "You have already reviewed this establishment."}
            )

        # Question validation (keep your existing code)
        required_questions = ReviewQuestion.objects.filter(type=establishment.type)
        required_question_ids = set(required_questions.values_list('id', flat=True))
        
        answered_question_ids = set()
        answers_data = data.get('answers', [])
        
        for answer in answers_data:
            question = answer['question']
            if question.type != establishment.type:
                raise serializers.ValidationError(
                    {"answers": f"Question {question.id} does not match establishment type."}
                )
            answered_question_ids.add(question.id)
        
        missing = required_question_ids - answered_question_ids
        extra = answered_question_ids - required_question_ids
        
        if missing:
            raise serializers.ValidationError(
                {"answers": f"Missing answers for questions: {list(missing)}"}
            )
        if extra:
            raise serializers.ValidationError(
                {"answers": f"Extra answers provided for questions: {list(extra)}"}
            )
        
        return data

    def create(self, validated_data):
        answers_data = validated_data.pop('answers')
        request = self.context.get('request')
        establishment = self.context.get('establishement')
        
        if not request or not establishment:
            raise serializers.ValidationError("Missing context data")

        try:
            with transaction.atomic():
                review = Review.objects.create(
                    profile=request.user.profile,
                    establishement=establishment,
                    **validated_data
                )
                
                for answer_data in answers_data:
                    ReviewAnswer.objects.create(
                        review=review,
                        question=answer_data['question'],
                        rating=answer_data['rating']
                    )
                
                review.calculate_rating()
            return review
                
        except Exception as e:
            raise serializers.ValidationError(str(e))
        
""""
VERY IMPORTANT NOTEE : make sure to wait after submiting the creation request 
even in the browsable api since the creation is made with a transition 
that makes sure every necessary instance of each model is created
before returning the response and the checking takes time 
"""

"""
Example of a review Make sure its sent in raw data (browsableapi) or body (postman)
{
    "title": "makan makan",
    "content": "mayeeeeet",
    "answers": [
        {"question": 1, "rating": 4},
        {"question": 2, "rating": 5},
        {"question": 3, "rating": 4}
    ]
}
"""