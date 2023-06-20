import json, calendar
from datetime import datetime

from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from cashbook.models import Cash

# Create your views here.

def export_income_data(year):
    income = Cash.objects.filter(stat=True)
    income = income.filter(date__year=year)
    monthly = [0] * 12
    for i in income :
        #print(i.date.month)
        monthly[i.date.month -1] += i.amount/10000
    #print(monthly)
    return monthly
def export_expense_data(year):
    expense = Cash.objects.filter(stat=False)
    expense = expense.filter(date__year=year)
    monthly = [0] * 12
    for i in expense:
        monthly[i.date.month - 1] += i.amount / 10000
    return monthly

def category_div_1(year, month):
    data = Cash.objects.filter(category="6")
    data = data.filter(date__year=year)
    data = data.filter(date__month=month)
    data_sum = 0
    for i in data:
        data_sum += i.amount
    return data_sum
def category_div_2(year, month):
    data = Cash.objects.filter(category="7")
    data = data.filter(date__year=year)
    data = data.filter(date__month=month)
    data_sum = 0
    for i in data:
        data_sum += i.amount
    return data_sum
def category_div_3(year, month):
    data = Cash.objects.filter(category="8")
    data = data.filter(date__year=year)
    data = data.filter(date__month=month)
    data_sum = 0
    for i in data:
        data_sum += i.amount
    return data_sum
def category_div_4(year, month):
    data = Cash.objects.filter(category="9")
    data = data.filter(date__year=year)
    data = data.filter(date__month=month)
    data_sum = 0
    for i in data:
        data_sum += i.amount
    return data_sum
def category_div_5(year, month):
    data = Cash.objects.filter(category="10")
    data = data.filter(date__year=year)
    data = data.filter(date__month=month)
    data_sum = 0
    for i in data:
        data_sum += i.amount
    return data_sum
def category_div_6(year, month):
    data = Cash.objects.filter(category="11")
    data = data.filter(date__year=year)
    data = data.filter(date__month=month)
    data_sum = 0
    for i in data:
        data_sum += i.amount
    return data_sum
def category_div_7(year, month):
    data = Cash.objects.filter(category="12")
    data = data.filter(date__year=year)
    data = data.filter(date__month=month)
    data_sum = 0
    for i in data:
        data_sum += i.amount
    return data_sum
def category_div_8(year, month):
    data = Cash.objects.filter(category="13")
    data = data.filter(date__year=year)
    data = data.filter(date__month=month)
    data_sum = 0
    for i in data:
        data_sum += i.amount
    return data_sum
def category_div_9(year, month):
    data = Cash.objects.filter(category="14")
    data = data.filter(date__year=year)
    data = data.filter(date__month=month)
    data_sum = 0
    for i in data:
        data_sum += i.amount
    return data_sum

def category_sum(c1,c2,c3,c4,c5,c6,c7,c8,c9):
    total_sum = c1 + c2 + c3 + c4 + c5 + c6 + c7 + c8 + c9
    return total_sum

@login_required
def mainchart(request):
    year = datetime.now().year
    month = datetime.now().month
    month_name = calendar.month_name[month]

    acash = Cash.objects.all()
    amount_data_in = export_income_data(year)
    json.dumps(amount_data_in)
    amount_data_out = export_expense_data(year)
    json.dumps(amount_data_out)

    ct1 = category_div_1(year, month)
    json.dumps(ct1)
    ct2 = category_div_2(year, month)
    json.dumps(ct2)
    ct3 = category_div_3(year, month)
    json.dumps(ct3)
    ct4 = category_div_4(year, month)
    json.dumps(ct4)
    ct5 = category_div_5(year, month)
    json.dumps(ct5)
    ct6 = category_div_6(year, month)
    json.dumps(ct6)
    ct7 = category_div_7(year, month)
    json.dumps(ct7)
    ct8 = category_div_8(year, month)
    json.dumps(ct8)
    ct9 = category_div_9(year, month)
    json.dumps(ct9)
    total_sum = ct1 + ct2 + ct3 + ct4 + ct5 + ct6 + ct7 + ct8 + ct9
    json.dumps(total_sum)

    return render(
        request,
        'expense_chart/main_chart.html',
        {
            'acash' : acash,
            'amount_data_in' : amount_data_in,
            'amount_data_out' : amount_data_out,
            'year' : year,
            'month_name' : month_name,
            'ct1': ct1,
            'ct2': ct2,
            'ct3': ct3,
            'ct4': ct4,
            'ct5': ct5,
            'ct6': ct6,
            'ct7': ct7,
            'ct8': ct8,
            'ct9': ct9,
            'total_sum': total_sum,

        }
    )