from django.shortcuts import render

# Create your views here.
def show_chart(reqeust):
    context = {}
    return render(reqeust, 'chart_test/chart_view.html', context=context)
