import math
import random
import threading

import pygame as pg

from diff import Manager
from fft import fast_fourier_transformation, simple
from Enemys import Enemy
class Game:
    def __init__(self) -> None:
        pg.init()
        pg.font.init()
        
        self.FPS = 60
        self.clock = pg.time.Clock()
        self.font = pg.font.SysFont('Comic Sans MS', 30, bold = True)
        self.manager = Manager()

        self.running = False
        self.WIDTH, self.HEIGHT = 1000,600
        self.screen = pg.display.set_mode((self.WIDTH, self.HEIGHT))

        self.inp = Enemy(self.font, self.HEIGHT - 50 ,0)
        self.inp.r_color = (255, 255, 255)
        self.inp.inp = True       
        self.inp.x = 20
        self.amps = [random.randint(1,10) for _ in range(1)]
        self.enemys = [Enemy(self.font, i*50, amp) for i, amp in enumerate(self.amps)]

    def draw(self, surf, pos):
        self.screen.blit(surf, pos)
    
    def spawn_enemy(self) -> None:
        self.enemys.append(Enemy(self.font, random.randint(20, 500), 1))
        print(threading.active_count())
        self.spawn_timer = threading.Timer(self.manager.respon_time, self.spawn_enemy)
        self.spawn_timer.start()

    def run(self) -> None:
        self.running = True

        self.spawn_timer = threading.Timer(self.manager.respon_time, self.spawn_enemy)
        self.spawn_timer.start()

        while self.running:
            #self.screen.fill((0,0,0))
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    self.spawn_timer.daemon = True
                    self.running = False

                if event.type == pg.KEYDOWN:
                    if event.key == pg.K_DELETE:
                        Enemy.mask = ""

                    elif event.key == pg.K_BACKSPACE:
                        Enemy.mask = Enemy.mask[:-1]
                    else:
                        Enemy.mask += event.unicode

                    Enemy.mask = Enemy.mask[1:] if Enemy.mask.startswith(" ") else Enemy.mask
                    self.inp.name = Enemy.mask
                    
            for i, enemy in enumerate (self.enemys):
                enemy.x += .5
                enemy.y = fast_fourier_transformation(enemy)
                
                if enemy.update_mask():
                    self.enemys.pop(i)
                    Enemy.mask = ""
                    self.manager.difficulty +=1
                    self.manager.update()
                    continue

                if enemy.x >= self.WIDTH:
                    self.enemys.pop(i)
                    self.manager.difficulty -=1
                    self.manager.update()

                self.draw(enemy.render, (enemy.x, enemy.y))
                self.draw(enemy.mask_render, (enemy.x, enemy.y))

            self.inp.update_mask()
            self.draw(self.inp.mask_render, (self.inp.x, self.inp.y))
            man = [("difficulty",self.manager.difficulty), 
                   ("max", self.manager.max), 
                   ("min", self.manager.min),
                   ("respn_t", self.manager.respon_time)]
            
            for y, (name, val) in enumerate(man):
                render = self.font.render(f"{name} : {val}", False, (255,255,255))
                self.draw(render, (self.WIDTH / 2, y*30))
            

            pg.display.flip()
            self.clock.tick(self.FPS)
if __name__ == "__main__":
    Game().run()