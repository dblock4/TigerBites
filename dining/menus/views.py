from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return HttpResponse("TigerBites says hello world!")

def suggestion(request):
    return HttpResponse("Write your suggestion below")
