"""
URL configuration for ServerLa_Aeneta project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from TESCOM_MAIN.views import login_alumno, forgot_password, up_protocol, success

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', login_alumno, name='login'),
    path('forgot-password/', forgot_password, name='forgot-password'),
    path('up-protocol/', up_protocol, name='up-protocol'),
    path('success/', success, name='success')
]
