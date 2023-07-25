from django.shortcuts import render

# Create your views here.

def first_2(request):
    return render(request,'text3.html')

def second_2(request):
    return render(request,'text4.html')
