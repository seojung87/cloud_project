from django.urls import path
from . import views

urlpatterns = [
    path('inputForm/', views.input_form, name='input_form'),
    path('', views.main),
]