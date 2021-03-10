from django.urls import path
from .views import *

urlpatterns = [
    path('', blog,name='blog'),
    path('<slug:slug>/',blogdetails, name='post-detail' ),
    path("category/<slug:slug>/posts", Posts_in_CategoryView, name="posts_in_category"),
]
