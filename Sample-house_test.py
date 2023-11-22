import project.py

murphy_household = new Household('Murphys House')

living_room_sensor = new Sensor('Living Room', 'Radiator')
murphy_household.add_room('Living Room', living_room_sensor)

laura_bedroom_sensor = new Sensor('Living Room', 'Radiator')

murphy_household.add_room('Lauras Bedroom', laura_bedroom_sensor)

kitchen_sensor = new Sensor('Kitchen', 'Radiator')
murphy_household.add_room('Kitchen', kitchen_sensor)



# living_room_sensor.setTemp()