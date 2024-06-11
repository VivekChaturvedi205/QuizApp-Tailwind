from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms

class Registeruser(UserCreationForm):
    class Meta:
        model=User
        fields=('first_name', 'last_name', 'username','email', 'password1','password2')
        
        
class UsernamePasswordResetForm(forms.Form):
    username = forms.CharField(max_length=150)
    new_password1 = forms.CharField(widget=forms.PasswordInput)
    new_password2 = forms.CharField(widget=forms.PasswordInput)

    def clean(self):
        cleaned_data = super().clean()
        new_password1 = cleaned_data.get("new_password1")
        new_password2 = cleaned_data.get("new_password2")

        if new_password1 and new_password2 and new_password1 != new_password2:
            raise forms.ValidationError("Passwords do not match.")

        return cleaned_data