from django.urls import path,re_path
from . import views 
from django.contrib import admin
from django.contrib.auth import views as auth_views

urlpatterns = [
  
    #shebin shaji Admin section
    path('',views.load_admin,name='load_admin'),
    path('load_leads',views.load_leads,name='load_leads'),
    path('load_concilors',views.load_concilors,name='load_concilors'),
    path('load_docofficers',views.load_docofficers,name='load_docofficers'),
    path('load_documets',views.load_documets,name='load_documets'),
    path('load_completed',views.load_completed,name='load_completed'),
    path('load_cuttentdoc',views.load_cuttentdoc,name='load_cuttentdoc'),
    path('load_admin_profile',views.load_admin_profile,name='load_admin_profile'),
    path('load_previous_lead',views.load_previous_lead,name='load_previous_lead'),
    path('load_previous_consilers',views.load_previous_consilers,name='load_previous_consilers'),
    path('load_admin_clients_more',views.load_admin_clients_more,name='load_admin_clients_more'),
    path('load_admin_client_compstatus',views.load_admin_client_compstatus,name='load_admin_client_compstatus'),
]