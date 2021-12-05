from django.shortcuts import render
from rest_framework import generics
from .serializers import *
from rest_framework import permissions
from .models import Question, Answer
# Create your views here.
# isAdminUser

class AddQuestionView(generics.CreateAPIView):
    serializer_class = QuestionSerializer
    queryset = Question.objects.all()
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class AddAnswerView(generics.ListCreateAPIView):
    serializer_class = AnswerSerializer
    queryset = Answer.objects.all()
    permission_classes = [permissions.IsAdminUser]

    def perform_create(self, serializer):
        serializer.save()