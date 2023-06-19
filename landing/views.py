from django.shortcuts import render

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