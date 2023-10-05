import csv
import json
import os


class LoadData:

    booking_list=[]
    id_list = []

    @staticmethod
    def load_users():
        reader = csv.DictReader(open(os.getcwd() + "/Data/admin_user.csv"))

        for line in reader:
            LoadData.id_list.append(line)

    @staticmethod
    def load_data_to_list():
        with open(os.getcwd()+"/data/booking_details.json",'r') as data_reader:
            booking_details=json.load(data_reader)
            for item in booking_details:
                LoadData.booking_list.append(item)

    @staticmethod
    def send_data_to_user():
        if len(LoadData.booking_list) < 1:
            LoadData.load_data_to_list()
        return LoadData.booking_list.pop()

    @staticmethod
    def get_User():
        if len(LoadData.id_list) < 1:
            LoadData.load_users()
        return LoadData.id_list.pop()

    @staticmethod
    def update_bookingData():
        with open(os.getcwd() + "/data/update_booking_data.json", 'r') as data_reader:
            update_booking_details = json.load(data_reader)
            return update_booking_details