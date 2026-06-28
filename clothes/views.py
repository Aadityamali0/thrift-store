from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    # return HttpResponse('the app is working')
    return render(request, 'clothes/index.html')

def carousel(request):
    return render(request, 'clothes/navbar.html')