from django.shortcuts import render
from cashbook.models import Cash

# Create your views here.
def mainchart(request):
    acash = Cash.objects.all()

    return render(
        request,
        'expense_chart/main_chart.html',
        {
            'acash' : acash,
        }
    )