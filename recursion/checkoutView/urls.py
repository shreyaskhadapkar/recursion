from django.urls import path
from . import views

urlpatterns = [
    path('orderList/', views.orderList , name='orderList'),
    path('orderList/<slug:slug>/', views.orderDetails , name='orderDetails'),
]