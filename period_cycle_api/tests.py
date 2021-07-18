from django.urls import reverse
from rest_framework.test import APIClient


class TestCreateCycle(APIClient):
    def setup(self):
        self.url = reverse('create-cycles')
        self.empty_payload = {
            "last_period_date": "",
            "start_date": "",
            "end_date": "",
            "cycle_average": "",
            "period_average": ""
        }
        self.valid_payload = {
            "last_period_date": "2021-06-01",
            "start_date": "2021-07-01",
            "end_date": "2021-12-01",
            "cycle_average": 25,
            "period_average": 5,
        }
        self.invalid_payload = {
            "last_period_date": "2021-06-01",
            "start_date": "2021-12-01",
            "end_date": "2021-07-01",
            "cycle_average": 25,
            "period_average": 5,
        }

    def test_users_cannot_post_empty_data(self):
        res = self.client.post(self.url, self.empty_payload)
        self.assertEqual(res.status_code, 400)

    def test_users_can_post_valid_data(self):
        res = self.client.post(self.url, self.valid_payload)
        self.assertEqual(res.status_code, 200)

    def test_circle_calculation_is_correct(self):
        res = self.client.post(self.url, self.valid_payload)
        self.asserEqueal(res.data.get('total_created_cycle'), 5)
