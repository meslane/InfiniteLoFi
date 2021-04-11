import pygame

class piano():
    def __init__(self):
        self.keylist = []
        self.white_keylist = []
        self.black_keylist = []

    def build(self, screen):
        #number of keys on a piano
        num_keys = 88

        #Special case at the beginning of the piano
        self.add(0, 0, screen)
        self.add(1, 1, screen)
        self.add(0, 2, screen)

        #separates the keys into black and white keys
        for key in range(1, num_keys-3):
            if(key % 12 == 2 or key % 12 == 4 or key % 12 == 7
            or key % 12 == 9 or key % 12 == 11):
                self.add(1, key+2, screen)
            else:
                self.add(0, key+2, screen)

        #special case for the last key
        self.add(0, 87, screen)

    def add(self, color, number, screen):
        #white key
        #sets the width of the white keys
        #52 white keys on a piano
        white_width = (screen.get_width()/52)-2

        #draws the white keys first
        if color == 0:
            self.keylist.append(key((number*screen.get_width()/52), 0, white_width, screen.get_height()/4 - 2, 0, (255, 155, 40)))
            self.white_keylist.append(self.keylist[number])

        #draws the black keys on top of the white keys
        if color == 1:
            black_width = screen.get_width()/78-2
            black_X = self.keylist[number - 1].left + (white_width / 2) + (black_width/4) + 1
            self.keylist.append(key(black_X, 0, black_width, screen.get_height()/8 - 2, 1, (255, 155, 40)))
            self.black_keylist.append(self.keylist[number])

    def draw(self, screen):
        white_width = (screen.get_width() / 52) - 2
        num_white_keys = 0
        num_black_keys = 0

        for i in range(len(self.keylist)):
            if self.keylist[i].type == 0:
                self.keylist[i].move_and_rescale(num_white_keys*screen.get_width()/52, 0,white_width, screen.get_height()/4 - 2)
                num_white_keys += 1

            if self.keylist[i].type == 1:
                num_black_keys += 1
                black_width = screen.get_width() / 78
                black_X = self.keylist[i - 1].left + (white_width / 2) + (black_width/4) + 1
                self.keylist[i].move_and_rescale(black_X, 0, black_width, screen.get_height()/8 - 2)

        for white_key in self.white_keylist:
            white_key.draw(screen)

        for black_key in self.black_keylist:
            black_key.draw(screen)

    def press(self, number):
        #changes the color of a key when that note is played
        try:
            self.keylist[number].press()
        except IndexError:
            print("key at index {} does not exist".format(number))
            
    def release(self, number):
        #reverts the color of the key back to normal
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
        self.type = type
        
    def press(self):
        self.color = self.pressColor
        
    def release(self):
        self.color = self.passiveColor


    def move_and_rescale(self, newleft, newtop, new_width, new_height):
        # scales the keys when the size of the window changes
        self.left = newleft
        self.top = newtop
        self.width = new_width
        self.height = new_height
        
    def draw(self, surface):
        pygame.draw.rect(surface, self.color, self)