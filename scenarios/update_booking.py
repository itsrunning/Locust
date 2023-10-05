

from locust import TaskSet, task, SequentialTaskSet

from data.add_data import LoadData


class UpdateBooking(SequentialTaskSet):


    @task
    def post_booking_orders(self):
        booking_data = self.user.send_data_to_taskset()
        auth_headers = {"Content-Type": "application/json", "Accept": "application/json"}
        response = self.client.post("/booking", headers=auth_headers, json=booking_data)
        resp = response.json()
        self.booking_order = resp['bookingid']

    @task
    def update_booking_order(self):
        #     # token_id = ''
        token_id = self.user.give_token()
        auth_headers = {"Content-Type": "application/json", "Accept": "application/json",
                        "Cookie": "token={}".format(token_id)}
        with self.client.put('/booking/{}'.format(self.booking_order), headers=auth_headers, json=
        LoadData.update_bookingData(),catch_response=True) as resp:
            if resp.status_code == 200:
                resp.success()
            else:
                resp.failure(resp.text)

