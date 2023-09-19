from django.http import HttpResponse

# Create your views here.

def f1(req):
    return HttpResponse("this is from f1")

def f2(req):
    return HttpResponse("this is from f2")