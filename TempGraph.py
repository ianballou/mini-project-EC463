import matplotlib.pyplot as plt

# generates temperature graph in local folder
def tGraph(var):
    time = list(range(24))
    plt.plot(time, var)
    plt.xlabel('Time interval / hour')
    plt.ylabel('Temperature / F')
    plt.savefig('tGraph.png')
