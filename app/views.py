from ast import Return
from django.shortcuts import render

# Create your views here.
def birds(request):
    return render(request,'birds.html')

def animals(request):
    return render(request,'animals.html')

def flowers(request):
    return render(request,'flowers.html')

def fruits(request):
    return render(request,'fruits.html')