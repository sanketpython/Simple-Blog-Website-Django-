from django.shortcuts import render
from django.shortcuts import HttpResponse

def index(request):
    context = {
        'variable': "Harry is great"

    }
    return render(request, 'index.html',context)

def about(request):
    return  render(request, 'about.html')

def services(request):
    return  render(request, 'services.html')

def contact(request):
    return  render(request, 'contact.html')

def Open(request):
    return  render(request, 'blog1.html')














