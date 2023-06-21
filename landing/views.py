from django.shortcuts import render, redirect
from django.contrib.auth import logout
from django.contrib.auth.views import LoginView

# Create your views here.
def landing(request):
    return render(
        request,
        'landing/landing_page.html'
    )

def about_me(request):
    return render(
        request,
        'landing/about_me.html'
    )

def login_view(request):
    return render(
        request,
        'landing/login_page.html'
    )

class CustomLoginView(LoginView):
    template_name = 'landing/login_page.html'
    def get_success_url(self):
        return '/cashbook/'

def logout_view(request):
    logout(request)
    return redirect('/')  # 로그아웃 후 리디렉션할 URL 지정