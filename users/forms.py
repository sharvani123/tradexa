from django import forms
from .models import Post
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import ReadOnlyPasswordHashField


User=get_user_model()

class UserAdminCreationForm(forms.ModelForm):
    password1=forms.CharField(label='Password', widget=forms.PasswordInput)
    password2=forms.CharField(label='Confirm Password ', widget=forms.PasswordInput)
   
    class Meta:
        model=User
        fields=['first_name','last_name','username','email']
    
    def clean_password2(self):
         #check that the two password entries match
        password1=self.cleaned_data.get("password1")
        password2=self.cleaned_data.get("password2")
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError("Passwords doesn't match")
        return password2

    def save(self, commit=True):

        user=super(UserAdminCreationForm, self).save(commit=False)
        user.set_password(self.cleaned_data['password1'])
        if commit:
            user.save()
        return user

class UserAdminChangeForm(forms.ModelForm):

    password= ReadOnlyPasswordHashField()

    class Meta:
        model = User
        fields = ('username', 'password','active','admin')

    def clean_password(self):
        return self.initial["password"]

class LoginForm(forms.Form):
    username=forms.CharField(label='Username')
    password=forms.CharField(widget=forms.PasswordInput)

class RegisterationForm(forms.ModelForm):

    password1=forms.CharField(label='Password', widget=forms.PasswordInput)
    password2=forms.CharField(label='Confirm Password ', widget=forms.PasswordInput)
   
    class Meta:
        model=User
        fields=('first_name','last_name','username','email')
    
    def clean_password2(self):
        #check that the two password entries match
        password1=self.cleaned_data.get("password1")
        password2=self.cleaned_data.get("password2")
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError("Passwords doesn't match")
        return password2

    def save(self, commit=True):
        #save the provided password in hashed format
        user=super(RegisterationForm, self).save(commit=False)
        user.set_password(self.cleaned_data['password1'])
        
        if commit:
            user.save()
        return user

