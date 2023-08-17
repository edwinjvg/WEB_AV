from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
        
class UserCreateForm(UserCreationForm):
    email = forms.EmailField(label="Email Usuario")
    password1= forms.CharField(label="Clave", widget=forms.PasswordInput)
    password2= forms.CharField(label="Confirmar Clave", widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
        help_texts = {k:"" for k in fields}    

class UserUpdateForm(UserCreationForm):
    email = forms.EmailField(label="Modificar E-mail")
    password1 = forms.CharField(label='Clave', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Confirmar Clave', widget=forms.PasswordInput) 
    first_name = forms.CharField(label="Nombre", max_length=60, required=False)
    last_name = forms.CharField(label="Apellido", max_length=60, required=False)

    class Meta:
        model = User
        fields = [ 'email', 'password1', 'password2', 'first_name', 'last_name' ] 
        help_texts = { k:"" for k in fields}

class UserAvatarForm(forms.Form):
    image = forms.ImageField(required=True)        