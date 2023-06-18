from django.shortcuts import render
from .models import Cash, Category

# Create your views here.
def main(request):
    acash = Cash.objects.all()

    return render(
        request,
        'cashbook/main.html',
        {
            'acash' : acash,
        }
    )

def input_form(request):
    actgr = Category.objects.all()

    return render(
        request,
        'cashbook/inputForm.html',
        {
            'actgr' : actgr
        }
    )