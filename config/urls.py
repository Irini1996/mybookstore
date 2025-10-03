"""
URL configuration for config project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
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
from django.contrib import admin #Import Django’s admin site.
#This gives us the ready-made /admin/ route for the backend interface

from django.urls import path, include  #Import path → used to define URL routes.
#Import include → lets us “include” another app’s URL patterns (like store.urls).

urlpatterns = [
    path('admin/', admin.site.urls), #Makes the admin site available at http://127.0.0.1:8000/admin/
    path('', include('store.urls')),  #for all other URLs, look inside store/urls.py to find the correct view
]