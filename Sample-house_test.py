import unittest
from household import (Household, Sensor, Room)
from datetime import datetime, time

class TestHousehold(unittest.TestCase):
    # def setUp(self):
    #     self.murphy_household = Household('Murphys House')
    #     self.living_room = Room('Living Room')
    #     self.living_room_sensor = Sensor('Living Room', 'Radiator')

    # def test_add_room(self):
    #     self.murphy_household._add_room('Bedroom', 'Radiator')
    #     self.assertIn('Bedroom', self.murphy_household._rooms)

    #     self.murphy_household._add_room(self.living_room, self.living_room_sensor)
    #     self.assertIn('Living Room', self.murphy_household._rooms)

    # def test_sensor_room(self):
    #     self.assertEqual(self.living_room_sensor._name, self.living_room._name)

    # def test_sensor_type(self):
    #     self.assertEqual(self.living_room_sensor._type, 'Radiator')


    # def test_add_room(self):
    #     household = Household("Household")
    #     for room in range(1, 6):
    #         household._add_room(f"Room {room}", "Radiator")
    #         room_instance = household._get_room(f"Room {room}")

    #         self.assertEqual(room_instance._name, f"Room {room}")
    #         self.assertEqual(room_instance.sensor._type, "Radiator")

    #         # Add assertions for other properties or methods as needed
    #         print(room_instance.sensor)
    #         print(room_instance.sensor_name)
    #         print(room_instance.room_temperature)
    #         print(room_instance.desired_temperature)

    def test_generate_temps(self):
        household = Household("Household")
        household._add_room("Test Room", "Radiator")

        # Replace these with your desired start time and temperature

        today_date = datetime.now().date()
        desired_time = time(22, 0)
        custom_datetime = datetime.combine(today_date, desired_time)
  
        desired_temp = 30.0
        household._get_room("Test Room").schedule_desired_temp(desired_temp, custom_datetime)
        print(f"Scheduled desired temp {household._get_room('Test Room').scheduled_desired_temp}, Scheduled Time: {household._get_room('Test Room').schedule_start}")

        household.init_rooms_temp()


        # Add assertions to check if temperatures are generated correctly


if __name__ == '__main__':
    unittest.main()
