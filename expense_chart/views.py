from django.shortcuts import render

# Create your views here.
def mainchart(request):
    return render(
        request,
        'expense_chart/main_chart.html',
    )