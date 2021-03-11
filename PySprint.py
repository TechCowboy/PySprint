import pygame
import time
import math
pygame.init()
 
display_width = 640
display_height = 400
flags = 0
#Scale screen
#flags = pygame.SCALED

gameDisplay = pygame.display.set_mode((display_width,display_height),flags)
clock = pygame.time.Clock()

class Track:    
    background = pygame.image.load('Assets/SuperSprintTrack1.png')
    trackMask = pygame.image.load('Assets/SuperSprintTrack1Mask.png').convert_alpha()            

    externalBorders = [   
        (101,52),   
        (544,53),
        (560,54),
        (577,59),
        (591,71),
        (601,84),
        (606,96),
        (608,110),
        (610,331),
        (572,374),
        (545,377),
        (449,374),
        (431,371),
        (278,235),
        (266,228),
        (256,231),
        (257,258),
        (257,273),
        (266,318),
        (266,354),
        (247,373),
        (99,373),
        (71,368),
        (35,330),
        (37,112),
        (40,93),
        (46,79),
        (64,59),
        (75,55),
        (84,51)
        ]

    internalBorders=[
        (133,134),
        (129,143),
        (125,153),
        (124,295),
        (132,305),
        (143,307),
        (157,298),
        (161,163),
        (178,148),
        (292,148),
        (314,152),
        (333,161),
        (489,306),
        (499,307),
        (504,302),
        (512,299),
        (512,141),
        (503,131),
        (137,130)
    ]

class Car:
    #Appearance
    sprites = {
    0:pygame.image.load('Assets/BlueCar0.png').convert_alpha(),
    1:pygame.image.load('Assets/BlueCar1.png').convert_alpha(),
    2:pygame.image.load('Assets/BlueCar2.png').convert_alpha(),
    3:pygame.image.load('Assets/BlueCar3.png').convert_alpha(),
    4:pygame.image.load('Assets/BlueCar4.png').convert_alpha(),
    5:pygame.image.load('Assets/BlueCar5.png').convert_alpha(),
    6:pygame.image.load('Assets/BlueCar6.png').convert_alpha(),
    7:pygame.image.load('Assets/BlueCar7.png').convert_alpha(),
    8:pygame.image.load('Assets/BlueCar8.png').convert_alpha(),
    9:pygame.image.load('Assets/BlueCar9.png').convert_alpha(),
    10:pygame.image.load('Assets/BlueCar10.png').convert_alpha(),
    11:pygame.image.load('Assets/BlueCar11.png').convert_alpha(),
    12:pygame.image.load('Assets/BlueCar12.png').convert_alpha(),
    13:pygame.image.load('Assets/BlueCar13.png').convert_alpha(),
    14:pygame.image.load('Assets/BlueCar14.png').convert_alpha(),
    15:pygame.image.load('Assets/BlueCar15.png').convert_alpha()
    }
    
    angleVectorSign = {
    0:(0,-1),
    1:(1,-1),
    2:(1,-1),
    3:(1,-1),
    4:(1,0),
    5:(1,1),
    6:(1,1),
    7:(1,1),
    8:(0,1),
    9:(-1,1),
    10:(-1,1),
    11:(-1,1),    
    12:(-1,0),
    13:(-1,-1),
    14:(-1,-1),
    15:(-1,-1),
    16:(0,-1)
    }

    #Position & Vector
    x = 325
    y = 65
    sprite_angle = 12
    angle= 12
    speed = 0
    aIntersectSide=(0,0)
    bIntersectSide=(0,0)
    xVector=0
    yVector=0
    sin_angle=0
    
    #Mechanics
    rotation_step=.30
    acceleration_step=0.3        
    deceleration_step=0.3
    bump_decelaration_step=1.5   
    speed_max=12
    bump_speed=6
    decelerating=False
    rotating=False
    bumping=False
    bumpingVertical=False
    bumpingHorizontal=False
    bumpingDiagonal=False
    diagonalDetectionTolerance = 5
    
    def rotate(self, left):
        self.rotating=True
        if left:
            self.angle -= self.rotation_step 
        else:
            self.angle += self.rotation_step

        if self.angle<0:
            self.angle +=  16
        if self.angle>=16:
            self.angle -= 16
        self.sprite_angle =  round(self.angle,0)
        if self.sprite_angle==16:
            self.sprite_angle = 0

    def accelerate(self):
         self.decelerating=False
         if self.speed < self.speed_max:
            self.speed+=self.acceleration_step

    def decelerate(self):
        self.decelerating=True
        if self.bumping:
            self.speed-=self.bump_decelaration_step
        else:
            self.speed-=self.deceleration_step

        if self.speed < 0:
            self.speed=0
            self.decelerating=False
            #Stop Bumping routine once speed down to 0
            self.bumping=False
            self.bumpingDiagonal=False
            self.bumpingHorizontal=False
            self.bumpingVertical=False

    def searchBorderSide(self, polygonBorder,xIntersect,yIntersect):
        self.bumpingDiagonal = False
        self.bumpingHorizontal = False
        self.bumpingVertical = False
        for i in range(0,len(polygonBorder)):
            nextIndex = i+1
            if nextIndex == len(polygonBorder):
                nextIndex=0
            top=0
            left=0
            if polygonBorder[i][0]<=polygonBorder[nextIndex][0]:
                top=polygonBorder[i][0]
            else:
                top=polygonBorder[nextIndex][0]
            if polygonBorder[i][1]<=polygonBorder[nextIndex][1]:
                left=polygonBorder[i][1]
            else:
                left=polygonBorder[nextIndex][1]

            rect_width = abs(polygonBorder[nextIndex][0]-polygonBorder[i][0])
            if rect_width==0:
                rect_width=1
            rect_height = abs(polygonBorder[nextIndex][1]-polygonBorder[i][1])
            if rect_height==0:
                rect_height=1
            wall_rect = pygame.Rect(top,left,rect_width,rect_height)
            #Enlarge detection Box to maximize chance of hitting a polygon side
            sprite_rect = pygame.Rect(xIntersect-7,yIntersect-7,14,14)

            if sprite_rect.colliderect(wall_rect):
                print('found matching pair of points ({},{})'.format(polygonBorder[i],polygonBorder[nextIndex]))
                self.aIntersectSide=polygonBorder[i]
                self.bIntersectSide=polygonBorder[nextIndex]
                if (abs(polygonBorder[i][0]-polygonBorder[nextIndex][0])<=self.diagonalDetectionTolerance) and (abs(polygonBorder[i][1]-polygonBorder[nextIndex][1])>self.diagonalDetectionTolerance):
                    print('x delta <={} - looks vertical enough'.format(self.diagonalDetectionTolerance))
                    self.bumpingVertical = True
                    return True
                if (abs(polygonBorder[i][0]-polygonBorder[nextIndex][0])>self.diagonalDetectionTolerance) and (abs(polygonBorder[i][1]-polygonBorder[nextIndex][1])<=self.diagonalDetectionTolerance):
                    print('y delta <={} - looks horizontal enough'.format(self.diagonalDetectionTolerance))
                    self.bumpingHorizontal = True
                    return True
                print('Not sure about direction - Diagonal Bumping')
                self.bumpingDiagonal = True
                self.bumpingHorizontal = False
                self.bumpingVertical = False
                return True
        return False

    def calculateVectorFromSprite(self):
            self.sin_angle = math.sin(math.radians(abs(self.sprite_angle*22.5-90)))
            
            self.yVector = abs(self.speed * self.sin_angle)
                                
            self.yVector = self.yVector * self.angleVectorSign[self.sprite_angle][1]
            
            self.xVector = math.sqrt(self.speed*self.speed-self.yVector*self.yVector)
            
            self.xVector = self.xVector * self.angleVectorSign[self.sprite_angle][0]
    

    def updatePosition(self, track):                
        if not self.decelerating:
            #Calculate Vector - No skidding
            self.calculateVectorFromSprite()
        else:
            if not self.rotating:
                #Start Skidding - Ignore current Rotation sprite, update speed and use previous Angle and sign
                if abs(self.yVector)>0:
                    self.yVector = self.yVector * abs(self.speed * self.sin_angle) / abs(self.yVector)

                if abs(self.xVector)>0:                    
                    self.xVector = self.xVector * math.sqrt(self.speed*self.speed-self.yVector*self.yVector)  / abs(self.xVector)
                
                if self.xVector==0 and self.yVector==0 and self.speed>0:
                     #Wrong situation: reset to default vector
                     self.calculateVectorFromSprite()

        if self.bumping:            
            if self.bumpingVertical:
                #Bump horizontally when hitting a vertical border diagonally or horizontally
                self.yVector = 0
                self.x -= self.xVector
                self.y -= self.yVector
            else:
                if self.bumpingHorizontal:
                    #Bump vertically when hitting a horizontal border diagonally or vertically
                    self.xVector = 0
                    self.x -= self.xVector
                    self.y -= self.yVector
                else:
                    if self.bumpingDiagonal:
                        #Diagonal Bumping: Bump Diagnoally if hit Horizontally - or Vertically  - Vert or Horiz Bump if hit diagonally
                        aPoint=self.aIntersectSide
                        bPoint=self.bIntersectSide
                        
                        if self.angleVectorSign[self.sprite_angle][1]==0 or self.angleVectorSign[self.sprite_angle][0]==0:
                            #Car is Horizontal or Vertical - Force 45 degree angle
                            self.sin_angle = math.sin(math.radians(abs(45)))
                            self.yVector = abs(self.speed * self.sin_angle)                                            
                            self.xVector = math.sqrt(self.speed*self.speed-self.yVector*self.yVector)

                            if (aPoint[0]<bPoint[0] and aPoint[1]<bPoint[1]) or (aPoint[0]>bPoint[0] and aPoint[1]>bPoint[1]):
                                #Top-Right or Bottom Left Diagonal    
                                if self.angleVectorSign[self.sprite_angle][1]>0 or self.angleVectorSign[self.sprite_angle][0]<0:
                                    #Bottom Left Diagonal    
                                    self.x += self.xVector
                                    self.y -= self.yVector
                                if self.angleVectorSign[self.sprite_angle][1]<0 or self.angleVectorSign[self.sprite_angle][0]>0:
                                    #Top Right Diagonal    
                                    self.x -= self.xVector
                                    self.y += self.yVector

                            if (aPoint[0]>bPoint[0] and aPoint[1]<bPoint[1]) or (aPoint[0]<bPoint[0] and aPoint[1]>bPoint[1]):
                                #Top-left or Bottom Right Diagonal                    
                                if self.angleVectorSign[self.sprite_angle][1]<0 or self.angleVectorSign[self.sprite_angle][0]<0:
                                    #Top Left Diagonal    
                                    self.x += self.xVector
                                    self.y += self.yVector
                                if self.angleVectorSign[self.sprite_angle][1]>0 or self.angleVectorSign[self.sprite_angle][0]>0:
                                    #Bottom Right Diagonal    
                                    self.x -= self.xVector
                                    self.y -= self.yVector
                        else:
                            #Car is Diagonal - Normal Bump
                            self.x -= self.xVector
                            self.y -= self.yVector
                    # else:
                    #     self.x -= self.yVector
                    #     self.y -= self.xVector

        else:
            self.x += self.xVector
            self.y += self.yVector
        self.rotating=False
        
        if self.speed>0:
            #If the car is not stopped Detect Track Borders. If not let it rotate over the edges & ignore collisions
            track_mask = pygame.mask.from_surface(track.trackMask,50)
            car_mask = pygame.mask.from_surface(self.sprites[self.sprite_angle],50)
            intersect_point = track_mask.overlap(car_mask,((round(self.x),round(self.y))))
            if intersect_point:
                #Check if the car is going into a border a going away from it (i.e. the tail touching the border)
                #If it is going away from the border then skip the Bump routine


                self.bumping = True
                self.speed=self.bump_speed
                #Determine the agle at which angle the car is intersecting with the Border: either right angle or not
                #Lookup in the map for the closest intersection point and the polygon side that is intersecting            
                xIntersect = intersect_point[0]
                yIntersect = intersect_point[1]
                print('Ext Border Detected ({},{})'.format(xIntersect,yIntersect))            
                            
                #Search external borders other corners of the sprite in case no border poinst detected
                if not self.searchBorderSide(track.externalBorders,xIntersect,yIntersect):
                    if not self.searchBorderSide(track.internalBorders,xIntersect,yIntersect):
                        self.bumpingDiagonal=False
                        self.bumpingHorizontal=False
                        self.bumpingVertical=False                    
                        self.bumping=False                    
                        # print('Default Bumping Orientation based on Sprite')            
                        # if abs(self.angleVectorSign[self.sprite_angle][1])>0 and abs(self.angleVectorSign[self.sprite_angle][0])>0:
                        #     #Diagonal
                        #     self.bumpingDiagonal = True
                        # else:
                        #     if self.angleVectorSign[self.sprite_angle][1]==0:
                        #         #Horizontal car bumping Vertical
                        #         self.bumpingVertical = True
                        #     else:
                        #         #Vertical car bumping Horizontal
                        #         self.bumpingHorizontal = True
        else:
            self.bumpingDiagonal=False
            self.bumpingHorizontal=False
            self.bumpingVertical=False
            self.bumping=False                    
            



    
    
    def blit(self,track):
        if not self.bumping:
            self.updatePosition(track)
        if self.bumping:
            self.decelerating=True
            self.rotating=False
            self.updatePosition(track)        
        gameDisplay.blit(self.sprites[self.sprite_angle], (self.x, self.y))    


def game_loop():
    blueCar = Car()
    track1= Track()
 
    gameExit = False
 
    while not gameExit:
        if not blueCar.bumping:
            if pygame.key.get_pressed()[pygame.K_RCTRL]:
                blueCar.accelerate()
            else:
                blueCar.decelerate()

            if pygame.key.get_pressed()[pygame.K_LEFT]:
                blueCar.rotate(True)
            
            if pygame.key.get_pressed()[pygame.K_RIGHT]:
                blueCar.rotate(False)

            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RCTRL:
                        blueCar.accelerate()
                    if event.key == pygame.K_LEFT:
                        blueCar.rotate(True)
                    if event.key == pygame.K_RIGHT:
                        blueCar.rotate(False)
        else:
            blueCar.decelerate()
        gameDisplay.blit(track1.background, (0, 0))
        blueCar.blit(track1)
        pygame.display.update()
        clock.tick(30)


game_loop()
