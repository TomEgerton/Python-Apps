# List of colours to be used within the program
import colourise as col
import random


def ColourDic():
    """
    Creates a dictionary of randomised colours
    (I've kept my original list at the bottom for testing purposes)
    :return:
    A dictionary of randomly generated colours
    """
    colour = [
        {"r": random.randint(0, 255), "g": random.randint(0, 255), "b": random.randint(0, 255)},
        {"r": random.randint(0, 255), "g": random.randint(0, 255), "b": random.randint(0, 255)},
        {"r": random.randint(0, 255), "g": random.randint(0, 255), "b": random.randint(0, 255)},
        {"r": random.randint(0, 255), "g": random.randint(0, 255), "b": random.randint(0, 255)},
        {"r": random.randint(0, 255), "g": random.randint(0, 255), "b": random.randint(0, 255)},
        {"r": random.randint(0, 255), "g": random.randint(0, 255), "b": random.randint(0, 255)},
        {"r": random.randint(0, 255), "g": random.randint(0, 255), "b": random.randint(0, 255)},
        {"r": random.randint(0, 255), "g": random.randint(0, 255), "b": random.randint(0, 255)},
        {"r": random.randint(0, 255), "g": random.randint(0, 255), "b": random.randint(0, 255)},
        {"r": random.randint(0, 255), "g": random.randint(0, 255), "b": random.randint(0, 255)},
        {"r": random.randint(0, 255), "g": random.randint(0, 255), "b": random.randint(0, 255)},
        {"r": random.randint(0, 255), "g": random.randint(0, 255), "b": random.randint(0, 255)},
        {"r": random.randint(0, 255), "g": random.randint(0, 255), "b": random.randint(0, 255)},
        {"r": random.randint(0, 255), "g": random.randint(0, 255), "b": random.randint(0, 255)},
        {"r": random.randint(0, 255), "g": random.randint(0, 255), "b": random.randint(0, 255)},
        {"r": random.randint(0, 255), "g": random.randint(0, 255), "b": random.randint(0, 255)},
        {"r": random.randint(0, 255), "g": random.randint(0, 255), "b": random.randint(0, 255)},
        {"r": random.randint(0, 255), "g": random.randint(0, 255), "b": random.randint(0, 255)},
        {"r": random.randint(0, 255), "g": random.randint(0, 255), "b": random.randint(0, 255)},
        {"r": random.randint(0, 255), "g": random.randint(0, 255), "b": random.randint(0, 255)},
        {"r": random.randint(0, 255), "g": random.randint(0, 255), "b": random.randint(0, 255)}

        # {"r": 255, "g": 1, "b": 1},
        # {"r": 153, "g": 255, "b": 255},
        # {"r": 255, "g": 153, "b": 51},
        # {"r": 255, "g": 153, "b": 51},
        # {"r": 67, "g": 93, "b": 100},
        # {"r": 99, "g": 150, "b": 25},
        # {"r": 200, "g": 200, "b": 50},
        # {"r": 66, "g": 1, "b": 200},
        # {"r": 200, "g": 160, "b": 99},
        # {"r": 15, "g": 155, "b": 85},
    ]
    return colour


def RGBToHex(r, g, b):
    """
    Takes the RGB values and returns the hex code.
    :return:
    The hex code
    """

    return "#{:02x}{:02x}{:02x}".format(r, g, b)


def CompCol(r, g, b):
    """
    Takes the input RGB values and passes them into the
    complement colour function from colourise, returning the
    complimentary RGB values
    :return:
    A tuple containing the values
    """

    comp = col.complement_rgb(r, g, b)
    hexcomp = RGBToHex(round(comp[0]), round(comp[1]), round(comp[2]))

    return hexcomp
