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
        self.__sensors: {str:Sensor} = {}
        self.__time: datetime = datetime.datetime.now()
        self._temps = []

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
    def rooms(self):
        return self.__rooms

    def add_room(self, name_or_room: str or Room, sensor_or_sensor_type: str or Sensor):
        """
        Function adds a room to the household
        Room is found in the rooms dictionary by its name
        Equally, this room has a sensor which is found in the sensors dictionary 
        by the room name
        """
        if isinstance(name_or_room, str) and isinstance(sensor_or_sensor_type, str):
            # Handle the case where name and sensor_type are provided
            self.__rooms[name_or_room] = Room(name_or_room, sensor_or_sensor_type)
            self.__sensors[name_or_room] = self.__rooms[name_or_room].sensor
        elif isinstance(name_or_room, Room) and isinstance(sensor_or_sensor_type, Sensor):
            # Handle the case where room and sensor are provided
            self.__rooms[name_or_room.name] = name_or_room
            self.__sensors[sensor_or_sensor_type.name] = sensor_or_sensor_type
        else:
            raise TypeError("Invalid parameters for _add_room method")
    
    def get_room(self, room_name: str) -> Room:
        return self.__rooms[room_name]
    
    # def init_rooms_temp(self):
    #     """
    #     Function initializes the temperature of each room in the household
    #     """
        
    #     self.__time = datetime.datetime.now()
    #     start_time = self.__time
    #     for room in self.__rooms.values():
    #         #  random temps between 18 and 23 celsius
    #         start_temp = random.randint(18, 23)
    #         room.sensor._temperature = round(float(start_temp), 2)

    #         while self.__time < (start_time + datetime.timedelta(days=2)):
    #             room.set_temp(room.generate_temps(room.sensor._temperature, self.__time))
    #             print(f"Room: {room._name} \nCurrent Time: {self.__time.strftime('%Y-%m-%d %H:%M:%S')} \nRoom temperature: {room.room_temperature:.2f} \nDesired Temperature: {room.desired_temperature} \nScheduled Temperature: {room.scheduled_desired_temp} For {room.schedule_start}\nRadiator: {room.radiator_setting}\n")
    #             self.__time = tf.accelerate_time(self.__time, acceleration_factor=6000)
    #             time.sleep(2)

    def init_rooms_temp(self):
        self.__time = datetime.datetime.now()
        start_time = self.__time
        

        while self.__time < (start_time + datetime.timedelta(days=2)):
            for room in self.__rooms.values():
                start_temp = random.randint(18, 23)
                room.sensor._temperature = round(float(start_temp), 2)
                room.set_temp(room.generate_temps(room.sensor._temperature, self.__time))
                # Store the temperatures in the list
                self._temps.append((
                    self.__time.strftime('%Y-%m-%d %H:%M:%S'),
                    {
                        'room': room.name,
                        'room_temperature': room.room_temperature,
                        'desired_temperature': room.desired_temperature,
                        'scheduled_temperature': room.scheduled_desired_temp,
                        'schedule_start': room.schedule_start,
                        'radiator_setting': room.radiator_setting
                    }
                ))
            self.__time = tf.accelerate_time(self.__time, acceleration_factor=6000)
<<<<<<< HEAD

=======
        print(self._temps)
>>>>>>> 0d3eff391e7f694f5b5dec4e798caf672c9a2896
    # def init_boiler_temp(self):
    #     """
    #     Function initializes the temperature of the boiler
    #     """
    #     self.__time = datetime.datetime.now()
    #     start_time = self.__time
    #     boiler_temp = random.randint(40, 50)
    #     while self.__time < (start_time + datetime.timedelta(days=2)):
    #         print(f"Boiler temperature: {boiler_temp}")
    #         self.__time = tf.accelerate_time(self.__time, acceleration_factor=6000)

    def delete_room(self, room_name: str):
        if room_name not in self.__rooms.keys():
            raise ValueError("Room does not exist")
        del self.__sensors[room_name]
        del self.__rooms[room_name]