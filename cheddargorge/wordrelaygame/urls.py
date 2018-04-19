from django.urls import path

from . import views

app_name = 'wordrelaygame'

urlpatterns = [
    path('', views.HomeView.as_view(), name='home'),
    # path('archive/', views.ArchiveView.as_view(), name='archive'),
    # path('story/new/', views.create_story, name='new_story'),
    # path('story/<int:story_id>/', views.StoryView.as_view(), name=''),
    # path('addword/', views.addword, name='addword'),
]
