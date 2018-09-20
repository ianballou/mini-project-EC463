from random import randint

# function that generates 24 random temperature
def temperature():
    temperature = [randint(20, 100) for i in range(24)]
    return temperature
