class Temperature:
    def __init__(self, value: float, unit: str = 'Celsius'):
        if not isinstance(value, float):
            raise TypeError("Value must be a float")

        if not isinstance(unit, str):
            raise TypeError("Unit must be a string")

        self.__value = value
        self.__unit = unit

        if self.__unit == 'Celsius':
            self._celsius = self.__value
            self._fahrenheit = self.__to_fahrenheit()
        elif self.__unit == 'Fahrenheit':
            self._fahrenheit = self.__value
            self._celsius = self.__to_celsius()
        else:
            raise ValueError("Unsupported unit")
  
    def __str__(self) -> str:
        return f"Temperature is {self.__value} degrees {self.__unit})"

    def __to_fahrenheit(self) -> float:
        return (self.__value * 9/5) + 32

    def __to_celsius(self) -> float:
        return (self.__value - 32) * (5/9)
    
    @property
    def value(self) -> float:
        return self.__value
    @value.setter
    def value(self, new_value: float) -> None:
        if not isinstance(new_value, float):
            raise ValueError("Value must be a float")

        self.__value = new_value

        if self.__unit == 'Celsius':
            self._celsius = self.__value
            self._fahrenheit = self.__to_fahrenheit()
        elif self.__unit == 'Fahrenheit':
            self._fahrenheit = self.__value
            self._celsius = self.__to_celsius()
        else:
            raise ValueError("Unsupported unit")

        
    @property
    def _celsius(self) -> float:
        return self._celsius
    @property
    def _fahrenheit(self) -> float:
        return self._fahrenheit
    
    @property
    def _unit(self) -> str:
        return self.__unit
    @_unit.setter
    def _unit(self, new_unit: str) -> None:
        if not isinstance(new_unit, str):
            raise TypeError("Unit must be a string")

        if new_unit not in {'Celsius', 'Fahrenheit'}:
            raise ValueError("Unsupported unit")

        self.__unit = new_unit

        if self.__unit == 'Celsius':
            self._celsius = self.__value
            self._fahrenheit = self.__to_fahrenheit()
        elif self.__unit == 'Fahrenheit':
            self._fahrenheit = self.__value
            self._celsius = self.__to_celsius()

        


class Sensor:
    def __init__(self, name: str, sensor_type: str = 'Radiator'):
        self.__name = name
        self.__type = sensor_type
        self.__temperature = Temperature(0.0, 'Celsius')

    def __str__(self) -> str:
        return f"Sensor({self.__name}, {self.__type}, {self.__temperature.value})"

    @property
    def _temperature(self):
        return self.__temperature.value
    
    @_temperature.setter
    def _temperature(self, new_temp):
        # Don't need to check if it's a float, as the Temperature class will do that
        self.__temperature.value = new_temp

    @property
    def _temperature_unit(self):
        return self.__temperature.unit
    @_temperature_unit.setter
    def _temperature_unit(self, new_unit):
         # Don't need to check if it's a string, as the Temperature class will do that
        self.__temperature.unit = new_unit

    @property
    def _type(self):
        return self.__type
    
    @property
    def _name(self):
        return self.__name