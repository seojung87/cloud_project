from django.urls import path
from . import views


urlpatterns = [
    path('about_me/', views.about_me),
    path('logout/', views.logout_view),
    #path('login/', views.login_view),
    path('login/', views.CustomLoginView.as_view()),
    path('', views.landing),
]