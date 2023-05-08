from django.urls import path
from . import views


urlpatterns = [
    path('baby', views.baby, name='baby' ),
    path('product', views.product, name='product' ),
    path('country', views.country, name='country' ),
]