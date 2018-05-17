from django.urls import path

from . import views

app_name = 'wordrelaygame'

urlpatterns = [
    path('', views.HomeView.as_view(), name='home'),
    path('addword/', views.AddWordView.as_view(), name='addword'),
    # path('archive/', views.ArchiveView.as_view(), name='archive'),
    path('story/new/', views.AddStoryView.as_view(), name='new_story'),
    # path('story/<int:story_id>/', views.StoryView.as_view(), name=''),
]
