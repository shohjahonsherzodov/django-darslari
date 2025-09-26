from django import forms 
from django.contrib.auth.models import User

class UserCreateForm(forms.ModelForm):
    email = forms.EmailField(required=True)
    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password') 
    def save(self, commit=True):
        user = super().save(commit)
        user.set_password(self.cleaned_data['password'])

        user.save()

        return user
    
class UserLoginForm(forms.Form):
    username = forms.CharField(max_length=60) 
    password = forms.CharField(max_length=60) 
