from django.shortcuts import render

# Create your views here.
def Home1(req):
    return render(req,'app2/home1.html')
