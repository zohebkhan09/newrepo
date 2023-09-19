from django.shortcuts import render

def home(req):
    print (req)
    return render(req,"academics/index.html")

def about(req):
    print (req)
    return render(req,"academics/about.html")

def contact(req):
    print (req)
    return render(req,"academics/contact.html")

def service(req):
    print (req)
    return render(req,"academics/service.html")