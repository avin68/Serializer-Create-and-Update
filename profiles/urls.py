"""DjangoRestFramework URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from django.urls import path

from profiles import views

urlpatterns = [
    # path('', views.profile_list, name='profile_list')
    path('', views.ProfileView.as_view(), name='ProfileView'),
    # path('<int:pk>', views.RetrieveProfileView.as_view(), name='RetrieveProfileView'),
    path('<int:pk>', views.RetrieveUpdateDestroyAPIViewProfile.as_view(), name='RetrieveUpdateDestroyAPIViewProfile')

]
