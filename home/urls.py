from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('details/<slug:slug>/',views.exp_details, name='exp-details' ),
    path('favourite/<int:id>/',views.favourite,name='favourite'),
    path('favourites/', views.favourite_list, name='favourite_list'),

]