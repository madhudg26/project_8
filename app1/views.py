from django.shortcuts import render

# Create your views here.
def firstapp(request):
    return render(request,'genaric.html')