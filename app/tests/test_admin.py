from django.test import TestCase
import pytest
from django.contrib.admin.sites import AdminSite
from django.contrib import admin
from app.models import Ticket, Staff
from app.admin import admin

class TestAdmin(TestCase):
    @classmethod
   
    def setUp(self):
        self.site = AdminSite()
    
