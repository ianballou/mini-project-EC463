from random import randint
import matplotlib.pyplot as plt

# function that generates 24 random temperature
def temperature():
    temperature = [randint(20, 100) for i in range(24)]
    return temperature

# function that generates 24 random humidity
def humidity ():
    humidity = [randint(30, 60) for i in range(24)]
    return humidity

# generates temperature graph in local folder
def tGraph(var):
    time = list(range(24))
    plt.plot(time, var)
    plt.xlabel('Time interval / hour')
    plt.ylabel('Temperature / F')
    plt.savefig('tGraph.png')


# generates humidity graph in local folder
def hGraph(var):
    time = list(range(24))
    plt.plot(time, var)
    plt.xlabel('Time interval / hour')
    plt.ylabel('Humidity / %')
    plt.savefig('hGraph.png')
