from django import forms


class SyudentRegistration(forms.Form):
    first_name = forms.CharField(error_messages={'required':'Enter your name'}) # _ converted into space and first charector converted into Uppercase
    email = forms.EmailField(label='Your Email', label_suffix='',initial='neeraj@gmail.com', required=False,disabled=True)
    contact = forms.CharField(help_text='limit 20 char')
    password = forms.CharField()