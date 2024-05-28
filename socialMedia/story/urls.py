from django.contrib import admin
from django.urls import path
from .views import StoryCreateView,StorydeleteView,StoryListView

urlpatterns = [
    path('story/create/',StoryCreateView.as_view(),name="Story Create"),
    path('stories/',StoryListView.as_view(),name="Stories list"),
    path('story/<int:pk>/',StorydeleteView.as_view(),name="Story delete"),
]