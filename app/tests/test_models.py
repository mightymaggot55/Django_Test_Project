from datetime import datetime
from django.test import TestCase
from app.models import Ticket, Staff, Asset
from django.utils.timezone import make_aware
  

class TestAssets(TestCase):

    def test_init(self):
        obj = Asset.objects.get(id=1)
        self.assertEqual(obj.pk, 1)
        
    

