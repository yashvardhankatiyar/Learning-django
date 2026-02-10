from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def home(request) :
    return render(request,'home.html')
    
def add(request) :
    #number 1
    num1 = int(request.GET['num1'])
    #number 2
    num2 = int(request.GET['num2'])
    result  = num1 + num2
    return render(request, 'result.html', {'result' : result})