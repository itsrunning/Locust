import datetime
import json


import pytz
from locust import events
import socket
from influxdb import InfluxDBClient


class InfluxHandlerEvents:

    hostname = socket.gethostname()
    data_base_name = "locustdb"
    table_name = "REST_Table"


    influxDbClient = InfluxDBClient(host='localhost',
                                    port=8086,
                                    database=data_base_name)

    @staticmethod
    def init_influx_client():
        InfluxHandlerEvents.influxDbClient.drop_database(InfluxHandlerEvents.data_base_name)
        InfluxHandlerEvents.influxDbClient.create_database(InfluxHandlerEvents.data_base_name)
        InfluxHandlerEvents.influxDbClient.switch_database(InfluxHandlerEvents.data_base_name)



    @staticmethod
    @events.request.add_listener
    def my_request_handler(request_type, name, response_time, response_length, response,
                           context, exception, start_time, url, **kwargs):
        if exception:
            print("fail")
            # InfluxHandlerEvents.influxDbClient.write_points(InfluxHandlerEvents.hostname, request_type, name, response_time,
            #                                          response_length,  exception, "FAIL")
            InfluxHandlerEvents.influxDbClient.write("FAIL")
        else:
            print("pass")
            success_temp = \
                '[{"measurement": "%s",\
                "tags": {\
                    "hostname": "%s",\
                    "requestName": "%s",\
                    "requestType": "%s",\
                    "status": "%s"\
                }, \
                "fields": {\
                    "responseTime": "%i",\
                    "responseLength": "%i"\
                }\
             }]'

            json_string = success_temp % (
                InfluxHandlerEvents.table_name, InfluxHandlerEvents.hostname, name, request_type,
                "PASS", response_time, response_length)
            InfluxHandlerEvents.influxDbClient.write_points(json.loads(json_string))
            # InfluxHandlerEvents.write_api.write(InfluxHandlerEvents.bucket,InfluxHandlerEvents.org,json.loads(json_string))
