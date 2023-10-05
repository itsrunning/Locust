from locust import HttpUser, between

from data.add_data import LoadData


class UserWithoutAuthentication(HttpUser):
    wait_time = between(1,2)
    abstract = True

    def on_start(self):
        self.booking_data=LoadData.send_data_to_user()

    def send_data_to_taskset(self):
        return self.booking_data
