from urllib import request
from django.contrib.auth.decorators import login_required
from django.core.exceptions import ValidationError
from django.views.generic import TemplateView
from datetime import datetime
from django.shortcuts import render
from django.http import HttpRequest, HttpResponseBadRequest, HttpResponseRedirect, HttpResponse
#from .forms import UserForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import AuthenticationForm


class LoginView(TemplateView):
    template_name = 'registration/login.html'


@login_required(login_url='/accounts/login')
class HomeView(TemplateView):
    template_name = 'home.html'


class OverviewView(TemplateView):
    template_name = 'overview.html'


class ContactView(TemplateView):
    template_name = 'contact.html'


class DetailsView(TemplateView):
    template_name = 'details.html'


class LogoutView(TemplateView):
    template_name = 'registration/logged_out.html'


