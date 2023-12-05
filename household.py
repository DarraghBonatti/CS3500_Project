"""
File containing each class for the house heating system

This file is being constructed using the Sample-house_test file as a basis 
for test driven development


"""
from sensor import Sensor 
from room import Room 
import datetime
import random
import time_file as tf
import time


class Household:
    def __init__(self, name):
        self.__name: str = name
        self.__rooms: {str: Room} = {}
        self.__sensors: {str: Sensor} = {}
        # Set the time to 9:00 AM today
        today = datetime.datetime.now().date()
        desired_time: datetime = datetime.datetime(today.year, today.month, today.day, 9, 0)
        self.__time: datetime = desired_time

    def __str__(self) -> str:
        return f"Household: {self.__name}, Rooms: {self.__rooms}"
    
    @property
    def name(self):
        return self.__name
    
    @name.setter
    def name(self, new_name):
        self.__name = new_name

    @property
    def time_string(self):
        return self.__time.strftime('%Y-%m-%d %H:%M:%S')
    
    @property
    def time(self):
        return self.__time

    @time.setter
    def time(self, new_time: datetime):
        self.__time = new_time

    @property
    def temps(self):
        return self.__temps

    @property
    def rooms(self):
        return self.__rooms

    def add_room(self, name: str, sensor_type: str):
        """
        Function adds a room to the household
        Room is found in the rooms dictionary by its name
        Equally, this room has a sensor which is found in the sensors dictionary 
        by the room name
        """
        if isinstance(name, str) and isinstance(sensor_type, str):
            # Handle the case where name and sensor_type are provided
            self.__rooms[name] = Room(name, sensor_type)
            self.__sensors[name] = self.__rooms[name].sensor
        else:
            raise TypeError("Invalid parameters for _add_room method")
    
    def get_room(self, room_name: str) -> Room:
        return self.__rooms[room_name]

    

    def init_rooms_temp(self):
        for room in self.__rooms.values():
            if room.sensor_type == "Radiator":
                start_temp = random.randint(15, 18)
                room.sensor.temperature = round(float(start_temp), 2)
            elif room.sensor_type == "Boiler":
                start_temp = random.randint(40, 45)
                room.sensor.temperature = round(float(start_temp), 2)

    def update_rooms_temp(self):
        for room in self.__rooms.values():
            if room.sensor_type == "Radiator":
                room.set_temp(room.generate_temps(room.sensor.temperature, self.__time))
            elif room.sensor_type == "Boiler":
                room.set_temp(room.generate_temps(room.sensor.temperature, self.__time))
        self.__time = tf.accelerate_time(self.__time, acceleration_factor=900)

    def delete_room(self, room_name: str):
        if room_name not in self.__rooms.keys():
            raise ValueError("Room does not exist")
        del self.__sensors[room_name]
        del self.__rooms[room_name]
