
from locust import SequentialTaskSet, task


class GetBooking(SequentialTaskSet):

    @task
    def get_booking(self):
        with self.client.get("/booking/4746", catch_response=True) as resp:
            if resp.status_code == 200:
                resp.success()
            else:
                resp.failure(resp.text)
