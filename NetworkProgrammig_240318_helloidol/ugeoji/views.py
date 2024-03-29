from django.shortcuts import render

# Create your views here.

def show_seoyoung(request) :
    return render(request, 'ugeoji/seoyoung.html')

def show_haewon(request) :
    return render(request, 'ugeoji/haewon.html')

def show_seohyeon(request) :
    return render(request, 'ugeoji/seohyeon.html')