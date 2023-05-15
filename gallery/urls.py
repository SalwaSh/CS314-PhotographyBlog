from django.urls import path
from . import views


urlpatterns = [
    path('celebration', views.celebration, name='celebration' ),
    path('landmark', views.product, name='landmark' ),
    path('food', views.food, name='food' ),
]