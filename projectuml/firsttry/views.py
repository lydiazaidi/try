
from datetime import timezone
from decimal import Decimal
from pyexpat.errors import messages
from django import views
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404, redirect
from requests import request
from .models import Avion, AvionVol, Categorie, Classe, Passager, Reservation, Trajet, Vol
from .forms import  AvionForm, ClassForm ,CategorieForm, CombinedForm, PassagerForm, PassagerFormSet, RegisterForm, TrajetForm2, VolForme2
from django.http import HttpResponseForbidden
from django.contrib import messages
from .forms import RegisterForm
from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm
from django.views import View
from django.contrib.auth import  login as auth_login
from django.contrib.auth import logout
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.views import View
from django.contrib.auth.models import User
from django.forms import formset_factory
from .forms import PassagerForm, CustomPassagerFormSet

from .forms import PassagerForm, CustomPassagerFormSet
from .models import Passager









def csrf_failure(request, reason=""):
    return HttpResponseForbidden("CSRF verification failed. Please try again.")


def acceuil(request):
    context = {}
    return render(request, "acceuil.html", context)

def rechercher(request):
    context = {}
    return render(request, "rechercher.html", context)

def login(request):
    context = {}
    return render(request, "login.html", context)


def signin(request):
    context = {}
    return render(request, "sign in.html", context)

def dashboard(request):
    context = {}
    return render(request, "dashboard.html", context)

def facture(request):
    context = {}
    return render(request, "facture.html", context)




# Create
def ajouter_view(request):
    if request.method == 'POST':
        form = AvionForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('list_view')  # Replace with the name of your list view
    else:
        form = AvionForm()

    return render(request, 'ajouter.html', {'form': form})

# Read
def list_view(request):
    queryset = Avion.objects.all()
    return render(request, 'list .html', {'queryset': queryset})


# Update
def update_view(request, pk):
    avion = get_object_or_404(Avion, pk=pk)
    if request.method == 'POST':
        form = AvionForm(request.POST, instance=avion)
        if form.is_valid():
            form.save()
            return redirect('list_view')
    else:
        form = AvionForm(instance=avion)
    return render(request, 'update.html', {'form': form, 'avion': avion})
# Delete
def delete_view(request, pk):
    obj = get_object_or_404(Avion, num_avion=pk)

    if request.method == 'POST':
        # Delete the object if the form is submitted
        obj.delete()
        return redirect('list_view')

    # Pass the object to the template context
    return render(request, 'delete.html', {'x': obj})


def class_view(request):
    queryset = Classe.objects.all()
    return render(request, 'class.html', {'queryset': queryset})

def delete_class(request, pk):
    instance = get_object_or_404(Classe, pk=pk)
    if request.method == 'POST':
        instance.delete()
        return redirect('class')  # Redirect to the list view after successful delete
    return render(request, 'delete_class.html', {'instance': instance})


def update_class(request, pk):
    instance = Classe.objects.get(type=pk)  # Use the correct field for primary key
    form = ClassForm(instance=instance)
    
    if request.method == 'POST':
        form = ClassForm(request.POST, instance=instance)
        if form.is_valid():
            form.save()
            return redirect('class')  # Replace with the name of your list view
    
    return render(request, 'update_class.html', {'form': form, 'instance': instance})

def ajouter_class(request):
    if request.method == 'POST':
        form = ClassForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('class')  # Replace with the name of your list view
    else:
        form = ClassForm()

    return render(request, 'ajouter_class.html', {'form': form})

def ajouter_categorie(request):
    if request.method == 'POST':
        form = CategorieForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('categorie')  # Replace with the name of your list view
    else:
        form = CategorieForm()

    return render(request, 'ajouter_categorie.html', {'form': form})

def categorie_view(request):
    queryset = Categorie.objects.all()
    return render(request, 'categorie.html', {'queryset': queryset})

def update_categorie(request, pk):
    instance = Categorie.objects.get(id_categorie=pk)  # Use the correct field for primary key
    form = CategorieForm(instance=instance)
    
    if request.method == 'POST':
        form = CategorieForm(request.POST, instance=instance)
        if form.is_valid():
            form.save()
            return redirect('categorie')  # Replace with the name of your list view
    
    return render(request, 'update_categorie.html', {'form': form, 'instance': instance}) 


def delete_categorie(request, pk):
    instance = get_object_or_404(Categorie, pk=pk)
    if request.method == 'POST':
        instance.delete()
        return redirect('categorie')  # Redirect to the list view after successful delete
    return render(request, 'delete_categorie.html', {'instance': instance})





#passager


@login_required
def reservationview(request):
    if request.method == 'POST':
        num_forms = int(request.POST.get('num_forms', 1))
        PassagerFormSet = formset_factory(PassagerForm, extra=num_forms)

        formset = PassagerFormSet(request.POST, prefix='passenger')
        if formset.is_valid():
            instances = formset.save(commit=False)

            # Loop through instances and set additional fields
            for instance in instances:
                instance.client = request.user  # Set the client field
                instance.save()

            # Redirect or do something else upon successful form submission
            return redirect('acceuil')
    else:
        # Default to showing one form initially
        PassagerFormSet = formset_factory(PassagerForm, extra=1)
        formset = PassagerFormSet(prefix='passenger')

    return render(request, 'reservationform.html', {'formset': formset})



class RegisterView(View):
    form_class = RegisterForm
    initial = {'key': 'value'}
    template_name = 'sign-in.html'

    def dispatch(self, request, *args, **kwargs):
        # will redirect to the home page if a user tries to access the register page while logged in
        if request.user.is_authenticated:
            return redirect(to='/')

        # else process dispatch as it otherwise normally would
        return super(RegisterView, self).dispatch(request, *args, **kwargs)

    def get(self, request, *args, **kwargs):
        form = self.form_class(initial=self.initial)
        return render(request, self.template_name, {'form': form})

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)

        if form.is_valid():
            form.save()

            first_name = form.cleaned_data.get('first_name')
            messages.success(request, f'Account created for {first_name}')

            return redirect(to='acceuil')

        return render(request, self.template_name, {'form': form})



class LoginView(View):
    form_class = AuthenticationForm
    template_name = 'login.html'

    def get(self, request, *args, **kwargs):
        form = self.form_class()
        return render(request, self.template_name, {'form': form})

    def post(self, request, *args, **kwargs):
        form = self.form_class(request, request.POST)

        if form.is_valid():
            user = form.get_user()
            auth_login(request, user)

            # Check if the entered email is adminsarah@gmail.com
            if user.email == "adminsarah@gmaill.com":
                return redirect('list_view')
            else:
                return redirect('acceuil')
        else:
            for field, errors in form.errors.items():
                for error in errors:
                    messages.error(request, f"{field}: {error}")

            return redirect('login')

class LogoutView(View):
    def get(self, request, *args, **kwargs):
        logout(request)
        return redirect('acceuil') 
    





# Create




def ajouter_trajet(request):
    if request.method == 'POST':
        form = TrajetForm2(request.POST)
        if form.is_valid():
            trajet = form.save(commit=False)  # Save the form data but don't commit to the database yet
            trajet.calculer_prix_et_duree()  # Calculate and update prix, duree, and distance
            trajet.save()  # Commit the changes to the database
            return redirect('trajet')  # Redirect to the list view of trajets
    else:
        form = TrajetForm2()

    return render(request, 'ajouter_trajet.html', {'form': form})


def ajouter_vol(request):
    if request.method == 'POST':
        form = CombinedForm(request.POST)
        if form.is_valid():
            vol = form.save(commit=False)
            num_avion_pk = form.cleaned_data['num_avion'].pk
            num_avion = Avion.objects.get(pk=num_avion_pk)  # Retrieve Avion instance




            # Check if aircraft has enough autonomy for the flight
            distance_to_travel = vol.trajet.distance  # Assuming Trajet has a 'distance' field
            aircraft = Avion.objects.get(num_avion=num_avion_pk)
            if aircraft.autonomie < distance_to_travel:
                return HttpResponse("Aircraft does not have enough autonomy for this flight.")


            # Check if the aircraft is available at the scheduled departure time
            scheduled_departure_datetime = timezone.datetime.combine(vol.dateD, vol.timeD)
            conflicting_flights = AvionVol.objects.filter(num_avion=num_avion_pk)
            if conflicting_flights.exists():
                return HttpResponse("Aircraft is already in use at the scheduled departure time.")


            vol.save()
            AvionVol.objects.create(num_avion=aircraft, num_vol=vol)        
            return redirect('vol')  # Redirect to the flight list view
    else:
        form = CombinedForm()


    return render(request, 'ajouter_vol.html', {'form': form})




# Read
def trajet_view(request):
    queryset = Trajet.objects.all()
    return render(request, 'trajet.html', {'queryset': queryset})




def reservation_view(request):
    queryset = Reservation.objects.all()
   
    return render(request, 'reservation.html', {'queryset': queryset})


def vol_view(request):
    queryset1 = Vol.objects.all()
    queryset2 = AvionVol.objects.select_related('num_vol').all()
   
    return render(request, 'vol.html', {'queryset': queryset1  ,'queryset2':queryset2})


def reservation_view(request):
    queryset = Reservation.objects.all()  
    return render(request, 'reservation.html', {'queryset': queryset})




def passager_view(request):
    queryset = Passager.objects.all()  
    return render(request, 'passager.html', {'queryset': queryset})


def user_view(request):
    queryset = User.objects.all()  
    return render(request, 'user.html', {'queryset': queryset})






# Update


def trajet_update(request, pk):
    instance = Trajet.objects.get(idtrajet=pk)  # Use the correct field for primary key
    form = TrajetForm2(instance=instance)
   
    if request.method == 'POST':
        form = TrajetForm2(request.POST, instance=instance)
        if form.is_valid():
            trajet=form.save()
            trajet.calculer_prix_et_duree()
            return redirect('trajet')  # Replace with the name of your list view
   
    return render(request, 'trajet_update.html', {'form': form, 'instance': instance})




def vol_update(request, pk):
    instance = Vol.objects.get(num_vol=pk)  # Use the correct field for primary key
    form = VolForme2(instance=instance)
   
    if request.method == 'POST':
        form = VolForme2(request.POST, instance=instance)
        if form.is_valid():
            form.save()
            return redirect('vol')  # Replace with the name of your list view
   
    return render(request, 'update_vol.html', {'form': form, 'instance': instance})


# Delete




def delete_trajet(request, pk):
    instance = get_object_or_404(Trajet, pk=pk)
    if request.method == 'POST':
        instance.delete()
        return redirect('trajet')  # Redirect to the list view after successful delete
    return render(request, 'delete_trajet.html', {'instance': instance})




def reservation_delete(request, pk):
    instance = get_object_or_404(Reservation, pk=pk)
    if request.method == 'POST':
        instance.delete()
        return redirect('reservation')  # Redirect to the list view after successful delete
    return render(request, 'reservation_delete.html', {'instance': instance})




def delete_vol(request, pk):
    instance = get_object_or_404(Vol, pk=pk)
    if request.method == 'POST':
        instance.delete()
        return redirect('vol')  # Redirect to the list view after successful delete
    return render(request, 'delete_vol.html', {'instance': instance})