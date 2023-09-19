from django.shortcuts import render
from . forms import RegistrationForm
from .models import User

# Create your views here.
def home (request):
    if request.method=='POST':
        form = RegistrationForm(request.POST)
        print(form)
        if form.is_valid():
            nm = request.POST['name']
            print(nm)
            em = form.cleaned_data['email']
            print(em)
            cont = form.cleaned_data['contact']
            print(cont)
            
            # create or save form data into DB
            new_data = User(name=nm,email=em,contact=cont,)
            new_data.save()
            form=RegistrationForm()
    else:
        form=RegistrationForm()
    return render(request,'app/home.html',{'form':form})
