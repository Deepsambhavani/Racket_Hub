from django.http import HttpResponse
from django.shortcuts import render

def home(request):
    #return HttpResponse("Hello, I'M Deep This is home")
    return render(request,'website/index.html')
def about(request):
    return HttpResponse("Hello, I'M Deep This is about")
def contact(request):
    return HttpResponse("Hello, I'M Deep This is contact")
