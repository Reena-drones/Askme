from django.urls import path, include
from rest_framework.urlpatterns import format_suffix_patterns
from .views import *

urlpatterns = [
    path('', AddQuestionView.as_view()),
    path('/answer', AddAnswerView.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)