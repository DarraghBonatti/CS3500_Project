class Temperature:
    def __init__(self, value: float):
        if not isinstance(value, float):
            raise TypeError("Value must be a float")

        self.__value = value
        self.__unit = "Celsius"
  
    def __str__(self) -> str:
        return f"Temperature is {self.__value} degrees {self.__unit})"

    @property
    def value(self) -> float:
        return self.__value

    @value.setter
    def value(self, new_value: float) -> None:
        if not isinstance(new_value, float):
            raise ValueError("Value must be a float")
        self.__value = new_value

    @property
    def unit(self) -> str:
        return self.__unit

   
class Sensor:
    def __init__(self, name: str, sensor_type: str = 'Radiator'):
        """
        Object to represent a sensor.
        Stores the sensor's name, type, and temperature.
        """
        self.__name = name
        self.__type = sensor_type
        self.__temperature = Temperature(0.0)

    def __str__(self) -> str:
        return f"Sensor({self.__name}, {self.__type}, {self.__temperature.value})"

    @property
    def temperature(self):
        return self.__temperature.value

    @temperature.setter
    def temperature(self, new_temp):
        self.__temperature.value = new_temp

    @property
    def temperature_unit(self):
        return self.__temperature.unit

    @temperature_unit.setter
    def temperature_unit(self, new_unit):
        self.__temperature.unit = new_unit

    @property
    def type(self):
        return self.__type
    
    @property
    def name(self):
        return self.__name
