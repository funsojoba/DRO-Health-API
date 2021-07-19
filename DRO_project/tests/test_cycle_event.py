import datetime
from unittest import TestCase

from django.urls import reverse
from rest_framework.test import APIClient

from period_cycle_api.models import PeriodCylceModel


class TestCreateCycle(TestCase):
    client = APIClient()
    url = reverse('cycle-event')

    def test_event_cycle_with_no_date(self):
        res = self.client.get(self.url)
        self.assertEqual(res.data['error'], "Please input a valid date")
        self.assertEqual(res.status_code, 400)

    def test_event_cycle_with_date(self):
        date = "2021-08-14"
        res = self.client.get(self.url + '?date='+date)
        self.assertEqual(res.data[0]['date'], date)

    def test_date_returns_correct_calculation(self):
        cycle_date = PeriodCylceModel.objects.create(
            last_period_date=datetime.date(2021, 6, 1),
            cycle_average=25,
            period_average=5,
            start_date=datetime.date(2021, 7, 1),
            end_date=datetime.date(2021, 12, 1),
            total_created_cycle=5
        )
        cycle_date.save()
        date = "2021-08-14"
        res = self.client.get(self.url + '?date='+date)
        self.assertEqual(res.data[0]['event'], "mentral cycle starts")
        self.assertEqual(res.data[0]['date'], date)

    def test_valid_date_return_response(self):
        cycle_date = PeriodCylceModel.objects.create(
            last_period_date=datetime.date(2021, 6, 1),
            cycle_average=25,
            period_average=5,
            start_date=datetime.date(2021, 7, 1),
            end_date=datetime.date(2021, 12, 1),
            total_created_cycle=5
        )
        cycle_date.save()
        date = "2021-08-14"
        res = self.client.get(self.url + '?date='+date)
        self.assertEqual(res.status_code, 200)
