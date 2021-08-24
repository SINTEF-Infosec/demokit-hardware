from sense_hat import SenseHat

sense = SenseHat()
sense.clear()


def read_temperature():
    return sense.get_temperature()


def read_humidity():
    return sense.get_humidity()
