class Temperature:
    def __init__(self, value: float, unit: str = 'Celsius'):
        if not isinstance(value, float):
            raise TypeError("Value must be a float")

        if not isinstance(unit, str):
            raise TypeError("Unit must be a string")

        self.__value = value
        self.__unit = unit
        self.__celsius = self.__value
        self.__fahrenheit = self.__value
  
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
            self.__celsius = self.__value
            self.__fahrenheit = self.__to_fahrenheit()
        elif self.__unit == 'Fahrenheit':
            self.__fahrenheit = self.__value
            self.__celsius = self.__to_celsius()
        else:
            raise ValueError("Unsupported unit")

    @property
    def celsius(self) -> float:
        return self.__celsius

    @celsius.setter
    def celsius(self, new_celsius: float) -> None:
        if not isinstance(new_celsius, float):
            raise ValueError("Value must be a float")
        self.__celsius = new_celsius
        if self.__unit == 'Celsius':
            self.__value = self.__celsius
            self.__fahrenheit = self.__to_fahrenheit()
        elif self.__unit == 'Fahrenheit':
            self.__fahrenheit = self.__value
            self.__celsius = self.__to_celsius()
        else:
            raise ValueError("Unsupported unit")
    
    @property
    def fahrenheit(self) -> float:
        return self.__fahrenheit

    @fahrenheit.setter
    def fahrenheit(self, new_fahrenheit: float) -> None:
        if not isinstance(new_fahrenheit, float):
            raise ValueError("Value must be a float")
        self.__fahrenheit = new_fahrenheit
        if self.__unit == 'Celsius':
            self.__celsius = self.__value
            self.__fahrenheit = self.__to_fahrenheit()
        elif self.__unit == 'Fahrenheit':
            self.__fahrenheit = self.__value
            self.__celsius = self.__to_celsius()
        else:
            raise ValueError("Unsupported unit")

    @property
    def unit(self) -> str:
        return self.__unit

    @unit.setter
    def unit(self, new_unit: str) -> None:
        if not isinstance(new_unit, str):
            raise TypeError("Unit must be a string")
        if new_unit not in {'Celsius', 'Fahrenheit'}:
            raise ValueError("Unsupported unit")
        self.__unit = new_unit
        if self.__unit == 'Celsius':
            self.celsius = self.__value
            self.fahrenheit = self.__to_fahrenheit()
        elif self.__unit == 'Fahrenheit':
            self.fahrenheit = self.__value
            self.celsius = self.__to_celsius()

   
class Sensor:
    def __init__(self, name: str, sensor_type: str = 'Radiator'):
        self.__name = name
        self.__type = sensor_type
        self.__temperature = Temperature(0.0, 'Celsius')

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