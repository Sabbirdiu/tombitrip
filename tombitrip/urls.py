"""tombitrip URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static
from blog.views import search
# local
from user import views as userviews
urlpatterns = [
    path('admin/', admin.site.urls),
    path('blog/',include("blog.urls")),
    path('user/',include("user.urls")),
    


    # local 
    path('signup/',userviews.signup_form, name='signup_form'),
    path('login/',userviews.login_form, name='login_form'),
    path('find/',search,name='search'),
    path('logout/',userviews.logout_func, name='logout'),
    path('update/', userviews.user_update,name='user_update'),
]
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL,
                          document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
