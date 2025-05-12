from random import randint, random


class Enemy():
    ls = None
    mask = ""

    def __init__(self, font, yy, apms) -> None:
        
        self.inp = False
        self.name = self.get_name()
        self.color = self.get_color()
        self.r_color = (0 ,255 ,0)
        self.font = font
        self.offset = randint(0,10)
        self.update_mask()
        self.y = yy 
        #self.angle = randint(1,360)
        #self.active_stat = randint(3,10)
        self.angle = 180
        self.active_stat = 2
        self.x = 0
        self.font.set_underline(False)
        self.render = self.font.render(self.name, False, self.color)
    
    def get_color(self):
        rgb = []
        for _ in range(3):
            rgb.append(randint(0,255))
    
        return rgb if sum(rgb) >= 40 else self.get_color()


    def get_name(self) -> str:
        ls = self.ls
        return self.ls[randint(0, len(ls)-1)]
    
    def check_mask(self) -> str | bool:
        if Enemy.mask == None:
            return "" 
        
        if Enemy.mask == self.name and self.inp == False:
            return True
        
        return Enemy.mask if self.name.startswith(Enemy.mask) else ""
    
    def update_mask(self) -> None:
        mask = self.check_mask()
        if mask == True:
            return True
        
        if self.inp is True:
            self.font.set_underline(True)
        else:
            self.font.set_underline(False)

        self.mask_render = self.font.render(mask, False, self.r_color)
        
 

