from django import forms
from .models import CustomUser, Profile


class UserCreateForm(forms.ModelForm):
    email = forms.EmailField(required=True)
    class Meta():
        model = CustomUser
        fields = ('username', 'first_name', 'last_name', 'email', 'password')
    
    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data['password'])
        if commit:
            user.save()
        return user
    
class UserUpdateForm(forms.ModelForm):
    class Meta:
        model = CustomUser
        fields = ['username',"first_name","last_name", 'email',"profile_picture"]

class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = CustomUser
        fields = ['username',"first_name","last_name", 'email',"profile_picture"]

    