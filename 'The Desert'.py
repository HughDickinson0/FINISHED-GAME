import pygame
import time
import random

pygame.init()


display_width = 800
display_height = 600
#display dimensions

black = (0,0,0)
white = (255,255,255)
red = (255,0,0)
#colour variables

car_width = 53
road_width = 460

oil = pygame.image.load('oil_1.png')
groundImg = pygame.image.load('ground.png')

cactusImg0 = pygame.image.load('cactus_0.png')
cactusImg1 = pygame.image.load('cactus_1.png')
cactusImg2 = pygame.image.load('cactus_2.png')
cactusImg3 = pygame.image.load('cactus_3.png')

roadImg_0 = pygame.image.load('road_0.png')
roadImg_1 = pygame.image.load('road_1.png')

rockImg0 = pygame.image.load('rock_0.png')
rockImg1 = pygame.image.load('rock_1.png')
rockImg2 = pygame.image.load('rock_2.png')
rockImg3 = pygame.image.load('rock_3.png')
rockImg4 = pygame.image.load('rock_4.png')
#importing obstacle images and ground and road

gameDisplay = pygame.display.set_mode((display_width,display_height))
pygame.display.set_caption('The Desert')
clock = pygame.time.Clock()

carImg = pygame.image.load('car_0.png')
carLeftImg = pygame.image.load('car_1.png')
carRightImg = pygame.image.load('car_2.png')
#importing car images

def things_dodged(count):
    font = pygame.font.SysFont(None, 25)
    text = font.render("Dodged: "+str(count), True, black)
    gameDisplay.blit(text,(0,0))

def things(thingx, thingy, thingw, thingh, color):
    gameDisplay.blit((oil),[thingx, thingy, thingw, thingh])
#oil obstacle

def rock0(rock0x, rock0y, rock0w, rock0h):
    gameDisplay.blit((rockImg0),[rock0x,rock0y, rock0w,rock0h])

def rock1(rock1x, rock1y, rock1w, rock1h):
    gameDisplay.blit((rockImg1),[rock1x,rock1y,rock1w,rock1h])

def rock2(rock2x, rock2y, rock2w, rock2h):
    gameDisplay.blit((rockImg2),[rock2x,rock2y,rock2w,rock2h])

def rock3(rock3x, rock3y, rock3w, rock3h):
    gameDisplay.blit((rockImg3),[rock3x,rock3y,rock3w,rock3h])

def rock4(rock4x, rock4y, rock4w, rock4h):
    gameDisplay.blit((rockImg4),[rock4x,rock4y,rock4w,rock4h])

def cactus0(cactus0x, cactus0y, cactus0w, cactus0h, color):
    gameDisplay.blit((cactusImg0),[cactus0x, cactus0y, cactus0w, cactus0h])

def cactus1(cactus1x, cactus1y, cactus1w, cactus1h, color):
    gameDisplay.blit((cactusImg1),[cactus1x, cactus1y, cactus1w, cactus1h])

def cactus2(cactus2x, cactus2y, cactus2w, cactus2h, color):
    gameDisplay.blit((cactusImg2),[cactus2x, cactus2y, cactus2w, cactus2h])

def cactus3(cactus3x, cactus3y, cactus3w, cactus3h, color):
    gameDisplay.blit((cactusImg3),[cactus3x, cactus3y, cactus3w, cactus3h])

#cactus obstacle

def road0(roadx,roady):
    gameDisplay.blit(roadImg_0,(roadx,roady))

def road1(roadx,roady):
    gameDisplay.blit(roadImg_1,(roadx,roady))

def isfloat(num):
    #print(num)
    try:
        float(num)
        return True
    except ValueError:
        return False

def ground(groundx,groundy):
    gameDisplay.blit(groundImg,(groundx,groundy))
#displaying ground

def car(carx,cary):
    gameDisplay.blit(carImg,(carx,cary))
#displaying car



def carLeft(carx,cary):
    gameDisplay.blit(carLeftImg,(carx -10,cary -10))
#displaying car turning left
def carRight(carx,cary):
    gameDisplay.blit(carRightImg,(carx,cary))
#displaying car turning right
def text_objects(text, font):
    textSurface = font.render(text, True, black)
    return textSurface, textSurface.get_rect()

def message_display(text):
    largeText = pygame.font.Font('freesansbold.ttf',115)
    TextSurf, TextRect = text_objects(text, largeText)
    TextRect.center = ((display_width/2),(display_height/2))
    gameDisplay.blit(TextSurf, TextRect)

    pygame.display.update()

    time.sleep(2.5)

    game_loop()
    
def crash():
    message_display('You Crashed')
    
def game_loop():
    carx = (display_width * 0.45)
    cary = (display_height * 0.8)

    groundx = 0
    groundy = 0

    roadx = 0
    roady = 0

   # timinge = 0
    
    carx_change = 0


#lines 131-208 are coordinant/hitbox variables for oil(pothole), cacti and rocks
    thing_startx = random.randrange(175, 550)
    thing_starty = random.randrange(-700,-300)
    thing_speed = 10
    thing_width = 64
    thing_height = 64

    cactus0_startx = random.randrange(0, 175)
    cactus0_starty = random.randrange(-600,-100)
    cactus0_speed = 10
    cactus0_width = 78
    cactus0_height = 78

    cactus2_startx = random.randrange(625,800)
    cactus2_starty = random.randrange(-600,-400)
    cactus2_speed = 10
    cactus2_width = 78
    cactus2_height = 78

    cactus3_startx = random.randrange(0, 175)
    cactus3_starty = random.randrange(-1000,-450)
    cactus3_speed = 10
    cactus3_width = 78
    cactus3_height = 78

    cactus1_startx = random.randrange(675,800)
    cactus1_starty = random.randrange(-650,-400)
    cactus1_speed = 10
    cactus1_width = 78
    cactus1_height = 78

    rock0_startx = random.randrange(675,800)
    rock0_starty = random.randrange(-600,-400)
    rock0_speed = 10
    rock0_width = 78
    rock0_height = 78

    rock1_startx = random.randrange(675,800)
    rock1_starty = random.randrange(-600,-400)
    rock1_speed = 10
    rock1_width = 78
    rock1_height = 78

    rock2_startx = random.randrange(0,175)
    rock2_starty = random.randrange(-600,-200)
    rock2_speed = 10
    rock2_width = 78
    rock2_height = 78

    rock3_startx = random.randrange(0,175)
    rock3_starty = random.randrange(-600,-400)
    rock3_speed = 10
    rock3_width = 78
    rock3_height = 78

    rock4_startx = random.randrange(675,800)
    rock4_starty = random.randrange(-700,-400)
    rock4_speed = 10
    rock4_width = 78
    rock4_height = 78

    trailVar = random.randrange(0,200)
#trailvar is a variable that allows the secondary calling of the obstacle function to display somewhere else
    trailVary = random.randrange(-300,200,100)

    thingCount = 2

    #car(carx,cary)

    dodged = 0

    gameExit = False

    while not gameExit:
        
        car(carx,cary)

        
    
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_a:
                    carx_change = -10
                    carLeft(carx,cary)
                if event.key == pygame.K_d:
                    carx_change = 10
                    carRight(carx,cary)

            if event.type == pygame.KEYUP:
                if event.key == pygame.K_a or event.key == pygame.K_d:

                    carx_change = 0
                    car(carx,cary)

        carx += carx_change

        ground(groundx,groundy)

        #time.sleep(5)

     #   if (clock.tick % 2)==0:
       #     road0(roadx,roady)
       # else:
       #     road1(roadx,roady)
        
        # things(thingx, thingy, thingw, thingh, color)
        things(thing_startx, thing_starty, thing_width, thing_height, black)
        thing_starty += thing_speed

        cactus0(cactus0_startx, cactus0_starty, cactus0_width, cactus0_height, black)
        cactus1(cactus1_startx, cactus1_starty, cactus1_width, cactus1_height, black)
        cactus2(cactus2_startx, cactus2_starty, cactus2_width, cactus2_height, black)
        cactus3(cactus3_startx, cactus3_starty, cactus3_width, cactus3_height, black)
        
        cactus0_starty += cactus0_speed
        cactus1_starty += cactus1_speed
        cactus2_starty += cactus2_speed
        cactus3_starty += cactus3_speed

        cactus0((cactus0_startx+trailVar), (cactus0_starty-trailVary), cactus0_width, cactus0_height, black)
        cactus1((cactus1_startx-trailVar), (cactus1_starty-trailVary), cactus1_width, cactus1_height, black)
        cactus2((cactus2_startx-trailVar), (cactus2_starty-trailVary), cactus2_width, cactus2_height, black)
        cactus3((cactus3_startx+trailVar), (cactus3_starty-trailVary), cactus3_width, cactus3_height, black)

        rock0(rock0_startx, rock0_starty, rock0_width, rock0_height)
        rock1(rock1_startx, rock1_starty, rock1_width, rock1_height)
        rock2(rock2_startx, rock2_starty, rock2_width, rock2_height)
        rock3(rock3_startx, rock3_starty, rock3_width, rock3_height)
        rock4(rock4_startx, rock4_starty, rock4_width, rock4_height)

        rock0_starty += rock0_speed
        rock1_starty += rock1_speed
        rock2_starty += rock2_speed
        rock3_starty += rock3_speed
        rock4_starty += rock4_speed

        rock0((rock0_startx+trailVar), (rock0_starty-trailVar), rock0_width, rock0_height)
        rock1((rock1_startx+trailVar), (rock1_starty-trailVar), rock1_width, rock1_height)
        rock2((rock2_startx-trailVar), (rock2_starty-trailVar), rock2_width, rock2_height)
        rock3((rock3_startx-trailVar), (rock3_starty-trailVar), rock3_width, rock3_height)
        rock4((rock4_startx+trailVar), (rock4_starty-trailVar), rock4_width, rock4_height)
        
        car(carx,cary)

     #   timinge += 0.5

       #if isfloat(timinge) == False:
          #  road0(roadx,roady)
            
      #  if isfloat(timinge) == True:
          #  road1(roadx,roady)
        
        things_dodged(dodged)
        
        if carx > 650 - car_width or carx < 150:
            crash()
            
        if cactus0_starty > display_height:
            cactus0_starty = random.randrange(-600,-400)
            cactus0_startx = random.randrange(0, 150)
            cactus0_speed += 1

        if cactus1_starty > display_height:
            cactus1_starty = random.randrange(-600,-400)
            cactus1_startx = random.randrange(0, 150)
            cactus1_speed += 1

        if cactus2_starty > display_height:
            cactus2_starty = random.randrange(-600,-400)
            cactus2_startx = random.randrange(675,800)
            cactus2_speed += 1

        if cactus3_starty > display_height:
            cactus3_starty = random.randrange(-600,-400)
            cactus3_startx = random.randrange(675,800)
            cactus3_speed += 1

        if thing_starty > display_height:
            thing_starty = random.randrange(-600,-400)
            thing_startx = random.randrange(175,600)
            dodged += 1
            thing_speed += 1

        if rock0_starty > display_height:
            rock0_starty = random.randrange(-600,-400)
            rock0_startx = random.randrange(675,800)
            rock0_speed += 1

        if rock1_starty > display_height:
            rock1_starty = random.randrange(-600,-400)
            rock1_startx = random.randrange(675,800)
            rock1_speed += 1

        if rock2_starty > display_height:
            rock2_starty = random.randrange(-600,-400)
            rock2_startx = random.randrange(0,175)
            rock2_speed += 1

        if rock3_starty > display_height:
            rock3_starty = random.randrange(-600,-400)
            rock3_startx = random.randrange(0,175)
            rock3_speed += 1

        if rock4_starty > display_height:
            rock4_starty = random.randrange(-600,-400)
            rock4_startx = random.randrange(675,800)
            rock4_speed += 1
        #
        if cary < thing_starty+thing_height:
            #print('y crossover')

            if carx > thing_startx and carx < thing_startx + thing_width or carx+car_width > thing_startx and carx + car_width < thing_startx+thing_width:
              #  print('x crossover')
                crash()
        ####
            if carx > cactus0_startx and carx < cactus0_startx + cactus0_width or carx+car_width > cactus0_startx and carx + car_width < cactus0_startx + cactus0_width:
                crash()

            if carx > cactus1_startx and carx < cactus1_startx + cactus1_width or carx+car_width > cactus1_startx and carx + car_width < cactus1_startx + cactus1_width:
                crash()

            if carx > cactus2_startx and carx < cactus2_startx + cactus2_width or carx+car_width > cactus2_startx and carx + car_width < cactus2_startx + cactus2_width:
                crash()

            if carx > cactus3_startx and carx < cactus3_startx + cactus3_width or carx+car_width > cactus3_startx and carx + car_width < cactus3_startx + cactus3_width:
                crash()

            if carx > rock0_startx and carx < cactus0_startx + cactus0_width or carx+car_width > rock0_startx and carx + car_width< rock0_startx + rock0_width:
                crash()

            if carx > rock1_startx and carx < rock_startx + rock1_width or carx+car_width > rock1_startx and carx + car_width< rock1_startx + rock1_width:
                crash()

            if carx > rock2_startx and carx < rock2_startx + rock2_width or carx+car_width > rock2_startx and carx + car_width< rock2_startx + rock2_width:
                crash()

            if carx > rock3_startx and carx < rock3_startx + rock3_width or carx+car_width > rock3_startx and carx + car_width< rock3_startx + rock3_width:
                crash()

            if carx > rock4_startx and carx < rock4_startx + rock4_width or carx+car_width > rock4_startx and carx + car_width< rock4_startx + rock4_width:
                crash()
        
        pygame.display.update()
        clock.tick(30)
        #print(isfloat(clock.tick))
        #print(clock.tick)


game_loop()
pygame.quit()
quit()
