from django.shortcuts import render
from datetime import datetime
# Create your views here.

def filter_datetime(request):
    d = datetime.now()
    return render(request,'app1/filter.html',{'dt':d})

def float_format(request):
    data ={
        'x':45.2345,
        'y':45.0000,
        'z':45.4600
    }
    return render(request,'app1/float.html',data)

def if_tag(request):
    return render(request,'app1/if_tag.html',{'name':'Zoheb','st':5, 'languages':['python','java','django']})