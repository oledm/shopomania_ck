import json 

from django.core.urlresolvers import reverse
from django.test import TestCase
from datetime import datetime, timedelta
from django.utils import timezone

from .models import Customer, Order, Item

class OrderAPITest(TestCase):

    def setUp(self):
        self.now = timezone.now()
        self.later = self.now + timedelta(hours=1)
        Order.objects.get_or_create(date=self.now, author='Олейник') 
        Order.objects.get_or_create(date=self.later, author='Пешкова') 
        self.create_read_url = reverse('api:orders-list')
        self.read_update_delete_url = reverse('api:orders-detail', args=(1,))

    def test_list(self):
        response = self.client.get(self.create_read_url)
        self.assertEquals(response.status_code, 200)
        data = len(response.json())
        self.assertEquals(data, 2)

    def test_detail(self):
        response = self.client.get(self.read_update_delete_url)
        self.assertEquals(response.status_code, 200)
        print('response', self.read_update_delete_url)
        data = {'id': 1, 'date': str(self.now), 'description': 'None',
                'author': 'Олейник', 'comment': 'None'}
        print(response.json())
        self.assertEquals(response.json(), json.dumps(data))

