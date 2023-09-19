def formdata(request):
    form = StudentRegistration(auto_id='id_%s', initial={'first_name':'Neeraj','email':'neeraj@gmail.com','contact':'9424444348'}) # bydefault----<label for="id_name">
    return render(request,'app/registration.html',{'form':form})