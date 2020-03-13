from django.urls import path
from . import views

urlpatterns = [
    path('login/',views.login,name='login' ),
    path('registration/',views.registration,name='registration' ),
    path('logout/',views.login,name='logout' ),
    path('index/',views.index,name='index')
]