from django.shortcuts import render

# Create your views here.
def secondapp(request):
    return render(request,'gen2.html')