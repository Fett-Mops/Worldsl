import math
from Enemys import Enemy
import random
import numpy as np

def fast_fourier_transformation(enemy : Enemy) -> int:
    enemy.angle += 1
    enemy_a = enemy.angle
    
    freq = 0.25
    print(f"{enemy_a = }")

    # Auch das Hinzufügen von anderen Sinuswellen
    component1 = 10 * np.sin(2 * np.pi  *4* enemy_a/30)  # 50 Hz Sinus
    component2 = 10 * np.sin(2 * np.pi  *2* enemy_a/30) # 120 Hz Sinus

    # Gesamtes Signal
    signal =  component1 + component2
    return enemy.y + signal 

def simple(enemy : Enemy):
    enemy.angle += 1
    return enemy.y + math.cos(enemy.angle/30) * random.randint(1,8)/4