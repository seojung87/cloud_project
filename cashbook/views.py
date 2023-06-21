import json

from django.http import JsonResponse

from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.views.generic.edit import DeleteView
from .models import Cash, Category
from datetime import datetime

# Create your views here.
@login_required(login_url='/login/')
def main(request):
    acash = Cash.objects.all()
    events = []

    for cash in acash:
        event = {
            'id': cash.pk,
            'title': "["+cash.category.name+"]  " + str(cash.amount),
            'date': cash.date.strftime('%Y-%m-%d'),
            'stat': cash.stat,
            'extendedProps': {
            'memo': cash.memo,
            },
        }
        events.append(event)

    events_json = json.dumps(events)

    return render(
        request,
        'cashbook/main.html',
        {
            'acash' : acash,
            'events_json' : events_json,
        }
    )


def category_div_in():
    categories = ["월급", "용돈"]
    cate_in = Category.objects.filter(name__in=categories).values('name')
    return cate_in

def category_div_out():
    categories = ["식비", "교통비", "문화생활", "생필품", "의류", "미용", "교육", "저축", "카드대금"]
    cate_out = Category.objects.filter(name__in=categories).values('name')
    return cate_out

def input_form(request):
    actgr = Category.objects.all()

    category_in = category_div_in()
    json.dumps(list(category_in))
    category_out = category_div_out()
    json.dumps(list(category_out))

    if request.method == 'POST':
        amount = request.POST.get('amount')
        status = request.POST.get('btnradio')
        category_name = request.POST.get('category')
        memo = request.POST.get('memo')
        date_str = request.POST.get('date')

        category = Category.objects.get(name=category_name)
        date = datetime.strptime(date_str, '%Y-%m-%d').date()

        cash = Cash.objects.create(
            amount=amount,
            category=category,
            memo=memo,
            date=date,
        )
        cash.stat = status
        cash.save()

        return redirect('/cashbook/')

    return render(
        request,
        'cashbook/inputForm.html',
        {
            'actgr' : actgr,
            'category_in' : category_in,
            'category_out' : category_out,
        }
    )

class DeleteEvent(DeleteView):
    model = Cash
    success_url = '/cashbook/'


def delete_event(request, pk):
    if request.method == 'POST':
        try:
            cash = Cash.objects.get(id=pk)
            cash.delete()

            return JsonResponse({'success': True})
        except Cash.DoesNotExist:
            return JsonResponse({'success': False, 'error': 'Cash object not found.'})
    else:
        return JsonResponse({'success': False, 'error': 'Invalid request method.'})

