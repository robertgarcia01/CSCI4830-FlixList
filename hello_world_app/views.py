from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return render(request, 'index_hello.html')

def about(request):
    return render(request, 'about_hello.html')

# Create your views here.
