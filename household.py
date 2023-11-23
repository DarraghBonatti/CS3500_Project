"""
File containing each class for the house heating system

This file is being constructed using the Sample-house_test file as a basis 
for test driven development


"""
from sensor import Sensor 
from room import Room 


class Household:
    def __init__(self, name):
        self.__name: str = name
        self.__rooms: {str: Room} = {}
        self.__sensors: {str:Sensor} = {}

    def __str__(self) -> str:
        return f"Household: {self.__name}, Rooms: {self.__rooms}"
    
    @property
    def _name(self):
        return self.__name
    
    @_name.setter
    def _name(self, new_name):
        self.__name = new_name

    @property
    def _rooms(self):
        return self.__rooms

    def _add_room(self, name, sensor_type):
        """
        Function adds a room to the household
        Room is found in the rooms dictionary by it's name
        Equally, this room has a sensor which is found in the sensors dictionary 
        by the room name
        """
        self.__rooms[name] = Room(name, sensor_type)
        self.__sensors[name] = self.rooms[name].sensor

    def _get_room(self, room_name: str):
        return self.rooms[room_name]
    
    # def _delete_room(self, room_name: str):
    #     del self.rooms[room_name]
    #     del self.sensors[room_name]

