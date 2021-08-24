from sense_hat import SenseHat

sense = SenseHat()
sense.clear()


def read_temperature():
    return sense.get_temperature()


def read_humidity():
    return sense.get_humidity()


def light_with_color(r, g, b):
    sense.clear((r, g, b))


def light_on():
    light_with_color(255, 255, 255)


def light_off():
    sense.clear()
