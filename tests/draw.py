import matplotlib.pyplot as plt

def ploting(methods: list, values: list, control: dict, interval: tuple) -> None:
    for i in range(interval[0], interval[1]):
        plt.bar(methods[i], values[i])
    plt.title(control['title'])
    plt.xlabel(control['xlabel'])
    plt.ylabel(control['ylabel'])
    plt.show()
    return None