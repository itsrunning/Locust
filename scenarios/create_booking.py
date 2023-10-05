from locust import TaskSet, SequentialTaskSet, task


class CreateBooking(SequentialTaskSet):

    @task
    def post_booking_order(self):
        booking_data=self.user.send_data_to_taskset()
        auth_headers = {"Content-Type": "application/json", "Accept": "application/json"}
        response=self.client.post("/booking",headers=auth_headers,json=booking_data)
        resp=response.json()
        self.booking_order=resp['bookingid']
        if self.booking_order == '':
            response.failure(response.text)

    @task
    def get_booking_order_details(self):
        with self.client.get("/booking/{}".format(self.booking_order),catch_response=True) as resp:
            if resp.status_code == 200:
                resp.success()
            else:
                resp.failure(resp.text)
        print(resp.text)
