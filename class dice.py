import pygame
import random
pygame.init

#constants for colors
RED = (250,0,0)
ORANGE = (200, 100, 0)
GREEN = (0,150, 0)
WHITE = (255,255,255)
BLACK = (0, 0, 0)

### class definition--------------------------------------------
class flower:
    def __init__(self, xpos, ypos):
        self.xpos = xpos
        self.ypos = ypos
        self.side = 0
        
    def roll(self):
        self.side = random.randrange(1,7)
    def output(self):
        if self.side == 1:
            print ("you are facing side of 1")
        elif self.side == 2:
            print ("you are facing side of 2")
        elif self.side == 3:
            print ("you are facing side of 3") 
        elif self.side == 4:
            print ("you are facing side of 4")
        elif self.side == 5:
            print ("you are facing side of 5")
        elif self.side == 6:
            print ("you are facing side of 6")
    def draw(self):
        pygame.draw.rect(screen, (WHITE), (self.xpos-10, self.ypos+20, 100, 100))
        if self.side == 1:
            pygame.draw.circle(screen, (BLACK), (self.xpos+40, self.ypos+70), 20) 
        if self.side == 2:
            pygame.draw.circle(screen, (BLACK), (self.xpos+55, self.ypos+50), 20)
            pygame.draw.circle(screen, (BLACK), (self.xpos+25, self.ypos+90), 20)
        if self.side == 3:
            pygame.draw.circle(screen, (BLACK), (self.xpos+65, self.ypos+50), 20)
            pygame.draw.circle(screen, (BLACK), (self.xpos+15, self.ypos+50), 20)
            pygame.draw.circle(screen, (BLACK), (self.xpos+40, self.ypos+90), 20)
        if self.side == 4:
            pygame.draw.circle(screen, (BLACK), (self.xpos+65, self.ypos+45), 20)
            pygame.draw.circle(screen, (BLACK), (self.xpos+15, self.ypos+45), 20)
            pygame.draw.circle(screen, (BLACK), (self.xpos+65, self.ypos+94), 20)
            pygame.draw.circle(screen, (BLACK), (self.xpos+15, self.ypos+94), 20)
        if self.side == 5:
            pygame.draw.circle(screen, (BLACK), (self.xpos+65, self.ypos+40), 20)
            pygame.draw.circle(screen, (BLACK), (self.xpos+15, self.ypos+40), 20)
            pygame.draw.circle(screen, (BLACK), (self.xpos+65, self.ypos+99), 20)
            pygame.draw.circle(screen, (BLACK), (self.xpos+15, self.ypos+99), 20)
            pygame.draw.circle(screen, (BLACK), (self.xpos+40, self.ypos+70), 20)
        if self.side == 6:
            pygame.draw.circle(screen, (BLACK), (self.xpos+70, self.ypos+40), 20)
            pygame.draw.circle(screen, (BLACK), (self.xpos+20, self.ypos+40), 20)
            pygame.draw.circle(screen, (BLACK), (self.xpos+70, self.ypos+75), 20)
            pygame.draw.circle(screen, (BLACK), (self.xpos+20, self.ypos+75), 20)
            pygame.draw.circle(screen, (BLACK), (self.xpos+70, self.ypos+100), 20)
            pygame.draw.circle(screen, (BLACK), (self.xpos+20, self.ypos+100), 20)

#stamp (aka instantiate) flowers
flower1 = flower(200, 200)
flower2 = flower(400, 400)
flower3 = flower(100, 400)

#creates game screen and caption
screen = pygame.display.set_mode((800, 800))
pygame.display.set_caption("flower class demo")


#game variables
doExit = False #variable to quit out of game loop
clock = pygame.time.Clock() #sets up a game clock to regulate game speed

flower1.roll()
flower2.roll()
flower3.roll()
flower1.output()
flower2.output()
flower3.output()

#BEGIN GAME LOOP######################################################
while not doExit:
   
    clock.tick(60) #FPS (frames per second)
   
    #pygame's way of listening for events (key presses, mouse clicks, etc)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
           doExit = True #lets you quit program

    #keyboard input-----------------------------------
  
     
    #render section-----------------------------------
    flower1.draw()
    flower2.draw()
    flower3.draw()

    #draw class objects
    

    pygame.display.flip() #update graphics each game loop

#END GAME LOOP#######################################################
pygame.quit()
