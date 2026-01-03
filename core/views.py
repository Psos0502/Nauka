from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index(response):
    return HttpResponse("</h2>Tu narazie jest sciernisko ale bedzie... kasyno</h2>")
def v1(response):
    return HttpResponse("<h2>Wersja 1 strony</h2>")
