from django.urls import path
from . import views

urlpatterns = [
    path('inputForm/', views.input_form),
    path('deleteEvent/<int:pk>/', views.delete_event),
    path('', views.main),
]