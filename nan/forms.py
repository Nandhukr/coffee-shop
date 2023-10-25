from django import forms
from django.contrib.auth.models import User



from nan.models import MenuItem
from django.contrib.auth.models import User



class ContactForm(forms.Form):
    name = forms.CharField(max_length=100)
    phone = forms.CharField(max_length=15, required=False)
    email = forms.EmailField()
    message = forms.CharField(widget=forms.Textarea)


class MenuItemForm(forms.ModelForm):
    class Meta:
        model=MenuItem
        fields="__all__"