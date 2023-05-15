from django import forms


class Studform(forms.Form):
    s_name = forms.CharField(max_length=30, label='Student Name')
    s_class = forms.CharField(max_length=30, label='Class')
    s_addr = forms.CharField(max_length=30, label='Address')
    s_school = forms.CharField(max_length=30, label='School')
    s_email = forms.EmailField(max_length=30, label='Student Email')

class Sform(forms.Form):
     s_name = forms.CharField(max_length=30, label='Student Name')
