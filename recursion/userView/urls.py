from django.urls import path
from . import views

urlpatterns = [
    path('Home/',views.homepage,name='homepage'),
    path('scanner/',views.scanner,name='scanner'),
    path('cart/',views.cart,name='cart')
]