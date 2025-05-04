from django.db import models
from django.db.models import Avg
from django.core.validators import MinValueValidator,MaxValueValidator
# Create your models here.


class Review(models.Model):
    title = models.CharField(max_length=100, null=True, blank=True)
    content = models.TextField()
    date_posted = models.DateTimeField(auto_now_add=True)
    profile = models.ForeignKey("accounts.Profile", on_delete=models.CASCADE)
    rating = models.IntegerField(null=True, blank=True,validators=[MinValueValidator(1),MaxValueValidator(5)]) 
    establishement = models.ForeignKey(
        "establishements.Establishement",
        on_delete=models.CASCADE,
        related_name="reviews"
    )
    class Meta:
        unique_together = ("profile", "establishement")
        
    def calculate_rating(self):
        avg_rating = self.answers.aggregate(avg=Avg('rating'))['avg']
        self.rating = round(avg_rating) if avg_rating is not None else None
        self.save()
    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        self.establishement.get_average_rating()

    def __str__(self):
        return self.profile.user.username + " - " + self.establishement.name + " - " + str(self.rating) + " - " + str(self.date_posted)


class ReviewQuestion(models.Model):
    QUESTION_TYPE = [
        ("hotel", "Hotel"),
        ("restaurant", "Restaurant"),
    ]
    type = models.CharField(max_length=50, choices=QUESTION_TYPE)
    question = models.CharField(max_length=100)

    def __str__(self):
        return self.question

class ReviewAnswer(models.Model):
    review = models.ForeignKey(Review, on_delete=models.CASCADE, related_name="answers")
    question = models.ForeignKey(ReviewQuestion, on_delete=models.CASCADE)
    rating = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)])   
    class Meta:
        unique_together = ("review", "question")

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        self.review.calculate_rating() 

    def __str__(self):
        return f"Standards for {self.review.title}"