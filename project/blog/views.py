from django.shortcuts import render
from django.http import HttpResponse
from templates import *
# Create your views here.


def About(request):
    return render(request, 'about.html')

def Home(request):
    return render(request, 'home.html')

def Interview(request):
    return render(request, 'interviews.html')

def IViewers(request):
    return render(request, 'books.html')

def Blog(request):
    context = {
        "data":[("World","Featured post","Nov 12","This is a wider card with supporting text below as a natural lead-in to additional content","https://source.unsplash.com/1400x400/?teaching","inter_viewer"),("Open Access , Publishing","Katharine Dunn: Open access is still viewed as a bold step—when it should be the norm","July 18 2022","Dissemination of knowledge” is a core value that people return to again and again when making decisions around open sharing—including during the creation of OCW, DSpace, and MIT’s faculty OA policy.","https://openinterview.org/wp-content/uploads/2022/07/Katharine_Dunn-Open_Interview-MIT-Santosh_C_Hulagabali-removebg-preview.png","inter_viewer"),("Avinash","Gourav","Abhishek","Manish","https://source.unsplash.com/1400x400/?emotions","inter_viewer"),("Avinash","Gourav","Manish","Abhishek","https://source.unsplash.com/1400x400/?teaching","inter_viewer")],
        "arch":["January","February","March","April","June","July","August","September","Octorber","November","December"],
        "caro":[("https://source.unsplash.com/1400x400/?teaching",True),("https://source.unsplash.com/1400x400/?emotions",False),("https://source.unsplash.com/1400x400/?social,learning",False)],
        "images":["https://source.unsplash.com/1400x400/?teaching","https://source.unsplash.com/1400x400/?emotions","https://source.unsplash.com/1400x400/?social,learning"],
        "about":'/about',
        "index":'/',
        "inter":'/inter',
        "interviewer":'/inter_viewer',
        "home":'/home',
        "bg":'darkBG.jpg',
        "vol":'/volunteer',
        "vol_tra":'/vol_tra',
        "con":'/contact',
    }
    return render(request, 'nbase.html',context)

def Xyz(request):
    return render(request, 'xyz.html')


def contact(request):
    return render(request, 'books.html')

def joinAsInter(request):
    return render(request, 'books.html')

def joinAsVolun(request):
    return render(request, 'books.html')

def joinAsTrans(request):
    return render(request, 'books.html')

def faqs(request):
    return render(request, 'books.html')

def recomInter(request):
    return render(request, 'books.html')


def volunters(request):
    return render(request, 'books.html')

def thirdParty(request):
    return render(request, 'books.html')

def usefulLinks(request):
    return render(request, 'books.html')

def testimonials(request):
    return render(request, 'books.html')

def feedback(request):
    return render(request, 'books.html')

def support(request):
    return render(request, 'books.html')

def desclaimer(request):
    return render(request, 'books.html')

