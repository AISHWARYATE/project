from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import User
from .models import trolling
from django.forms import ModelForm, TextInput
from .models import City,boat
from .models import products
from .models import fishermen

class LoginForm(forms.Form):
    username = forms.CharField(
        widget= forms.TextInput(
            attrs={
                "class": "form-control"
            }
        )
    )
    password = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                "class": "form-control"
            }
        )
    )


class SignUpForm(UserCreationForm):
    username = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "class": "form-control"
            }
        )
    )
    password1 = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                "class": "form-control"
            }
        )
    )
    password2 = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                "class": "form-control"
            }
        )
    )
    email = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "class": "form-control"
            }
        )
    )

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2', 'is_admin', 'is_employee', 'is_customer')

class trollingForm(forms.ModelForm):
    class Meta:
        model=trolling
        # fields=('alert')
        fields='__all__'

class CityForm(ModelForm):
    class Meta:
        model = City
        fields = ['name']
        widgets = {
            'name': TextInput(attrs={'class' : 'input', 'placeholder' : 'City Name'}),
        } #updates the input class to have the correct Bulma class and placeholder


class productForm(ModelForm):
    class Meta:
        model=products
        fields=['product_name','product_dis','product_cost','product_img']


class AddBoat(forms.ModelForm):
    class Meta:
        model=boat
        fields=['boat_no','boat_name','no_of_fishermen','boat_length','upload_photo']


class addfishermen(forms.ModelForm):
    class Meta:
        model=fishermen
        fields=['fname','city','age','phone']