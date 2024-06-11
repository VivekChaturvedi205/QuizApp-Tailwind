from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    return render(request, 'home.html')


def all_chai(request):
    return render(request, 'all_chai.html')
