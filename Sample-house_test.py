import unittest
from household import (Household, Sensor, Room)

class TestHousehold(unittest.TestCase):
    def setUp(self):
        self.murphy_household = Household('Murphys House')
        self.living_room = Room('Living Room')
        self.living_room_sensor = Sensor('Living Room', 'Radiator')

    def test_add_room(self):
        self.murphy_household._add_room('Bedroom', 'Radiator')
        self.assertIn('Bedroom', self.murphy_household._rooms)

        self.murphy_household._add_room(self.living_room, self.living_room_sensor)
        self.assertIn('Living Room', self.murphy_household._rooms)

    def test_sensor_room(self):
        self.assertEqual(self.living_room_sensor._name, self.living_room._name)

    def test_sensor_type(self):
        self.assertEqual(self.living_room_sensor._type, 'Radiator')

if __name__ == '__main__':
    unittest.main()