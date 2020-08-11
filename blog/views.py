from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse

# def index(request):
#     return HttpResponse('welcome to my blog!')

def index(request):
    return render(request,'blog/index.html',context={
        'title':'Home page of my blog',
        'welcome':'Welcome to my blog',
    })