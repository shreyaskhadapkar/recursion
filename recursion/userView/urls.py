from django.urls import path
from . import views

urlpatterns = [
    path('Home/',views.homepage,name='homepage'),
    
   

]