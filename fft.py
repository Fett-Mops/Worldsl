import math
from Enemys import Enemy
import random
import numpy as np

def fast_fourier_transformation(enemy : Enemy) -> float:
    y = 0
    x = enemy.angle

    for set in enemy.afa:
            new = set[1] * np.sin(x/25 *2 * np.pi * set[0])
            y += new
            print(y)
            print(f"{len(enemy.afa) = }, {set[0] = }, {set[1] = }")

    return  y
 

def simple(enemy : Enemy) -> float:
    return  math.cos(enemy.angle/30) * random.randint(1,8)/10