import datetime
from unittest import TestCase

from django.urls import reverse
from rest_framework.test import APIClient

from period_cycle_api.models import PeriodCylceModel



class TestCreateCycle(TestCase):
    client = APIClient()
    url = reverse('create-cycles')

    def test_users_cannot_post_empty_data(self):
        payload = {
            "last_period_date": "",
            "start_date": "",
            "end_date": "",
            "cycle_average": "",
            "period_average": ""
        }
        res = self.client.post(self.url, payload)
        self.assertEqual(res.status_code, 400)

    def test_users_can_post_valid_data(self):
        payload = {
            "last_period_date": "2021-06-01",
            "start_date": "2021-07-01",
            "end_date": "2021-12-01",
            "cycle_average": 25,
            "period_average": 5,
        }
        res = self.client.post(self.url, payload)
        self.assertEqual(res.status_code, 200)

    def test_circle_calculation_is_correct(self):
        payload = {
            "last_period_date": "2021-06-01",
            "start_date": datetime.date(2021, 7, 1),
            "end_date": datetime.date(2021, 12, 1),
            "cycle_average": 25,
            "period_average": 5,
        }
        res = self.client.post(self.url, payload)
        self.assertEqual(res.data['total_created_cycles'], 5)
    
    
        

