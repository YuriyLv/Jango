from django.urls import path
from . import views

urlpatterns = [
    path('', views.PostView.as_view()),
    path('<str:cat>/', views.PostCatView.as_view(), name='PostCatView'),
]