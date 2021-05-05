import unittest
import os
import json
from app import create_app, db
import requests

class TestFlaskAPI(unittest.TestCase):

    def setUp(self):
        """Define test variables and initialize app."""
        self.app = create_app(os.getenv('APP_SETTINGS_MODULE'))
        self.client = self.app.test_client
        # self.bucketlist = {'name': 'Go to Borabora for vacation'}
        #
        # # binds the app to the current context
        # with self.app.app_context():
        #     # create all tables
        #     db.create_all()

    def test_daily_power(self):
        res = self.client().get('api/daily-power/2019-08-01/2019-08-04')
        self.assertEqual(res.status_code, 200)

    def test_power_series(self):
        res = self.client().get('api/power-timeseries/2019-08-01/2019-08-04')
        self.assertEqual(res.status_code, 200)

    def test_power_month(self):
        res = self.client().get('api/actual-energy-month')
        self.assertEqual(res.status_code, 200)

    def test_reactive_month(self):

        res = self.client().get('api/actual-reactive-month')
        self.assertEqual(res.status_code, 200)

    def test_get_token(self):
        "Test get token"

        headers = {'content-type': 'application/json'}
        response = self.client().post('http://127.0.0.1:5000/auth', json={
            'username': 'user1', 'password': 'abcxyz'
        })
        self.assertEqual(response.status_code, 200)



    def tearDown(self):
        """teardown all initialized variables."""
        with self.app.app_context():
            # drop all tables
            db.session.remove()
            db.drop_all()