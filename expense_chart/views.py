from django.shortcuts import render
from django.contrib.auth.decorators import login_required
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