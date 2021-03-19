from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('<slug:slug>/',views.exp_details, name='exp-details' ),

]