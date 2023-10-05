from locust import HttpUser,wait_time,between
import csv
import os
from data.add_data import LoadData

class UserWithAuthentication(HttpUser):

    wait_time=between(1,2)
    abstract = True

    def __init__(self,parent):
        super(UserWithAuthentication, self).__init__(parent)
        self.token_id = ''
        self.user_obj = {}

    def on_start(self):
        self.booking_data = LoadData.send_data_to_user()
        self.user_obj = LoadData.get_User()

        self.userid = self.user_obj['username']
        self.pwd= self.user_obj['password']

        user_creds = {"username": self.userid, "password": self.pwd}
        response = self.client.post('/auth', user_creds )
        tokens = response.json()
        self.token_id = tokens['token']

    def give_token(self):
        return self.token_id

    def send_data_to_taskset(self):
        return self.booking_data





