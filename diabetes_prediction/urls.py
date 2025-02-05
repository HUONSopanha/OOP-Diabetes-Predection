"""
URL configuration for diabetes_prediction project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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

from dataclasses import field
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from user.views import(
    home_screen_view,
    success_view,
    success1_view,
    diabetes_blog,
    about_us,
)
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home_screen_view, name= 'home'),
    path('success/', success_view, name='success_page'),
    path('success1/', success1_view, name='success1_page'),
    path('diabetes_blog/', diabetes_blog, name = 'diabetes_blog'),
    path('about_us/', about_us, name = 'about_us')
]
