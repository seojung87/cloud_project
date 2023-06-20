from django.shortcuts import render, redirect
from django.contrib.auth import logout

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

def logout_view(request):
    logout(request)
    return redirect('/')  # 로그아웃 후 리디렉션할 URL 지정