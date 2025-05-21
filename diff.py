
import os
from file_handler import read_json
from Enemys import Enemy

class Manager:
    def __init__(self) -> None:
        self.ls = read_json(os.path.join(os.getcwd(), "words.json"))
        #self.ls = ["."]
        Enemy.ls = self.ls

        self.difficulty = 1
        self.min = 2
        self.max = self.min + 4
        self.respon_time = 1.8

    def set_len(self) -> None:
        self.ls = list(filter(lambda x : self.max >= len(x) , self.ls))
      
        Enemy.ls = self.ls
    
    def update(self) -> None:
        if self.respon_time >= 1:
            self.respon_time += 0.0025 * self.difficulty * -1
            
        print(self.respon_time)

        self.max = int(self.min) + 3 + int(self.difficulty/4)
        self.set_len()
