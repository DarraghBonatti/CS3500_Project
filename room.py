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
        self.__desired_temperature = 25.0
        self.__radiator_setting = "Off"

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
    
    @room_temperature.setter
    def room_temperature(self, new_temp):
        self.__sensor._temperature = new_temp
    
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

    @property
    def radiator_setting(self):
        return self.__radiator_setting
    
    # implement generate_temps method
    def generate_temps(self, current_time, current_temp):

        base_rate = 0.05

        rate = base_rate * tf.time_multiplier(current_time, 0.99, 1.01)

        # Add the effect of the radiator
        if self.__radiator_setting == "Low":
            rate += 0.125  # Low setting boosts temperature at a lower rate
        elif self.__radiator_setting == "High":
            rate += 0.35  # High setting boosts temperature at a higher rate

        if current_time.hour >= 6 and current_time.hour < 18:
            # daytime
            new_temp = current_temp + rate
        else:
            # nighttime
            new_temp = current_temp - rate

        rounded_temp = round(new_temp, 2)
        return rounded_temp
    

    def set_temp(self, new_temp: float):
        if self.__desired_temperature != new_temp:
            print(f"New temp = {new_temp}")
            delta_temp = abs(self.__desired_temperature - new_temp)

            if delta_temp >= 1:
                self.turn_radiator_on(delta_temp)
            elif abs(self.__sensor._temperature - self.__desired_temperature) < 1:
                self.__radiator_setting = "Off"
                print(f"Radiator is now set to {self.__radiator_setting}.")

        self.__sensor._temperature = round(new_temp, 2)


    def turn_radiator_on(self, delta_temp):
        if delta_temp < 4:
            self.__radiator_setting = "Low"
        else:
            self.__radiator_setting = "High"
        print(f"Radiator is now set to {self.__radiator_setting}.")
