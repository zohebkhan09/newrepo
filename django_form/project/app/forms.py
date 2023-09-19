from django import forms

class RegistrationForm(forms.Form):
    name=forms.CharField(error_messages={'required':'Enter your name'}) # _ converted into space and first charector converted into Uppercase
    email=forms.EmailField(label='Your Email',label_suffix='',initial='zohebukhan09@gmail.com',)
    contact=forms.CharField(min_length=10, max_length=10, help_text='limit 10 char')


    def clean(self):
        cleaned_data = super().clean()
        val_name = self.cleaned_data['name']
        val_email = self.cleaned_data['email']
        val_contact = self.cleaned_data['contact']
        if len(val_name)<4:
            raise forms.ValidationError('Name must be greater than 4 characters')
        elif len(val_email)<10:
            raise forms.ValidationError('Email must be greater than 10 characters')
        elif len(val_contact)!=10:
            raise forms.ValidationError('Contact must be eqaul to 10 characters')
    