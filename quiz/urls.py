# quiz/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.quiz_page, name='quiz-page'),
]
