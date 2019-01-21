"""roster URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
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
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings
from . import views
from core.views import celery_test, celery_res

urlpatterns = [
    path('', views.home),
    path('admin/', admin.site.urls),
    path('api/user/', include('user.urls')),
    path('api/shift/', include('shift.urls')),
    path('accounts/login/', views.acc_login),
    path('accounts/logout/', views.acc_logout, name="logout"),
    path('celery_test/', celery_test),
    path('celery_res/', celery_res),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
