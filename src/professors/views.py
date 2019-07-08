from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def professors(request, *args, **kwargs):
    test = {
        'name':'Teja',
        'branch':'CSE',
        'city':'Vizag',
        'area':'Seethampeta'
    }
    # return HttpResponse("<h1>This is professors page</h1>")
    return render(request,"prof.html",test)