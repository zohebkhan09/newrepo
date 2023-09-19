from django.shortcuts import render,redirect
from .models import Student
from django.http import HttpResponse

# Create your views here.
def home(req):
    return render(req,'reg/home.html')

def insert(req):
    if req.method=="POST":
       print(req.POST)  
       fn=req.POST.get('fn')
       ag=req.POST.get('ag')
       em=req.POST.get('em')
       im=req.FILES.get('img')
       instance=Student(name=fn,email=em,age=ag,image=img)
       instance.save()
    return render(req,'reg/insert.html')

def update(req):
    if req.method=="POST":
       print(req.POST)  
       a=req.POST.get('fn')
       c=req.POST.get('ag')
       d=req.POST.get('em')
       e=req.FILES.get('img')
    if e==None:
        Student.objects.filter(id=id).update(name=a,lname=b,age=c,email=d)
        return HttpResponseRedirect('/displaydata/')
    else:
        data=Student(id=id,name=a,lname=b,age=c,email=d,image=e)
        data.save()
        return HttpResponseRedirect('/displaydata')
    d1=Student.objects.get(pk=id)
    return render(req,'reg/update.html',{'data0':d1})

def delete(req,id):
    d=Student.objects.get(pk=id)
    d.delete()
    return HttpResponse('display')

def display(req):
    print(req)
    d=Student.objects.all() 
 #queryset
    return render(req,'reg/display.html',{'data':d})