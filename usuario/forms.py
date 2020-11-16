from django import forms
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from django.contrib.auth.models import User

class registroForm(UserCreationForm):
    edad = forms.IntegerField();
    password1 = forms.CharField(label = "Contraseña",widget = forms.PasswordInput)
    password2 = forms.CharField(label = "Confirma contraseña",widget = forms.PasswordInput)
    
    class Meta:
        model = User
        fields = ['username','edad','password1','password2']
        help_texts = {k: "" for k in fields}
        
class loginForm(AuthenticationForm):
    username = forms.CharField(label = "Usuario")
    password = forms.CharField(label = "Contraseña",widget = forms.PasswordInput)