from django.urls import path

from . import views

urlpatterns = [
    path('', views.store, name="store"),
    path('cart/', views.cart, name="cart"),
    path('checkout/<str:pk>/', views.store, name="store"),

]
