from django import forms
from .models import ContactList


class UserForm(forms.ModelForm):
    class Meta:
        model = ContactList
        fields = ['User_id', 'name', 'address',
                  'profession', 'profession2', 'Phone_Number', 'email']
