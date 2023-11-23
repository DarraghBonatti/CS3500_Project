import unittest
from household import (Household, Sensor, Room)

class TestHousehold(unittest.TestCase):
    def setUp(self):
        self.murphy_household = Household('Murphys House')
        self.living_room = Room('Living Room')
        self.living_room_sensor = Sensor(self.living_room, 'Radiator')

    def test_add_room(self):
        self.murphy_household.add_room('Living Room', self.living_room_sensor)
        self.assertIn('Living Room', self.murphy_household.rooms)

    def test_sensor_room(self):
        self.assertEqual(self.living_room_sensor.room, self.living_room)

    def test_sensor_type(self):
        self.assertEqual(self.living_room_sensor.type, 'Radiator')

if __name__ == '__main__':
    unittest.main()