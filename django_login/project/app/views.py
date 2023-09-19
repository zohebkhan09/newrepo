from django.shortcuts import render
from .models import *
from .forms import UserForm
from .models import Student,Teacher


# Create your views here.
def RegisterPage(request):
    context={}
    context['form']=UserForm
    return render(request,"app/register.html",context)

# View for user registration
def UserRegister(request):
   if request.method == "POST":
    fname = request.POST['Firstname']
    lname = request.POST['Lastname']
    email = request.POST['Email']
    contact = request.POST['Contact']
    password = request.POST['Password']
    cpassword = request.POST['cpassword']
    # First we will validate that user already exist
    user = User.objects.filter(Email=email)

    if user:
        message = "User already exist"
        return render(request,"app/register.html",{'msg':message})
    else:
        if password == cpassword:
            newuser = User.objects.create(Firstname=fname,Lastname=lname,Email=email,Contact=contact,Password=password)
            message = "User register Successfully"
            return render(request,"app/login.html",{'msg':message})
        else:
            message = "Password and Confirm Password Doesnot Match"
            return render(request,"app/register.html",{'msg':message})
#Login VIew

def LoginPage(request):
    return render(request,"app/login.html")
    
    # Login User
def LoginUser(request):
    if request.method == "POST":
        email = request.POST['email']
        password = request.POST['password']

        # Checking the emailid with database
        user = User.objects.filter(Email=email)
        # if not user:
        #     message = "User does not exist"
        #     return render(request,"app/register.html",{'msg':message})
        if user:
            data = User.objects.get(Email=email)
            if data.Password == password:
                # We are getting user data in session
                request.session['Firstname'] = data.Firstname
                request.session['Lastname'] = data.Lastname
                request.session['Email'] = data.Email
                return render(request,"app/home.html")
            else:
                message = "Password does not match"
                return render(request,"app/login.html",{'msg':message})
        else:
            message = "User does not exist"
            return render(request,"app/register.html",{'msg':message})
        

# Create your views here.

def home(request):
    # all()
    data0=Student.objects.all()
    print("SQL Query :", data0.query)
    data1=Student.objects.all().values()
    print("SQL Query :", data1.query)
    return render(request,'app/home.html',{'data0':data0,'data1':data1})
    
    filter(**kwargs)
    data0=Student.objects.filter(stu_city='Bhopal')
    print(data0)
    print("SQL Query :", data0.query)
    return render(request,'app/home.html',{'data0':data0})

    # exclude(**kwargs)
    # data0=Student.objects.exclude(stu_city='Bhopal')
    # print(data0)
    # print("SQL Query :", data0.query)
    # return render(request,'app/home.html',{'data0':data0})

    # order_by()
    # data0=Student.objects.order_by('stu_city') # bydefault assendind order
    # data0=Student.objects.order_by('-stu_city') # desending order
    # data0=Student.objects.order_by('?')
    # data0=Student.objects.order_by('stu_city').order_by('stu_name')
    # print(data0)
    # print("SQL Query :", data0.query)
    # return render(request,'app/home.html',{'data0':data0})
     
    # reverse()
    # data0=Student.objects.order_by('id').reverse()
    # data0=Student.objects.order_by('id').reverse()[:5] # last 5 entries
    # print("SQL Query :", data0.query)
    # print(data0)
    # return render(request,'app/home.html',{'data0':data0})

    # values(*fields) it provides dict formated values
    # data0=Student.objects.values()
    # data0=Student.objects.values('stu_name','stu_city')
    # print(data0)
    # print("SQL Query :", data0.query)
    # return render(request,'app/home.html',{'data0':data0})

    # distinct(*fields) this eleminated duplicate row from the query results.


    # values_list(*fields, flat=False, named=False) it provides tuple formated values
    # data0=Student.objects.values_list()
    # data0=Student.objects.values_list('id','stu_name')
    # data0=Student.objects.values_list('id','stu_name',named=True)
    # data0=Student.objects.values_list('stu_name',flat=True)
    # print(data0)
    # print("SQL Query :", data0.query)
    # return render(request,'app/home.html',{'data0':data0})

    # using(alias) it used when we are working with multiple databases
    # data0=Student.objects.using('default')
    # print(data0)
    # print("SQL Query :", data0.query)
    # return render(request,'app/home.html',{'data0':data0})

    # dates(*field,kind,order='ASC')

    # none()
    # data0=Student.objects.none()
    # print(data0)
    # print("SQL Query :", data0.query)
    # return render(request,'app/home.html',{'data0':data0})


    # union(*other, all=False/True)
    # qur1 = Student.objects.values_list('id','stu_name', named=True)
    # qur2 = Teacher.objects.values_list('id','stu_name', named=True)
    # data0 = qur2.union(qur1,all=True) # all=Ture allow duplicate values
    # data0 = qur2.union(qur1,all=False) # all=False not allow duplicate values
    # print(data0)
    # print("SQL Query :", data0.query) 
    # return render(request,'app/home.html',{'data0':data0})

    # intersection()
    # qur1 = Student.objects.values_list('id','stu_name', named=True)
    # qur2 = Teacher.objects.values_list('id','stu_name', named=True)
    # data0 = qur2.intersection(qur1)
    # data0 = qur1.intersection(qur2)
    # print(data0)
    # print("SQL Query :", data0.query) 
    # return render(request,'app/home.html',{'data0':data0})