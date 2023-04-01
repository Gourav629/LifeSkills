from django.shortcuts import render
from django.http import HttpResponse
from templates import *
# Create your views here.

def Index(request):
    return render(request, 'index.html')

def Home(request):
    return render(request, 'home.html')

def Temp(request):
    return render(request, 'temp.html')

def About(request):
    return render(request, 'about.html')

def Abc(request):
    context = {
        'data':["1.jpeg","2.jpeg","3.jpeg","5.jpeg"],
        'carosel':[
        ("teaching.jpeg","Reading is a good habit","All great leaders are good readers.",True),
        ("social.jpeg","So many books , so little time","The more you practice, the more you'll become good at it",False),
        ("emotions.jpeg","Writing is an art","Books are your best friend. Spend most time with them",False),
        ]
    }
    return render(request, 'nbase.html',context)

def Xyz(request):
    return render(request, 'xyz.html')

def Blog(request):
    return render(request, 'blog/nbase.html',{'title':'Blog','cname':'Blog','data':["1.jpeg","2.jpeg","3.jpeg","5.jpeg"]})