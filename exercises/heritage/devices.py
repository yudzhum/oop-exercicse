class Device:
    __slots__ = [ "_name", "_location", "_status"]

    def __init__(self, name, location):
        self._name = name
        self._location = location
        self._status = 'ON'

    @property
    def name(self):
        return self._name
    
    @property
    def location(self):
        return self._location
    
    @location.setter
    def location(self, new_location):
        self._location = new_location

    @property
    def status(self):
        return self._status
    
    @status.setter
    def status(self, new_status):
        self._status = new_status

    def turn_on(self):
        self._status = 'ON'

    def turn_off(self):
        self._status = 'OFF'


class Light(Device):
    __slots__ = ["_brightness", "_color"]

    def __init__(self, name, location, brightness, color):
        self._name = name
        self._location = location
        self._brightness = brightness
        self._color = color

    @property
    def brightness(self):
        return self._brightness
    
    @brightness.setter
    def brightness(self, new_brightness):
        self._brightness = new_brightness

    @property
    def color(self):
        return self._color
    

class Thermostat(Device):
    __slots__ = ["_current_temperature", "_target_temperature"]

    def __init__(self, name, location, current_temperature, target_temperature):
        self._name = name
        self._location = location
        self._current_temperature = current_temperature
        self._target_temperature = target_temperature

    @property
    def current_temperature(self):
        return self._current_temperature
    
    @current_temperature.setter
    def current_temperature(self, cur_temp):
        self._current_temperature = cur_temp

    @property
    def target_temperature(self):
        return self._target_temperature
    
    @target_temperature.setter
    def target_temperature(self, target_temp):
        self._target_temperature = target_temp


class SmartTV(Device):
    __slots__ = [ "_channel"]

    def __init__(self, name, location, channel):
        self._name = name
        self._location = location
        self._channel = channel

    @property
    def channel(self):
        return self._channel
    
    @channel.setter
    def channel(self, new_channel):
        self._channel = new_channel


device1 = Device('Устройство 1', 'Гостиная')
assert device1.name == 'Устройство 1'
assert device1._name == 'Устройство 1'
assert device1.location == 'Гостиная'
assert device1._location == 'Гостиная'
assert device1.status == 'ON'
assert device1._status == 'ON'

device1.turn_off()
assert device1.status == 'OFF'
device1.location = 'Кухня'
assert device1.location == 'Кухня'
assert device1._location == 'Кухня'
device1.turn_on()
assert device1.status == 'ON'

thermostat_1 = Thermostat('Термометр', 'Балкон', 10, 15)
thermostat_1.name == 'Термометр'
thermostat_1.location == 'Балкон'
thermostat_1.status == 'ON'
thermostat_1.current_temperature == 10
thermostat_1.target_temperature == 15