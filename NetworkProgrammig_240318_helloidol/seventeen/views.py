from django.shortcuts import render

# Create your views here.

def show_원우(request) :
    return render(request, 'seventeen/원우.html')

def show_디에잇(request) :
    return render(request, 'seventeen/디에잇.html')