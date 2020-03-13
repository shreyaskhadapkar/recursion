from django.urls import path
from . import views

urlpatterns = [
    path('product/',views.product,name='product'),
    path('productUpdate/<slug:slug>/',views.productUpdate,name='productUpdate'),
    path('productAdd/',views.productAdd,name='productAdd')
]