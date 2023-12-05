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
        self.__time: datetime = datetime.datetime.now()

    def __str__(self) -> str:
        return f"Household: {self.__name}, Rooms: {self.__rooms}"
    
    @property
    def name(self):
        return self.__name
    
    @name.setter
    def name(self, new_name):
        self.__name = new_name

    @property
    def time(self):
        return self.__time.strftime('%Y-%m-%d %H:%M:%S')

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

    # def init_rooms_temp(self):
    #     self.__time = datetime.datetime.now()
    #     start_time = self.__time
    #
    #     while self.__time < (start_time + datetime.timedelta(days=2.0)):
    #         # Initialize an empty list to store room data for the current time
    #         room_data = []
    #         for room in self.__rooms.values():
    #             start_temp = random.randint(18, 23)
    #             room.sensor._temperature = round(float(start_temp), 2)
    #             room.set_temp(room.generate_temps(room.sensor._temperature, self.__time))
    #             # Append the room data to the list
    #             room_data.append({
    #                 'room': room.name,
    #                 'room_temperature': room.room_temperature,
    #                 'esired_temperature': room.desired_temperature,
    #                 'scheduled_temperature': room.scheduled_desired_temp,
    #                 'schedule_start': room.schedule_start,
    #                 'radiator_setting': room.radiator_setting
    #             })
    #         # Append the time and room data as a tuple to the temperatures list
    #         self.__temps.append((self.__time.strftime('%Y-%m-%d %H:%M:%S'), room_data))
    #         self.__time = tf.accelerate_time(self.__time, acceleration_factor=6000)
    #     print(self.__temps)

    def init_rooms_temp(self):
        for room in self.__rooms.values():
            if room.sensor_type == "Radiator":
                start_temp = random.randint(18, 23)
                room.sensor.temperature = round(float(start_temp), 2)
            elif room.sensor_type == "Boiler":
                start_temp = random.randint(30, 40)
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
