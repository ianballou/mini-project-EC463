# function that generates 24 random humidity

from random import randint
def humidity ():
    humidity = [randint(30, 60) for i in range(24)]
    return humidity
