from django.http.response import HttpResponse
import random
from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request,'home.html')
def about(request):
    return render(request,'about.html')
def password(request):
    characters = list('abcdefghijklmnopqrstuvwxyz')

    if request.GET.get('uppercase'):
        characters.extend(list('ABCDEFGHIJKLMNOPQRSTUVWXYZ'))
    if request.GET.get('special'):
        characters.extend(list('!@#$%^&*'))
    if request.GET.get('number'):
        characters.extend('123456789')
    
    length = int(request.GET.get('length'))


    thepassword = ''
    for x in range(length):
        thepassword += random.choice(characters)

    return render(request,'password.html',{'password':thepassword})
