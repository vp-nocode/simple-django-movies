from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('add/', views.add_movie, name='add_movie'),
    path('add_review/<int:movie_id>/', views.add_review, name='add_review')
]
