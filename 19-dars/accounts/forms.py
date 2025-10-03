from django import forms
from .models import Profile, CustomUser


class UserCreateForm(forms.ModelForm):
    class Meta():
        model = CustomUser
        fields = ("username", "first_name", "last_name", "email", "password")
    
        def save(self, commit=True):
            user = super().save(commit=False)
            user.set_password(self.cleaned_data["password"]) 
            if commit:
                user.save()
            return user
        
class UserLoginForm(forms.Form):
    username = forms.CharField(max_length=60)
    password = forms.CharField(max_length=60)

class UserUpdateForm(forms.ModelForm):
    class Meta:
        model = CustomUser
        fields = ['username', 'email']

class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['avatar', 'first_name', 'last_name']
