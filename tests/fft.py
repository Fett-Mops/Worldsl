import numpy as np
import matplotlib.pyplot as plt
import random

col = ["red", "blue", "green"]

def fast_fourier_transformation(mult : bool = True) -> tuple:
    depth = 0
    freq = random.randint(1,10)
    ampli = random.randint(1,10)

    x = np.arange(0, 500, 0.1)
    y = ampli * np.sin(x/25 *2 * np.pi * freq)

    if mult:
        depth = random.randint(1,100)
        #plt.plot(x,y, color="blue")

    if depth >= 1:
        for i in range(depth):
            new = fast_fourier_transformation(False)
            #plt.plot(*new, label = f"{freq =}, {ampli = }", color=col[i])
            y += new[1]

    print(f"{depth = }, {freq = }, {ampli = }")
    return  x, y


for _ in range(1):
    print(_)
    plt.plot(*fast_fourier_transformation(), color = "yellow")
plt.show()