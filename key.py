import pygame

class piano():
    def __init__(self):
        self.keylist = []

    def build(self, screen):
        num_keys = 88
        self.add(0, 1, screen)
        self.add(1, 2, screen)
        self.add(0, 3, screen)
        for key in range(1, num_keys-5):
            if(key % 12 == 2 or key % 12 == 4 or key % 12 == 7
            or key % 12 == 9 or key % 12 == 11):
                self.add(1, key, screen)
            else:
                self.add(0, key, screen)
        self.add(0, 88, screen)

    def add(self, color, number, screen):

        #white key
        if color == 0:
            self.keylist.append(key((number*screen.get_width()/52), 0, (screen.get_width()/52)-2, screen.get_height()/4 - 2, 0, (255, 155, 40)))
        if color == 1:
            pass
        #     black_width = screen.get_width()/78-2
        #
        #     self.keylist.append(key(, 0, black_width, screen.get_height()/8 - 2, 0, (255, 155, 40))

    def draw(self, screen):
        for i in range(len(self.keylist)):
            if self.keylist[i].type == 0:
                self.keylist[i].move(i*screen.get_width()/52, 0)

            self.keylist[i].draw(screen)


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

class key(pygame.Rect):
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