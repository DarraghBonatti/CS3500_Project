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

    def _add_room(self, name_or_room: str or Room, sensor_or_sensor_type: str or Sensor):
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
            self.__rooms[name_or_room._name] = name_or_room
            self.__sensors[sensor_or_sensor_type._name] = sensor_or_sensor_type
        else:
            raise TypeError("Invalid parameters for _add_room method")

    def _get_room(self, room_name: str) -> Room:
        return self.__rooms[room_name]
    
    # def _delete_room(self, room_name: str):
    #     del self.rooms[room_name]
    #     del self.sensors[room_name]

