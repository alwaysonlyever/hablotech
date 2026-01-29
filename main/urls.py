from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('guides/', views.guides_index, name='guides_index'),
    path('guides/drones/', views.drone_guide, name='drone_guide'),
]
