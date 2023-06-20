import json
from datetime import datetime

from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from cashbook.models import Cash

# Create your views here.

def export_income_data():
    income = Cash.objects.filter(stat=True)
    monthly = [0] * 12
    for i in income :
        #print(i.date.month)
        monthly[i.date.month -1] += i.amount/10000
    #print(monthly)
    return monthly
def export_expense_data():
    expense = Cash.objects.filter(stat=False)
    monthly = [0] * 12
    for i in expense:
        monthly[i.date.month - 1] += i.amount / 10000
    return monthly

@login_required
def mainchart(request):
    acash = Cash.objects.all()
    amount_data_in = export_income_data()
    json.dumps(amount_data_in)
    amount_data_out = export_expense_data()
    json.dumps(amount_data_out)

    year = datetime.now().year

    return render(
        request,
        'expense_chart/main_chart.html',
        {
            'acash' : acash,
            'amount_data_in' : amount_data_in,
            'amount_data_out' : amount_data_out,
            'year' : year,
        }
    )