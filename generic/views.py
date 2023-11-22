from django.shortcuts import render

# Create your views here.
def gone(request):
    return render(request,'gone.html')

def gtwo(request):
    return render(request,'gtwo.html')