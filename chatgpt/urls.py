from django.contrib import admin
from django.urls import path
from chatgpt import views   

urlpatterns = [
    path('', views.index, name='chatgpt'),
]