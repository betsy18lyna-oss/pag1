from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def hello_view(request):
    return HttpResponse("Hello World")

def nombre_view(request):
    return HttpResponse("Mahily Betsabe Orozco Montesdeoca")

