from django.conf import settings
from django.urls import path, re_path
from . import views
from .views import LogoutView, ajouter_view, list_view, update_view, delete_view,ajouter_class
from . import views
from django.contrib.auth import views as auth_views
from django.conf.urls.static import static

urlpatterns = [
    
    path('create/', views.ajouter_view, name='ajouter_view'),
    
    path('list/', views.list_view, name='list_view'),
    
    
    path('avion/<int:pk>/update/', views.update_view, name='update_view'),
    path('avion/<int:pk>/delete/', views.delete_view, name='delete_view'),
   
  
    path('', views.acceuil, name='acceuil'),
    path('rechercher/', views.rechercher, name='rechercher'),
     path('dashboard/', views.dashboard, name='dashboard'),
    path('facture/', views.facture, name='facture'),
 
 
    path('reservationform/', views.reservationview, name='reservationform'),

    path('class/', views.class_view, name='class') ,
    path('update_class/<str:pk>/', views.update_class, name='update_class'),
    path('create_class/', views.ajouter_class, name='ajouter_class'),
     path('delete_class/<str:pk>/', views.delete_class, name='delete_class'),
    path('categorie/', views.categorie_view, name='categorie') ,
    path('update_categorie/<int:pk>/', views.update_categorie, name='update_categorie'),
    path('create_categorie/', views.ajouter_categorie, name='ajouter_categorie'),
     path('delete_categorie/<int:pk>/', views.delete_categorie, name='delete_categorie'),

 
    path('login/', views.LoginView.as_view(), name='login'),
    
    path('register/',views.RegisterView.as_view(), name='sign-in') ,

    path('logout/', LogoutView.as_view(), name='logout'),

    path('trajet/', views.trajet_view, name='trajet') ,
    path('trajet_update/<int:pk>/', views.trajet_update, name='trajet_update'),
    path('create_trajet/', views.ajouter_trajet, name='ajouter_trajet'),
    path('delete_trajet/<int:pk>/', views.delete_trajet, name='delete_trajet'),






    path('reservation/', views.reservation_view, name='reservation') ,
    path('delete_reservation/<int:pk>/', views.reservation_delete, name='reservation_delete'),
    path('vol/', views.vol_view, name='vol') ,
    path('vol_update/<int:pk>/', views.vol_update, name='vol_update'),
    path('vol_create/', views.ajouter_vol, name='ajouter_vol'),
    path('delete_vol/<int:pk>/', views.delete_vol, name='delete_vol'),


    path('passager/', views.passager_view, name='passager') ,
    path('user/', views.user_view, name='user')

      
]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

