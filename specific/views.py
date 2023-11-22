from django.shortcuts import render

# Create your views here.
def sone(request):
    return render(request,'sone.html')

def stwo(request):
    return render(request,'stwo.html')