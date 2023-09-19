from django.shortcuts import render
from .forms import Registration 

# Create your views here.

fm = Registration

def home(req):
    return render(req,'app/home.html',{'form':fm})