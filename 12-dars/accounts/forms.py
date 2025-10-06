from django import forms 
from django.contrib.auth.models import User

class UserCreateForm(forms.Form):
    email = forms.EmailField(required=True)
    class Meta():
        model = User
        fields = ('username', 'email', 'first_name', 'last_name', 'password')

        def save(self, commit=True):
            user = super().save(commit=False)
            user.set_password(self.cleaned_data['password'])
            if commit:
                user.save()
            return user

