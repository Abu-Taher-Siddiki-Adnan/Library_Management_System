from django import forms
from .models import Books,Employee
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm,UsernameField,PasswordChangeForm


class BookForm(forms.ModelForm):
    class Meta:
        model = Books
        fields = ['title','author','genre','publisher','publication_date','available_copies']
        labels = {
            'title': 'Title',
            'author': 'Author',
            'genre': 'Genre',
            'publisher': 'Publisher',
            'publication_date':'Publication Date',
            'available_copies': 'Available Copies'
        }
        widgets = {
            'title': forms.TextInput(attrs={'class': 'formcontrol'}),
            'author': forms.TextInput(attrs={'class': 'formcontrol'}),
            'genre': forms.TextInput(attrs={'class': 'formcontrol'}),
            'publisher': forms.TextInput(attrs={'class': 'formcontrol'}),
            'publication_date': forms.DateInput(attrs={'class': 'formcontrol'}),
            'available_copies': forms.NumberInput(attrs={'class': 'formcontrol'})
        }
        
class RegistrationForm(UserCreationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={'autofocus' : 'True','class':'form-control'}))
    email = forms.EmailField(widget=forms.EmailInput(attrs={'autofocus' : 'True','class':'form-control'}))
    password1 = forms.CharField(label='Password', widget=forms.PasswordInput(attrs={'autofocus' : 'True','class':'form-control'}))
    password2 = forms.CharField(label='Confirm Password', widget=forms.PasswordInput(attrs={'autofocus' : 'True','class':'form-control'}))
    
    class Meta:
        model = User
        fields = ['username','email','password1','password2']
        
class LoginForm(AuthenticationForm):
    username = UsernameField(widget=forms.TextInput(attrs={'autofocus' : 'True','class':'form-control'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'autofocus' : 'True','class':'form-control'}))
    
class ProfileForm(forms.ModelForm):
    class Meta:
        model = Employee
        fields =['name','mobile', 'email', 'address', 'position',]
        widgets = {
            'name': forms.TextInput(attrs={'class':'form-control'}),
            'mobile': forms.TextInput(attrs={'class':'form-control'}),
            'email': forms.EmailInput(attrs={'class':'form-control'}),
            'address': forms.TextInput(attrs={'class':'form-control'}),
            'position': forms.Select(attrs={'class':'form-control'}),
        }

class MyPasswordChangeForm(PasswordChangeForm):
    old_password = forms.CharField(
        label='Old Password',
        widget=forms.PasswordInput(attrs={'autofocus': 'True', 'autocomplete': 'current-password', 'class': 'form-control'})
    )
    new_password1 = forms.CharField(
        label='New Password',
        widget=forms.PasswordInput(attrs={'autocomplete': 'current-password', 'class': 'form-control'})
    )
    new_password2 = forms.CharField(
        label='Confirm New Password',
        widget=forms.PasswordInput(attrs={'autocomplete': 'current-password', 'class': 'form-control'})
    )
