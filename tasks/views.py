from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def home(request):
    return HttpResponse("Hello, Python Django World!")
def contact(request):
    return HttpResponse("Contact Us")
def show_tasks(request):
    return HttpResponse("Here are the tasks")