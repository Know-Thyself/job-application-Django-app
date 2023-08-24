from django import forms

class ApplicationForm(forms.Form):
    first_name = forms.CharField(max_length=70)
    last_name = forms.CharField(max_length=70)
    email = forms.EmailField()
    date = forms.DateField()
    occupation = forms.CharField(max_length=80)