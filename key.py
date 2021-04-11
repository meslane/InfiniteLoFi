import pygame

class piano():
    def __init__(self):
        self.keylist = []

    def build(self):
        num_keys = 88
        # self.add(0, 1)
        # self.add(1, 2)
        # self.add(0, 3)
        print("white")
        print("black")
        print("white")
        for key in range(4, num_keys-1):
            if(key % 12 == 2 or key % 12 == 4 or key % 12 == 7
            or key % 12 == 9 or key % 12 == 11):
                # self.add(1, key)
                print("black")
            else:
                # self.add(0, key)
                print("white")
        # self.add(0, 88)
        print("white")

    def add(self, color, number):
        self.keylist.append(key())

    def press(self, number):
        try:
            self.keylist[number].press()
        except IndexError:
            print("key at index {} does not exist".format(number))
            
    def release(self, number):
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
        self.pressColor = pressColor
        
    def press(self):
        self.color = self.pressColor
        
    def release(self):
        self.color = self.passiveColor
        
    def move(self, newleft, newtop):
        self.left = newleft
        self.top = newtop
        
    def draw(self, surface):
        pygame.draw.rect(surface, self.color, self)