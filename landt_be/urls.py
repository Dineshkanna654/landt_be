"""
URL configuration for landt_be project.

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
from authentication.views import LoginView
from home.views import scan_qr_code, get_all_data
from dash.views import form_data, status_form

urlpatterns = [
    path('admin/', admin.site.urls),
    path('login/', LoginView.as_view(), name='login'),
    path('scan-qr/', scan_qr_code, name='scan_qr_code'),
    path('all-qr-data/', get_all_data, name='get_all_data'),
    path('api/form-data/', form_data, name='form_data'),
    path('api/get-form-data/', status_form, name='post_user_rating'),
]
