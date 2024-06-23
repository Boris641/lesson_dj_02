from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    return render(request,'zero_02/index.html')
def new(request):
    return render(request,'zero_02/new.html')

def opinions(request):
    return render(request,'zero_02/opinions.html')

def contacts(request):
    return render(request,'zero_02/contacts.html')

