from django.urls import path

from . import views

urlpatterns = [
    path('supply/', views.supply, name='supply'),

]