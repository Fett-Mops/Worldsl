import math
from Enemys import Enemy
import random
import numpy as np

def fast_fourier_transformation(enemy : Enemy) -> int:
    enemy.angle += 1
    enemy_a = enemy.angle
    
    freq = 0.25
    print(enemy_a)
    x = np.sin(2*np.pi*freq*enemy_a/30)
    x += 0.2 * np.sin(5 * 2 * np.pi*freq*enemy_a/30)
    x += 1/1.1 * np.sin(1.1 *2*np.pi*freq*enemy_a/30)

    
    return enemy.y + x

def simple(enemy : Enemy):
    enemy.angle += 1
    return enemy.y + math.cos(enemy.angle/30) * random.randint(1,8)/4