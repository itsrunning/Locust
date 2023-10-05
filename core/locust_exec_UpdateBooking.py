from locust import events
import logging

from scenarios.update_booking import UpdateBooking
from users.user_with_authentication import UserWithAuthentication
# from common.InfluxHandlers import InfluxHandlerEvents



class TokenizedUsers(UserWithAuthentication):
    tasks = [UpdateBooking]


# @events.test_start.add_listener
# def on_start_influxdb(**kwargs):
#     InfluxHandlerEvents.init_influx_client()

@events.quitting.add_listener
def _(environment, **kw):
    if environment.stats.total.fail_ratio > 0.01:
        logging.error("Test failed due to failure ratio > 1%")
        environment.process_exit_code = 1
    elif environment.stats.total.avg_response_time > 200:
        logging.error("Test failed due to average response time ratio > 200 ms")
        environment.process_exit_code = 1
    elif environment.stats.total.get_response_time_percentile(0.95) > 800:
        logging.error("Test failed due to 95th percentile response time > 800 ms")
        environment.process_exit_code = 1
    else:
        environment.process_exit_code = 0
