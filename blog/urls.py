from django.urls import path
from .views import *

urlpatterns = [
    path('', blog,name='blog'),
    path('<slug:slug>/',blogdetails, name='post-detail' ),
]
