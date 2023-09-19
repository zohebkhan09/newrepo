from django.http import HttpResponse


def home(request):# http request
    return HttpResponse('Welcome All')