# generates humidity graph in local folder
import matplotlib.pyplot as plt

def hGraph(var):
    time = list(range(24))
    plt.plot(time, var)
    plt.xlabel('Time interval / hour')
    plt.ylabel('Humidity / %')
    plt.savefig('hGraph.png')
