from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView
from .models import Cash, Category
from datetime import datetime

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

    if request.method == 'POST':
        amount = request.POST.get('amount')
        status = request.POST.get('btnradio')
        category_name = request.POST.get('category')
        memo = request.POST.get('memo')
        date_str = request.POST.get('date')

        category = Category.objects.get(name=category_name)

        cash = Cash.objects.create(
            amount=amount,
            category=category,
            memo=memo,
            date=date_str,
        )
        cash.status = status
        cash.save()

        return redirect('cashbook/')

    return render(
        request,
        'cashbook/inputForm.html',
        {
            'actgr' : actgr
        }
    )
