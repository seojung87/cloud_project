from django.shortcuts import render
from .models import Cash

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