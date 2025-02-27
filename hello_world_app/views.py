from django.shortcuts import render, HttpResponse

def hello(request):
    return HttpResponse("Hello, World! Welcome to the future site of FlixList. ")

# Create your views here.
