from django.http import HttpResponse
from django.shortcuts import render


def say_hello(request):
    return HttpResponse("Hello World")

def say_hello_html(request):
    return render(request, 'playground/hello.html', {'name': '안녕 친구야', 'greetting': '안녕. 잘가.'})

def say_bye_html(request):
    context = {
        'singer' : '몰라',
        'title' : '또 만나요'
    }
    return render(request, 'playground/bye.html', context=context)