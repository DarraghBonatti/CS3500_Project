from sensor import Sensor

class Room: 
    """
    TODO: Consider whether rooms can have multiple sensors
    """
    def __init__(self, name, sensor_type: str = 'Radiator'):
        if not isinstance(name, str):
            raise TypeError("Name must be a string")
        if not isinstance(sensor_type, str):
            raise TypeError("Sensor type must be a string")
        
        self.__name = name
        self.__sensor = Sensor(name, sensor_type)

    def __str__(self) -> str:
        return f"Room: {self.__name}, Sensor : {self.__sensor}"
    
    @property
    def sensor_name(self):
        return self.__sensor.__name
    
    @property
    def sensor(self):
        return self.__sensor
    
    @property
    def room_temperature(self):
        return self.__sensor.__temperature.value
    
    # TODO: if we have multiple sensors, we need to be able to set them, and add + remove etc.
    #   How strongly do to couple the sensor to the room?
    # @_sensor.setter
    # def sensor(self, new_sensor_name):
    #     self.__sensor = new_sensor
    
    @property
    def _name(self):
        return self.__name
    @_name.setter
    def _name(self, new_name):
        if not isinstance(new_name, str):
            raise TypeError("Name must be a string")
        self.__name = new_name