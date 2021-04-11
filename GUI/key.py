import pygame

class piano():
    def __init__(self):
        self.keylist = []
        
    def press(self, number):
        try:
            self.keylist[number].press()
        except IndexError:
            print("key at index {} does not exist".format(number))
            
    def release(self.number):
        try:
            self.keylist[number].release()
        except IndexError:
            print("key at index {} does not exist".format(number))

class key(pygame.rect):
    def __init__(self, left, top, width, height, type, pressColor): #type: (0 = white, 1 = black)
        super().__init__(left, top, width, height)
        
        if type == 0:
            self.passiveColor = (255, 255, 255)
        elif type == 1:
            self.passiveColor = (0, 0, 0)
        
        self.color = self.passiveColor
        
    def press(self):
        self.color = self.pressColor
        
    def release(self):
        self.color = self.passiveColor
        
    def move(self, newleft, newtop):
        self.left = newleft
        self.top = newtop