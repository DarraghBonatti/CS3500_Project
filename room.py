from sensor import Sensor
import time_file as tf
import datetime

class Room: 
    def __init__(self, name, sensor_type: str = 'Radiator'):
        if not isinstance(name, str):
            raise TypeError("Name must be a string")
        if not isinstance(sensor_type, str):
            raise TypeError("Sensor type must be a string")
        
        self.__name = name
        self.__sensor = Sensor(name, sensor_type)
        self.__desired_temperature = 0.0

    def __str__(self) -> str:
        return f"Room: {self.__name}, Sensor : {self.__sensor}"
    
    @property
    def sensor_name(self):
        return self.__sensor._name
    
    @property
    def sensor(self):
        return self.__sensor
    
    @property
    def room_temperature(self):
        return self.__sensor._temperature
    
    @property
    def desired_temperature(self):
        return self.__desired_temperature
    @desired_temperature.setter
    def desired_temperature(self, new_temp):
        if not isinstance(new_temp, float):
            raise TypeError("Desired temperature must be a float")
        self.__desired_temperature = new_temp
    
    @property
    def _name(self):
        return self.__name
    @_name.setter
    def _name(self, new_name):
        if not isinstance(new_name, str):
            raise TypeError("Name must be a string")
        self.__name = new_name

    # implement generate_temps method
    def _generate_temps(self, current_time, current_temp):
        #  implement time multiplier on sine curve
        new_temp = current_temp * tf.time_multiplier(current_time) 
        # whereby time_multiplier is a function that returns a multiplier based on the time of day
        #   and range of time_multiplier is 0.85 to 1.0
        return new_temp
    

    def init_generate_temps(self, start_time: datetime, start_temp: float):
        # for 5 accelerated days
        #   set room temp to generate_temps(current_time, current_temp)
        current_time = start_time
        current_temp = start_temp

        while current_time < (start_time + datetime.timedelta(days=5)):
            current_temp = self._generate_temps(current_time, current_temp)
            print(f"Current Time: {current_time}, Room temperature: {current_temp}")
            current_time = tf.accelerate_time(current_time, acceleration_factor=10000)  # Assuming 300x acceleration

    def set_temp(self, new_temp):
        if self.desired_temperature != new_temp:
            delta_temp = self.desired_temperature - new_temp
            # self.turn_radiator_on(delta_temp)
