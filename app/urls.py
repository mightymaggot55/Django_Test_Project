"""testing_environment_02 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
from app import views
from django.views.generic import TemplateView
from django.contrib.auth import views as auth_views
from django.contrib.auth.decorators import login_required

urlpatterns = [
    path(r'', auth_views.LoginView.as_view(template_name='registration/login.html')),
    path(r'admin/', admin.site.urls),
    path(r'home/', login_required(TemplateView.as_view(template_name='home.html')), name='home'),
    path(r'overview/', views.OverviewView.as_view(), name='overview'),
    path(r'contact/', views.ContactView.as_view(), name='contact'),
    path(r'details/', views.DetailsView.as_view(), name='details'),
    path('api/', include('api.urls')),
    path(r'accounts/', include("django.contrib.auth.urls")),
    path(r'accounts/logout', auth_views.LogoutView.as_view(), name='logged_out.html'),
    # path(r'change-password/', auth_views.PasswordChangeView.as_view()),
]
