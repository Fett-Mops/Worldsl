import random 

class Enemy():
    ls = None
    mask = ""


    def __init__(self, font, yy) -> None:
        
        self.inp = False
        self.name = self.get_name()
        self.color = [random.randint(30, 255) for _ in range(3)]
        self.r_color = (0, 255, 0)
        self.font = font
        self.offset = random.randint(0, 10)
        self.update_mask()
        self.angle = 180
        self.y = yy 
        self.depth = random.randint(1, 3)
        self.afa = [[random.random() / 2, random.random() / 5] for _ in range(self.depth)]
        self.active_stat = 2
        self.x = 0
        self.font.set_underline(False)
        self.render = self.font.render(self.name, False, self.color)
    
    def get_name(self) -> str:
        ls = self.ls
        return ls[random.randint(0, len(ls) -1)]
    
    def check_mask(self) -> str | bool:
        mask = Enemy.mask
        if mask == None:
            return "" 
        
        if mask == self.name and self.inp == False:
            return True
        
        return mask if self.name.startswith(mask) else ""
    
    def update_mask(self) -> None:
        mask = self.check_mask()
        if mask == True:
            return True
        
        if self.inp is True:
            self.font.set_underline(True)
        else:
            self.font.set_underline(False)

        self.mask_render = self.font.render(mask, False, self.r_color)
        
 

