from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def professors(request, *args, **kwargs):
    # return HttpResponse("<h1>This is professors page</h1>")
    return render(request,"prof.html",{})