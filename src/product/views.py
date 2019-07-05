from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def product_page(*args, **kwargs):
    return HttpResponse('<h1>This is products page</h1>')
