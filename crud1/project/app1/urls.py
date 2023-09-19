from django.urls import path
from . import views


urlpatterns = [
    path('time/',views.filter_datetime,name='time'),
    path("float/",views.float_format,name='float'),
    path('iftag/',views.if_tag,name='iftag')
]
