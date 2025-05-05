from django.shortcuts import render
from rest_framework import generics 
from django.shortcuts import get_object_or_404
from rest_framework import generics
from rest_framework.exceptions import ValidationError
from rest_framework.permissions import IsAuthenticated
from .models import Review, ReviewQuestion, ReviewAnswer
from .serializers import ReviewSerializer,ReviewQuestionSerliazer,ListReviewSerializer
from establishements.models import Establishement 
from django.db import transaction
from .permissions import IsClient


class HotelQuestionsView(generics.ListAPIView):
    serializer_class = ReviewQuestionSerliazer
    queryset = ReviewQuestion.objects.filter(type='hotel')

class RestaurantQuestionsView(generics.ListAPIView):
    serializer_class = ReviewQuestionSerliazer
    queryset = ReviewQuestion.objects.filter(type='restaurant')

class AddReviewView(generics.CreateAPIView):
    serializer_class = ReviewSerializer
    permission_classes = [IsAuthenticated,IsClient]
    queryset = Review.objects.none()

    def get_serializer_context(self):
        context = super().get_serializer_context()
        establishment_id = self.kwargs.get('establishement_id')
        context['establishement'] = get_object_or_404(Establishement, id=establishment_id)
        return context


class EstablishmentReviewsView(generics.ListAPIView):
    serializer_class = ListReviewSerializer
    permission_classes = [IsAuthenticated]
    queryset = Review.objects.all()

    def get_queryset(self):
        establishment_id = self.kwargs.get('establishement_id')
        return Review.objects.filter(establishement_id=establishment_id)


class ReviewListView(generics.ListAPIView):
    serializer_class = ListReviewSerializer
    permission_classes = [IsAuthenticated]
    queryset = Review.objects.all()



class ProfileReviewList(generics.ListAPIView):
    serializer_class = ListReviewSerializer
    permission_classes = [IsAuthenticated,IsClient]

    def get_queryset(self):
        return Review.objects.filter(profile=self.request.user.profile)
    