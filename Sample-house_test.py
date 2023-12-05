import unittest
from household import (Household, Sensor, Room)
from datetime import datetime, time


class TestHousehold(unittest.TestCase):
    """
    Testing suit for the Household class and overall system functionality, excluding the GUI.
    """
    def test_add_room(self):
        household = Household("Household")
        for room in range(1, 6):
            household.add_room(f"Room {room}", "Radiator")
            room_instance = household.get_room(f"Room {room}")

            self.assertEqual(room_instance.name, f"Room {room}")
            self.assertEqual(room_instance.sensor.type, "Radiator")

            print(room_instance.sensor)
            print(room_instance.sensor_name)
            print(room_instance.room_temperature)
            print(room_instance.desired_temperature)

    def test_generate_temps(self):
        household = Household("Household")
        household.add_room("Test Room", "Radiator")
        household.add_room("Test Boiler", "Boiler")

        today_date = datetime.now().date()
        desired_time = time(22, 0)
        custom_datetime = datetime.combine(today_date, desired_time)
  
        desired_temp = 25.0
        household.get_room("Test Room").schedule_desired_temp(desired_temp, custom_datetime)
        print(f"Scheduled desired temp {household.get_room('Test Room').scheduled_desired_temp}, Scheduled Time: {household.get_room('Test Room').schedule_start}")

        desired_temp_boiler = 60.0
        household.get_room("Test Boiler").schedule_desired_temp(desired_temp_boiler, custom_datetime)

        household.init_rooms_temp()
        for i in range(60):
            household.update_rooms_temp()
            print(f"Time: {household.time_string}, \n"
                  f"Room Temperature: {household.get_room('Test Room').room_temperature}, \n"
                  f"Desired temp: {household.get_room('Test Room').desired_temperature}, \n"
                  f"Radiator Setting: {household.get_room('Test Room').radiator_setting}, \n"
                  f"\nBoiler Temperature: {household.get_room('Test Boiler').room_temperature}, \n"
                  f"Desired temp: {household.get_room('Test Boiler').desired_temperature}, \n"
                  f"Radiator Setting: {household.get_room('Test Boiler').radiator_setting}, \n")


if __name__ == '__main__':
    unittest.main()
