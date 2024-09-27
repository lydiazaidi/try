
import uuid
from django import forms
from django.contrib.auth.models import User
from django.forms import formset_factory

from django.contrib.auth.forms import AuthenticationForm
from .models import Avion, AvionVol, Categorie, Classe, Client, Passager, Reservation, Trajet, Vol
from django.contrib.auth.forms import UserCreationForm
from django.utils.text import slugify
from django.forms import BaseModelFormSet






class ClassForm(forms.ModelForm):
    class Meta:
        model = Classe
        fields = '__all__'

class CategorieForm(forms.ModelForm):
    class Meta:
        model = Categorie
        fields = '__all__'
    



class AvionForm(forms.ModelForm):
    class Meta:
        model = Avion
        fields = ['num_avion', 'autonomie', 'moteur']

class PassagerForm(forms.ModelForm):
    class Meta:
        model = Passager
        exclude = ['id_passager', 'client']
        widgets = {'dateN': forms.DateInput(attrs={'type': 'date'})}
        fields = ['nom', 'prenom', 'categorie', 'dateN']
        widgets = {
            'categorie': forms.Select(attrs={'class': 'form-control'}),
        }
PassagerFormSet = formset_factory(PassagerForm)
class CustomPassagerFormSet(BaseModelFormSet):
    def save(self, commit=True):
        instances = super().save(commit=False)

        for instance in instances:
            instance.categorie = instance.cleaned_data['categorie']
            instance.client = self.request.user
            instance.save()

        self.save_m2m()

        return instances
        
   
class RegisterForm(UserCreationForm):
    # fields we want to include and customize in our form
    username = forms.CharField(required=False, widget=forms.HiddenInput)
    first_name = forms.CharField(max_length=100,
                                 required=True,
                                 widget=forms.TextInput(attrs={
                                                              'class': 'form-control'
                                                               }))
    last_name = forms.CharField(max_length=100,
                                required=True,
                                widget=forms.TextInput(attrs={
                                                             'class': 'form-control'
                                }))
    email = forms.EmailField(required=True,
                             widget=forms.TextInput(attrs={
                                                           'class': 'form-control'
                                                           }))
    password1 = forms.CharField(max_length=50,
                                required=True,
                                widget=forms.PasswordInput(attrs={
                                                                  'class': 'form-control',
                                                                  'data-toggle': 'password',
                                                                  'id': 'password',
                                                                  }))
    password2 = forms.CharField(max_length=50,
                                required=True,
                                widget=forms.PasswordInput(attrs={
                                                                  'class': 'form-control',
                                                                  'data-toggle': 'password',
                                                                  'id': 'password',
                                                                  }))

    class Meta:
        model = User
        fields = ['first_name', 'last_name','email', 'password1', 'password2']

    def save(self, commit=True):
        user = super().save(commit=False)
        
        # Generate a unique username based on the user's email
        user.username = slugify(self.cleaned_data['email'])
        
        if commit:
            user.save()
        return user


 
    
class AuthenticationForm(AuthenticationForm):
     class Meta:
        model = User




class TrajetForm(forms.ModelForm):
    class Meta:
        model = Trajet
        fields = '__all__'        


class TrajetForm2(forms.ModelForm):
    class Meta:
        model = Trajet
        fields = ['idtrajet','villeD','villeA']        
               


class ReservationForm(forms.ModelForm):
    class Meta:
        model = Reservation
        fields = '__all__'        
       




class VolForme(forms.ModelForm):
    class Meta:
        model = Vol
        fields = '__all__'
       


class AvionVolForm(forms.ModelForm):
    class Meta:
        model = AvionVol
        fields = '__all__'
class CombinedForm(forms.ModelForm):
    class Meta:
        model = Vol
        fields = '__all__'


    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['num_avion'] = forms.ModelChoiceField(queryset=Avion.objects.all(), empty_label=None)
   
   
class VolForme2(forms.ModelForm):
    class Meta:
        model = Vol
        fields = ['trajet','dateD','timeD','img']    
        
        

