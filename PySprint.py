import pygame
import time
import math
import random

pygame.init()

display_width = 640
display_height = 400
flags = 0
race_laps = 4

#Scale screen
#flags = pygame.SCALED
FPS = 30
DEBUG_FINISH = False
DEBUG_COLLISION = False
DEBUG_BUMP = False
DEBUG_CRASH = False
DEBUG_FLAG = False
DEBUG_FPS = True

game_display = pygame.display.set_mode((display_width, display_height), flags)
clock = pygame.time.Clock()

#Flag Events
GREENFLAG = pygame.USEREVENT + 1
WHITEFLAG = GREENFLAG + 1
CHECKEREDFLAG = WHITEFLAG + 1


#Load Assets

small_font = pygame.font.Font('Assets/SupersprintST-Regular.ttf',15)
black_color = (0, 0, 0)
white_color = (255, 255, 255)
red_color = (238, 0, 34)
blue_color = (68, 102, 238)
yellow_color = (238, 238, 102)




loading_screen = pygame.image.load('Assets/SuperSprintLoadingScreen.png').convert_alpha()
loading_screen_foreground = pygame.image.load('Assets/SuperSprintLoadingScreenForeground.png').convert_alpha()
credits_screen = pygame.image.load('Assets/SuperSprintCreditsScreen.png').convert_alpha()
splash_screen = pygame.image.load('Assets/SuperSprintSplashScreen.png').convert_alpha()
start_race_screen = pygame.image.load('Assets/SuperSprintStartRaceScreen.png').convert_alpha()


transition_dots = {
    0:pygame.image.load('Assets/TransitionDot0.png').convert_alpha(),
    1:pygame.image.load('Assets/TransitionDot1.png').convert_alpha(),
    2:pygame.image.load('Assets/TransitionDot2.png').convert_alpha(),
    3:pygame.image.load('Assets/TransitionDot3.png').convert_alpha(),
    4:pygame.image.load('Assets/TransitionDot4.png').convert_alpha(),
    5:pygame.image.load('Assets/TransitionDot5.png').convert_alpha(),
    6:pygame.image.load('Assets/TransitionDot6.png').convert_alpha(),
    7:pygame.image.load('Assets/TransitionDot7.png').convert_alpha()
}


scrolling_font = {
    'A':pygame.image.load('Assets/ScrollingFontA.png').convert_alpha(),
    'B':pygame.image.load('Assets/ScrollingFontB.png').convert_alpha(),
    'C':pygame.image.load('Assets/ScrollingFontC.png').convert_alpha(),
    'D':pygame.image.load('Assets/ScrollingFontD.png').convert_alpha(),
    'E':pygame.image.load('Assets/ScrollingFontE.png').convert_alpha(),
    'F':pygame.image.load('Assets/ScrollingFontF.png').convert_alpha(),
    'G':pygame.image.load('Assets/ScrollingFontG.png').convert_alpha(),
    'H':pygame.image.load('Assets/ScrollingFontH.png').convert_alpha(),
    'I':pygame.image.load('Assets/ScrollingFontI.png').convert_alpha(),
    'J':pygame.image.load('Assets/ScrollingFontJ.png').convert_alpha(),
    'K':pygame.image.load('Assets/ScrollingFontK.png').convert_alpha(),
    'L':pygame.image.load('Assets/ScrollingFontL.png').convert_alpha(),
    'M':pygame.image.load('Assets/ScrollingFontM.png').convert_alpha(),
    'N':pygame.image.load('Assets/ScrollingFontN.png').convert_alpha(),
    'O':pygame.image.load('Assets/ScrollingFontO.png').convert_alpha(),
    'P':pygame.image.load('Assets/ScrollingFontP.png').convert_alpha(),
    'Q':pygame.image.load('Assets/ScrollingFontQ.png').convert_alpha(),
    'R':pygame.image.load('Assets/ScrollingFontR.png').convert_alpha(),
    'S':pygame.image.load('Assets/ScrollingFontS.png').convert_alpha(),
    'T':pygame.image.load('Assets/ScrollingFontT.png').convert_alpha(),
    'U':pygame.image.load('Assets/ScrollingFontU.png').convert_alpha(),
    'V':pygame.image.load('Assets/ScrollingFontV.png').convert_alpha(),
    'W':pygame.image.load('Assets/ScrollingFontW.png').convert_alpha(),
    'X':pygame.image.load('Assets/ScrollingFontX.png').convert_alpha(),
    'Y':pygame.image.load('Assets/ScrollingFontY.png').convert_alpha(),
    'Z':pygame.image.load('Assets/ScrollingFontZ.png').convert_alpha(),
    '.':pygame.image.load('Assets/ScrollingFontDOT.png').convert_alpha(),
    ' ':pygame.image.load('Assets/ScrollingFontSPACE.png').convert_alpha(),
    '_':pygame.image.load('Assets/ScrollingFont_.png').convert_alpha(),
    ':':pygame.image.load('Assets/ScrollingFontSemiColon.png').convert_alpha()
}

green_flag_frames = {
    0:pygame.image.load('Assets/GreenFlag0.png').convert_alpha(),
    1:pygame.image.load('Assets/GreenFlag1.png').convert_alpha(),
    2:pygame.image.load('Assets/GreenFlag2.png').convert_alpha(),
    3:pygame.image.load('Assets/GreenFlag3.png').convert_alpha(),
    4:pygame.image.load('Assets/GreenFlag4.png').convert_alpha(),
    5:pygame.image.load('Assets/GreenFlag5.png').convert_alpha(),
    6:pygame.image.load('Assets/GreenFlag6.png').convert_alpha()
}

white_flag_frames = {
    0:pygame.image.load('Assets/WhiteFlag0.png').convert_alpha(),
    1:pygame.image.load('Assets/WhiteFlag1.png').convert_alpha(),
    2:pygame.image.load('Assets/WhiteFlag2.png').convert_alpha(),
    3:pygame.image.load('Assets/WhiteFlag3.png').convert_alpha(),
    4:pygame.image.load('Assets/WhiteFlag4.png').convert_alpha(),
    5:pygame.image.load('Assets/WhiteFlag5.png').convert_alpha(),
    6:pygame.image.load('Assets/WhiteFlag6.png').convert_alpha()
}

checkered_flag_frames = {
    0:pygame.image.load('Assets/CheckeredFlag0.png').convert_alpha(),
    1:pygame.image.load('Assets/CheckeredFlag1.png').convert_alpha(),
    2:pygame.image.load('Assets/CheckeredFlag2.png').convert_alpha(),
    3:pygame.image.load('Assets/CheckeredFlag3.png').convert_alpha(),
    4:pygame.image.load('Assets/CheckeredFlag4.png').convert_alpha(),
    5:pygame.image.load('Assets/CheckeredFlag5.png').convert_alpha(),
    6:pygame.image.load('Assets/CheckeredFlag6.png').convert_alpha()
}


helicopter_frames = {
    0:pygame.image.load('Assets/Helicopter0.png').convert_alpha(),
    1:pygame.image.load('Assets/Helicopter1.png').convert_alpha(),
    2:pygame.image.load('Assets/Helicopter2.png').convert_alpha()
}

helicopter_step = 10

dust_cloud_frames = {
    0:pygame.image.load('Assets/DustCloud0.png').convert_alpha(),
    1:pygame.image.load('Assets/DustCloud1.png').convert_alpha(),
    2:pygame.image.load('Assets/DustCloud2.png').convert_alpha(),
    3:pygame.image.load('Assets/DustCloud3.png').convert_alpha(),
    4:pygame.image.load('Assets/DustCloud4.png').convert_alpha()
}


explosion_frames = {
    0:pygame.image.load('Assets/Explosion0.png').convert_alpha(),
    1:pygame.image.load('Assets/Explosion1.png').convert_alpha(),
    2:pygame.image.load('Assets/Explosion2.png').convert_alpha(),
    3:pygame.image.load('Assets/Explosion3.png').convert_alpha(),
    4:pygame.image.load('Assets/Explosion4.png').convert_alpha(),
    5:pygame.image.load('Assets/Explosion5.png').convert_alpha(),
    6:pygame.image.load('Assets/Explosion6.png').convert_alpha(),
    7:pygame.image.load('Assets/Explosion7.png').convert_alpha(),
    8:pygame.image.load('Assets/Explosion8.png').convert_alpha(),
    9:pygame.image.load('Assets/Explosion9.png').convert_alpha(),
    10:pygame.image.load('Assets/Explosion10.png').convert_alpha(),
    11:pygame.image.load('Assets/Explosion11.png').convert_alpha(),
    12:pygame.image.load('Assets/Explosion12.png').convert_alpha(),
    13:pygame.image.load('Assets/Explosion13.png').convert_alpha(),
    14:pygame.image.load('Assets/Explosion14.png').convert_alpha(),
    15:pygame.image.load('Assets/Explosion15.png').convert_alpha(),
    16:pygame.image.load('Assets/Explosion16.png').convert_alpha(),
    17:pygame.image.load('Assets/Explosion17.png').convert_alpha(),
    18:pygame.image.load('Assets/Explosion18.png').convert_alpha()
}



class Track:
    background = pygame.image.load('Assets/SuperSprintTrack1.png')
    trackMask = pygame.image.load('Assets/SuperSprintTrack1Mask.png').convert_alpha()

    flag_anchor = (320, 28)

    external_borders = [
        (101, 52, 0),
        (544, 53, 1),
        (560, 54, 1),
        (577, 59, 1),
        (591, 71, 1),
        (601, 84, 1),
        (606, 96, 1),
        (608, 110, 0),
        (610, 331, 1),
        (572, 364, 1),
        (545, 368, 1),
        (449, 371, 0),
        (437, 369, 0),
        (273, 224, 0),
        (263, 224, 1),
        (257, 229, 1),
        (256, 231, 1),
        (257, 258, 1),
        (257, 273, 1),
        (266, 318, 1),
        (266, 354, 1),
        (247, 373, 1),
        (99, 373, 0),
        (71, 368, 1),
        (35, 330, 1),
        (37, 112, 0),
        (40, 93, 1),
        (46, 79, 1),
        (64, 59, 1),
        (75, 55, 1),
        (84, 51, 1)
        ]

    internal_borders = [
        (133, 134,1),
        (129, 143,1),
        (125, 153,1),
        (124, 295,1),
        (132, 305,1),
        (143, 307,1),
        (157, 298,1),
        (161, 163,1),
        (178, 148,1),
        (292, 148,1),
        (314, 152,1),
        (333, 161,1),
        (489, 306,1),
        (499, 307,1),
        (504, 302,1),
        (512, 299,1),
        (512, 141,1),
        (503, 131,1),
        (137, 130,1)
    ]

    finish_line = pygame.Rect(346, 48,4,82)
    finish_line_direction = -1


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

    angle_vector_sign = {
        0:(0, -1),
        1:(1, -1),
        2:(1, -1),
        3:(1, -1),
        4:(1, 0),
        5:(1, 1),
        6:(1, 1),
        7:(1, 1),
        8:(0, 1),
        9:(-1, 1),
        10:(-1, 1),
        11:(-1, 1),
        12:(-1, 0),
        13:(-1, -1),
        14:(-1, -1),
        15:(-1, -1),
        16:(0, -1)
    }

    #Position & Vector
    x_position = 325
    y_position = 65
    sprite_angle = 12
    angle = 12
    speed = 0
    a_intersect_side = (0, 0)
    b_intersect_side = (0, 0)
    x_intersect = 0
    y_intersect = 0
    x_vector = 0
    y_vector = 0
    sin_angle = 0

    #Mechanics
    #30FPS Settings
    if FPS == 30:
        rotation_step = .26
        acceleration_step = 0.13
        deceleration_step = 0.2
        bump_decelaration_step = 0.3
        speed_max = 8
        bump_speed = 6.5

    #60FPS Settings - Calibrated to an unmodified car
    if FPS == 60:
        rotation_step = .13
        acceleration_step = 0.065
        deceleration_step = 0.1
        bump_decelaration_step = 0.15
        speed_max = 4
        bump_speed = 3.25

    bump_animation_timer = 30
    crash_animation_timer = 30

    #Collision Settings
    diagonal_detection_tolerance = 2
    vector_simulation_length = 10
    side_detection_tolerance = 7
    max_speed_crash_threshold = 3000
    #Threshold over which theer is a higher chance to crash
    speed_crash_probability_threshold = 0.85
    #% increase of probability to crash if condition is true
    speed_crash_probability_penalty = 1.2
    sensitive_border_crash_probability_penalty = 1.4
    #Max Random number drawn to calculate Crash probability
    crash_random_max = 60
    crash_certainty_treshold = 80

    #Car State
    decelerating = False
    rotating = False
    bumping = False
    crashing = False
    bumping_vector_initialized = False
    bumping_vertical = False
    bumping_horizontal = False
    bumping_diagonal = False
    crash_finished = False
    animation_index = 0
    helicopter_index = 0
    helicopter_x = 0
    helicopter_y = 0
    collision_time = 0
    max_speed_reached = 0
    on_finish_line = True
    passed_finish_line_wrong_way = False
    lap_count = 0
    current_lap_start = 0
    lap_times = [0,0,0,0]
    best_lap = 0
    average_Lap = 0

    #Car Events
    BUMPCLOUD = CHECKEREDFLAG + 1
    EXPLOSION = BUMPCLOUD + 1

    def rotate(self, left):
        self.rotating = True
        if left:
            self.angle -= self.rotation_step
        else:
            self.angle += self.rotation_step

        if self.angle < 0:
            self.angle += 16
        if self.angle >= 16:
            self.angle -= 16
        self.sprite_angle = round(self.angle,0)
        if self.sprite_angle == 16:
            self.sprite_angle = 0

    def accelerate(self):
        self.decelerating = False
        if self.speed < self.speed_max:
            self.speed += self.acceleration_step
            if self.speed >= self.speed_max:
                self.max_speed_reached = pygame.time.get_ticks()

    def decelerate(self):
        self.decelerating = True
        self.max_speed_reached = 0
        if self.bumping:
            self.speed -= self.bump_decelaration_step
        else:
            self.speed -= self.deceleration_step

        if self.speed < 0:
            self.speed = 0
        if self.speed == 0:
            self.decelerating = False
            if self.bumping:
                #Stop Bumping routine once speed down to 0
                self.end_bump_loop()

    def search_border_side(self, polygon_border, bumping):
        if bumping:
            self.bumping_diagonal = False
            self.bumping_horizontal = False
            self.bumping_vertical = False
        for i in range(0, len(polygon_border)):
            next_index = i+1
            if next_index == len(polygon_border):
                next_index = 0
            top = 0
            left = 0
            if polygon_border[i][0] <= polygon_border[next_index][0]:
                top = polygon_border[i][0]
            else:
                top = polygon_border[next_index][0]
            if polygon_border[i][1] <= polygon_border[next_index][1]:
                left = polygon_border[i][1]
            else:
                left = polygon_border[next_index][1]

            rect_width = abs(polygon_border[next_index][0]-polygon_border[i][0])
            if rect_width == 0:
                rect_width = 1
            rect_height = abs(polygon_border[next_index][1]-polygon_border[i][1])
            if rect_height == 0:
                rect_height = 1
            wall_rect = pygame.Rect(top, left, rect_width, rect_height)
            #Enlarge detection Box to maximize chance of hitting a polygon side
            sprite_rect = pygame.Rect(self.x_intersect-self.side_detection_tolerance, self.y_intersect-self.side_detection_tolerance, self.side_detection_tolerance*2, self.side_detection_tolerance*2)

            if sprite_rect.colliderect(wall_rect):
                if DEBUG_COLLISION:
                    print('found matching pair of points ({},{})'.format(polygon_border[i],polygon_border[next_index]))
                self.a_intersect_side = polygon_border[i]
                self.b_intersect_side = polygon_border[next_index]
                if (abs(polygon_border[i][0]-polygon_border[next_index][0]) <= self.diagonal_detection_tolerance) and (abs(polygon_border[i][1]-polygon_border[next_index][1]) > self.diagonal_detection_tolerance):
                    if DEBUG_COLLISION:
                        print('x delta <={} - looks vertical enough'.format(self.diagonal_detection_tolerance))
                    if bumping:
                        self.bumping_vertical = True
                    return True
                if (abs(polygon_border[i][0]-polygon_border[next_index][0])>self.diagonal_detection_tolerance) and (abs(polygon_border[i][1]-polygon_border[next_index][1])<=self.diagonal_detection_tolerance):
                    if DEBUG_COLLISION:
                        print('y delta <={} - looks horizontal enough'.format(self.diagonal_detection_tolerance))
                    if bumping:
                        self.bumping_horizontal = True
                    return True
                if DEBUG_COLLISION:
                    print('Diagonal Bumping')
                if bumping:
                    self.bumping_diagonal = True
                    self.bumping_horizontal = False
                    self.bumping_vertical = False
                return True
        return False

    def calculate_vector_from_sprite(self):
        self.sin_angle = math.sin(math.radians(abs(self.sprite_angle*22.5-90)))
        self.y_vector = abs(self.speed * self.sin_angle)
        self.y_vector = self.y_vector * self.angle_vector_sign[self.sprite_angle][1]
        self.x_vector = math.sqrt(self.speed*self.speed-self.y_vector*self.y_vector)
        self.x_vector = self.x_vector * self.angle_vector_sign[self.sprite_angle][0]

    def calculate_skidding_vector(self):
        #Start Skidding - Ignore current Rotation sprite, update speed and use previous Angle and sign
        if not self.y_vector == 0:
            self.y_vector = self.y_vector * abs(self.speed * self.sin_angle) / abs(self.y_vector)

        if not self.x_vector == 0:
            self.x_vector = self.x_vector * math.sqrt(self.speed*self.speed-self.y_vector*self.y_vector)  / abs(self.x_vector)

        if self.x_vector==0 and self.y_vector==0 and self.speed>0:
            #Wrong situation: reset to default vector
            self.calculate_vector_from_sprite()

    def calculate_bumping_vector(self,track):
        if not self.bumping_vector_initialized:
            if self.bumping_vertical:
                #Bump horizontally when hitting a vertical border diagonally or horizontally
                if self.x_vector == 0:
                    #Edge case: bumping into a Vertical wall while car is vertical
                    self.x_vector = self.y_vector
                    intersect_point = self.test_collision(track, True)
                    #Test if the vector is set away or towards the wall, and invert if necessary
                    if intersect_point:
                        self.x_vector = -self.x_vector
                else:
                    #Invert X component fo the vector
                    self.x_vector = -self.x_vector
                self.y_vector = 0
            else:
                if self.bumping_horizontal:
                    #Bump vertically when hitting a horizontal border diagonally or vertically
                    if self.y_vector == 0:
                        #Edge case: bumping into a Horizontal wall while car is horizontal
                        self.y_vector = self.x_vector
                        intersect_point = self.test_collision(track, True)
                        #Test if the vector is set away or towards the wall, and invert if necessary
                        if intersect_point:
                            self.y_vector = -self.y_vector
                    else:
                        #Invert Y component fo the vector
                        self.y_vector = -self.y_vector
                    self.x_vector = 0
                else:
                    if self.bumping_diagonal:
                        #Diagonal Bumping: Bump Diagnoally if hit Horizontally - or Vertically  - Vert or Horiz Bump if hit diagonally
                        a_point = self.a_intersect_side
                        b_point = self.b_intersect_side

                        if self.x_vector == 0 or self.y_vector == 0:
                            #Car is moving Horizontally or Vertical - Force 45 degree angle
                            self.sin_angle = math.sin(math.radians(abs(45)))
                            new_vector = abs(self.speed * self.sin_angle)

                            if (a_point[0] < b_point[0] and a_point[1] < b_point[1]) or (a_point[0] > b_point[0] and a_point[1] > b_point[1]):
                                #Top-Right or Bottom Left Diagonal
                                if self.y_vector > 0 or self.x_vector < 0:
                                    #Bottom Left Diagonal - Invert Y Component
                                    self.x_vector = new_vector
                                    self.y_vector = -new_vector
                                else:
                                    if self.y_vector < 0 or self.x_vector > 0:
                                        #Top Right Diagonal - Invert X Component
                                        self.x_vector = -new_vector
                                        self.y_vector = new_vector

                            if (a_point[0] > b_point[0] and a_point[1] < b_point[1]) or (a_point[0] < b_point[0] and a_point[1] > b_point[1]):
                                #Top-left or Bottom Right Diagonal
                                if self.y_vector < 0 or self.x_vector < 0:
                                    #Top Left Diagonal - No Changes on vector
                                    self.x_vector = new_vector
                                    self.y_vector = new_vector
                                else:
                                    if self.y_vector > 0 or self.x_vector > 0:
                                        #Bottom Right Diagonal - Invert Vector
                                        self.x_vector = -new_vector
                                        self.y_vector = -new_vector
                        else:
                            #Car is Diagonal - Assuming Orthogonal to the Border - Normal Bump - Invert Vector
                            self.x_vector = -self.x_vector
                            self.y_vector = -self.y_vector
                            #Vector Sanity Check
                            #Test if the vector is set away or towards the wall, and Refine direction if not
                            intersect_point = self.test_collision(track, False)
                            if intersect_point:
                                #Reset Vector to initial value
                                self.x_vector = -self.x_vector
                                self.y_vector = -self.y_vector
                                #Default Bump Vector - Max component of Vector
                                new_vector = max(abs(self.x_vector),abs(self.y_vector))
                                #Force the Vector Diagonally if the car is diagonal and "parallel" to the Border
                                if (a_point[0] < b_point[0] and a_point[1] < b_point[1]) or (a_point[0] > b_point[0] and a_point[1] > b_point[1]):
                                    #Top-Right or Bottom Left Diagonal
                                    self.x_vector = new_vector
                                    self.y_vector = -new_vector

                                if (a_point[0] > b_point[0] and a_point[1] < b_point[1]) or (a_point[0] < b_point[0] and a_point[1] > b_point[1]):
                                    #Top-left or Bottom Right Diagonal
                                    self.x_vector = -new_vector
                                    self.y_vector = -new_vector
                    #Vector Sanity Check
                    #Test if the vector is set away or towards the wall, and invert if necessary
                    intersect_point = self.test_collision(track, True)
                    if intersect_point:
                        #Try inverting X
                        self.x_vector = -self.x_vector
                        intersect_point = self.test_collision(track, True)
                        if intersect_point:
                            #Try Inverting Y
                            self.x_vector = -self.x_vector
                            self.y_vector = -self.y_vector
                            intersect_point = self.test_collision(track, True)
                            if intersect_point:
                            #try inverting both
                                self.x_vector = -self.x_vector
                                intersect_point = self.test_collision(track, True)
                                if intersect_point:
                                #No movement as we're stuck
                                    self.y_vector = 0
                                    self.x_vector = 0
        self.bumping_vector_initialized = True

    def test_collision(self, track, simulate_next_step):
        track_mask = pygame.mask.from_surface(track.trackMask, 50)
        car_mask = pygame.mask.from_surface(self.sprites[self.sprite_angle], 50)
        x_test = 0
        y_test = 0
        if simulate_next_step:
            if self.x_vector > 0:
                x_test = self.vector_simulation_length
            else:
                if self.x_vector < 0:
                    x_test = -self.vector_simulation_length
            if self.y_vector > 0:
                y_test = self.vector_simulation_length
            else:
                if self.y_vector < 0:
                    y_test = -self.vector_simulation_length

        return track_mask.overlap(car_mask, ((round(self.x_position+x_test), round(self.y_position+y_test))))

    def calculate_crashing_vector(self,track):
        #Reposition car in a suitable spot - Move car backwards until no collision detected.
        #Invert vector
        self.x_vector = -self.x_vector
        self.y_vector = -self.y_vector

        intersect_point = self.test_collision(track, True)
        #Test if thr car is still collidign and keep moving backwards until not the case
        if intersect_point:
            #No movement as we're stuck
            self.y_vector = 0
            self.x_vector = 0


    def detect_collision(self, track):
        if DEBUG_COLLISION:
            print('Checking for Collision at ({},{})'.format(self.x_position, self.y_position))
        intersect_point = self.test_collision(track,False)
        collision = False
        if intersect_point:
            if not self.decelerating:
                #Check if the car is going into a border a going away from it (i.e. the tail touching the border)
                #If it is going away from the border then skip the Bump routine
                #Simulate  Vector of same direction as current vector and check if still colliding
                intersect_point2 = self.test_collision(track,True)
                if intersect_point2:
                    #Collision confirmed by next incremental move
                    collision = True
                else:
                    #Moving away from wall - Force End Bump routine
                    self.end_bump_loop()
            else:
                collision = True
        if collision:
            if  self.detect_crash(track):
                self.init_crash_loop(track, intersect_point)
            else:
                self.init_bump_loop(track, intersect_point)

    def detect_crash(self, track):
        if self.max_speed_reached > 0:
            maxspeed_duration = pygame.time.get_ticks() - self.max_speed_reached
            #More than xxx ms at max_speed when coliding is a certain crash
            if maxspeed_duration <= self.max_speed_crash_threshold:
                return False
            else:
                return True
        else:
            #There is a random chance to Crash, increased:
            crash_probability = random.randint(1,self.crash_random_max)
            #1- If Speed is higher than xx% of max speed
            if self.speed >= self.speed_crash_probability_threshold * self.speed_max:
                crash_probability = crash_probability * self.speed_crash_probability_penalty
            #2- If A sensitive Border has been hit
            if self.search_border_side(track.external_borders, False) or self.search_border_side(track.internal_borders, False):
                if self.a_intersect_side[2] == 1 and self.b_intersect_side[2] == 1:
                    crash_probability = crash_probability * self.sensitive_border_crash_probability_penalty
            if crash_probability > self.crash_certainty_treshold:
                return True
            else:
                return False


    def init_bump_loop(self, track, intersect_point):
        self.bumping = True
        self.speed = self.bump_speed
        #Determine the agle at which angle the car is intersecting with the Border: either right angle or not
        #Lookup in the map for the closest intersection point and the polygon side that is intersecting
        self.x_intersect = intersect_point[0]
        self.y_intersect = intersect_point[1]
        self.collision_time = pygame.time.get_ticks()
        #Search external borders other corners of the sprite in case no border poinst detected
        if not self.search_border_side(track.external_borders, True):
            if not self.search_border_side(track.internal_borders, True):
                #Despite overlap detected no intersection with any side of the Track polygons has been found
                #Unable to determine the orientation of the colliding border
                if DEBUG_BUMP:
                    print('No Macthing Border Side found')
                self.end_bump_loop()
        if DEBUG_BUMP:
            print('{} - Bump Initiated({},{})'.format(self.collision_time, self.x_intersect, self.y_intersect))
        self.animation_index = 0
        pygame.time.set_timer(self.BUMPCLOUD, self.bump_animation_timer)

    def init_crash_loop(self, track, intersect_point):
        self.crashing = True
        self.crash_finished = False
        self.speed = 0
        self.x_intersect = intersect_point[0]
        self.y_intersect = intersect_point[1]
        self.helicopter_x = - helicopter_frames[0].get_width()
        self.helicopter_y = self.y_intersect - helicopter_frames[0].get_height()
        self.collision_time = pygame.time.get_ticks()
        print('{} - Crash Initiated({},{})'.format(self.collision_time, self.x_intersect, self.y_intersect))
        self.animation_index = 0
        self.helicopter_index = 0
        pygame.time.set_timer(self.EXPLOSION, self.crash_animation_timer)

    def end_bump_loop(self):
        self.bumping_diagonal = False
        self.bumping_horizontal = False
        self.bumping_vertical = False
        self.bumping_vector_initialized = False
        self.bumping = False
        end_time = pygame.time.get_ticks()
        if DEBUG_BUMP:
            print('{} - Bump Terminated - Duration: {})'.format(end_time,end_time-self.collision_time))
        pygame.time.set_timer(self.BUMPCLOUD,0)

    def end_crash_loop(self):
        self.crashing = False
        self.crash_finished = False
        end_time = pygame.time.get_ticks()
        if DEBUG_CRASH:
            print('{} - Crash Terminated - Duration: {})'.format(end_time,end_time-self.collision_time))
        pygame.time.set_timer(self.EXPLOSION,0)


    def update_position(self, track):
        if self.crashing:
            self.calculate_crashing_vector(track)
        else:
            if not self.decelerating:
                #Calculate Vector - Accelarating means No skidding
                self.calculate_vector_from_sprite()
            else:
                if not self.rotating:
                    #Calculate Vector - Skidding
                    self.calculate_skidding_vector()
            if self.bumping:
                #Calculate Vector - Bumping
                self.calculate_bumping_vector(track)

        #Update Car Offset
        self.x_position += self.x_vector
        self.y_position += self.y_vector

        if not self.crashing:
            #Reset Rotation Flag to match Key Pressed Status
            self.rotating = False
            #If the car is not stopped Detect Track Borders. If not let it rotate over the edges & ignore collisions
            if self.speed > 0:
                self.detect_collision(track)
            else:
                if self.bumping:
                    #Force end of Bump Routine if car is not moving
                    self.end_bump_loop()
        else:
            #Car is not moving anymore
            self.x_vector = 0
            self.y_vector = 0
            self.speed = 0
            #End Crash Routine if animation has run to the end.
            if self.crash_finished:
                self.end_crash_loop()

    def test_finish_line(self, track):
        #Detect if car collides with Finish line in the expected direction
        sprite_rect = pygame.Rect(self.x_position, self.y_position, self.sprites[self.sprite_angle].get_width(), self.sprites[self.sprite_angle].get_height())
        if sprite_rect.colliderect(track.finish_line):
            if not self.on_finish_line:
                self.on_finish_line = True
                if self.x_vector * track.finish_line_direction > 0:
                    if self.passed_finish_line_wrong_way:
                        self.passed_finish_line_wrong_way = False
                        if DEBUG_FINISH:
                            print('{} - Passed the line in the right direction after going the wrong way)'.format(pygame.time.get_ticks()))
                    else:
                        finish_time = pygame.time.get_ticks()
                        self.lap_times[self.lap_count] = finish_time - self.current_lap_start
                        if DEBUG_FINISH:
                            print('{} - New Lap {} - Duration: {})'.format(finish_time, self.lap_count, self.lap_times[self.lap_count]))
                        self.lap_count+=1
                        if self.lap_count == race_laps:
                            #Race finished
                            self.average_Lap =  sum(self.lap_times)/race_laps
                            self.best_lap = min(self.lap_times)
                            if DEBUG_FINISH:
                                print('{} - Race Finished - Duration: {} - Average lap: {} - Best Lap: {})'.format(finish_time, sum(self.lap_times), self.average_Lap, self.best_lap))
                            return True
                        self.current_lap_start = finish_time
                        return False
                else:
                    self.passed_finish_line_wrong_way = True
                    if DEBUG_FINISH:
                        print('{} - Passed the line in the wrong direction)'.format(pygame.time.get_ticks()))
        else:
            self.on_finish_line = False


    def draw(self, track):
        #Draw Car
        if not self.bumping:
            self.update_position(track)
        if self.bumping:
            #Ignore controls until Buming routine is finished - Force Skidding & Decelaration
            self.decelerating = True
            self.rotating = False
            self.update_position(track)

    def blit(self, track):
        #Car is not visible durign explosion
        if not self.crashing:
            game_display.blit(self.sprites[self.sprite_angle], (self.x_position, self.y_position))
        #Blit Dust Cloud if Bumping
        if self.bumping:
            if DEBUG_BUMP:
                print('{} - Blit Bump Frame - Index: {}'.format(pygame.time.get_ticks(), self.animation_index))
            if self.animation_index <= 4:
                game_display.blit(dust_cloud_frames[self.animation_index], (self.x_intersect, self.y_intersect))
        #Blit Explosion & Helicopter
        if self.crashing:
            if self.animation_index <= 4:
                game_display.blit(explosion_frames[self.animation_index], (self.x_intersect, self.y_intersect))
            if self.helicopter_x >= self.x_position:
                game_display.blit(self.sprites[self.sprite_angle], (self.x_position, self.y_position))
            game_display.blit(helicopter_frames[self.helicopter_index], (self.helicopter_x, self.helicopter_y))


    def display_bump_cloud(self):
        if DEBUG_BUMP:
            print('{} - Increment Bump Frame'.format(pygame.time.get_ticks()))
        if self.animation_index < len(dust_cloud_frames):
            self.animation_index += 1

    def display_explosion(self):
        if DEBUG_CRASH:
            print('{} - Blit Crash Frame - Index: {}'.format(pygame.time.get_ticks(), self.animation_index))
        if self.animation_index < len(explosion_frames):
            self.animation_index += 1
        if self.helicopter_x < display_width:
            self.helicopter_x += helicopter_step
            if self.helicopter_index == len(helicopter_frames)-1:
                self.helicopter_index = 0
            else:
                self.helicopter_index += 1
        else:
            self.crash_finished = True

def display_loading_screen(loop):
    screen_fadein(loading_screen)
    screen_exit = False
    scroll_message = "SUPER SPRINT REMADE WITH PYGAME BY SALEM_OK. CREATED FOR THE MIGHTY ATARI ST BY STATE OF THE ART. PROGRAMMING: NALIN SHARMA  MARTIN GREEN  JON STEELE. GRAPHICS: CHRIS GIBBS. SOUND: MARK TISDALE. A SOFTWARE STUDIOS PRODUCTION..."
    right_end = 490
    left_end = 148
    scroll_y = 370
    background = pygame.Surface((display_width,display_height))
    background.fill(black_color)
    text = pygame.Surface(((scrolling_font['A'].get_width() + 1) * len(scroll_message) + right_end - left_end, scrolling_font['A'].get_height()))
    x_offset = right_end - left_end
    for char in scroll_message:
        text.blit(scrolling_font[char], (x_offset, 0))
        x_offset += scrolling_font[char].get_width() + 1

    while not screen_exit:
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                screen_exit = True
        game_display.blit(background, (0, 0))
        game_display.blit(text, (left_end, scroll_y))
        game_display.blit(loading_screen_foreground, (0, 0))
        pygame.display.update()
        text.scroll(-3)
        clock.tick(FPS)
    screen_fadeout()

def display_credits_screen():
    screen_exit = False
    screen_fadein(credits_screen)
    pygame.display.update()
    while not screen_exit:
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                screen_exit = True
    screen_fadeout()

def print_press_acceltoplay(top_left, color, seconds):
    game_display.blit(small_font.render("PRESS", False, color), top_left)
    game_display.blit(small_font.render("ACCELERATE", False, color), (top_left[0] - 28, top_left[1] + 20))
    game_display.blit(small_font.render("TO PLAY".format(seconds), False, color), (top_left[0] - 10, top_left[1] + 40))
    game_display.blit(small_font.render("{}".format(seconds), False, color), (top_left[0] + 24, top_left[1] + 60))

def print_start_race_text(seconds):
    print_press_acceltoplay((77,6), blue_color, seconds)
    print_press_acceltoplay((291,6), red_color, seconds)
    print_press_acceltoplay((505,6), yellow_color, seconds)
    game_display.blit(small_font.render("PRESS SPACE TO SKIP", False, white_color), (240,384))

def display_start_race_screen():
    seconds = 5
    screen_exit = False
    screen_fadein(start_race_screen)
    print_start_race_text(seconds)
    pygame.display.update()
    countdown = pygame.time.get_ticks()
    while not screen_exit:
        time = pygame.time.get_ticks()
        if time - countdown >= 1000:
            seconds -= 1
            countdown = time
            game_display.blit(start_race_screen, (0, 0))
            print_start_race_text(seconds)
            pygame.display.update()
        if seconds == 0:
            screen_exit = True
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    screen_exit = True
    screen_fadeout()


def display_splash_screen():
    screen_exit = False
    screen_fadein(splash_screen)
    pygame.display.update()
    while not screen_exit:
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                screen_exit = True
    screen_fadeout()

def screen_fadeout():
    for frame in range (0,len(transition_dots)):
        for i in range (0,40):
            for j in  range (0,24):
                game_display.blit(transition_dots[frame], (i * 16, j *17))
        pygame.display.update()
        clock.tick(len(transition_dots)*1.5)


def screen_fadein(screen):
    frame = len(transition_dots)
    while frame > 0:
        game_display.blit(screen, (0, 0))
        for i in range (0,40):
            for j in  range (0,24):
                game_display.blit(transition_dots[frame-1], (i * 16, j *17))
        pygame.display.update()
        clock.tick(len(transition_dots)*1.5)
        frame -= 1

def trace_frame_time(trace_event, frame_start):
    if DEBUG_FPS:
        print('{} - Duration: {}'.format(trace_event, pygame.time.get_ticks() - frame_start))


def game_loop():

    display_loading_screen(False)
    display_splash_screen()
    display_credits_screen()
    display_start_race_screen()

    blue_car = Car()
    track1 = Track()
    screen_fadein(track1.background)

    game_exit = False
    race_start = True
    last_lap = False
    race_finish = False
    animation_index = 0
    flag_waves = 0
    wave_up = True
    flag_waved = False
    pygame.time.set_timer(GREENFLAG, 40)
    while not game_exit:
        frame_start = pygame.time.get_ticks()
        trace_frame_time("Frame start", frame_start)
        if pygame.key.get_pressed()[pygame.K_ESCAPE]:
            game_exit = True
        else:
            ignore_controls = False
            if blue_car.bumping or race_finish:
                ignore_controls = True
            if not ignore_controls:
                if pygame.key.get_pressed()[pygame.K_RCTRL]:
                    blue_car.accelerate()
                else:
                    blue_car.decelerate()

                if pygame.key.get_pressed()[pygame.K_LEFT]:
                    blue_car.rotate(True)

                if pygame.key.get_pressed()[pygame.K_RIGHT]:
                    blue_car.rotate(False)
            else:
                blue_car.decelerate()
            trace_frame_time("Checked Key input", frame_start)
            for event in pygame.event.get():
                if not ignore_controls:
                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_RCTRL:
                            blue_car.accelerate()
                        if event.key == pygame.K_LEFT:
                            blue_car.rotate(True)
                        if event.key == pygame.K_RIGHT:
                            blue_car.rotate(False)
                else:
                    blue_car.decelerate()
                #Draw Dust Cloud
                if event.type == blue_car.BUMPCLOUD:
                    if DEBUG_BUMP:
                        print('{} - Bump Timer triggerred'.format(pygame.time.get_ticks()))
                    if blue_car.bumping:
                        blue_car.display_bump_cloud()
                #Draw Explosion
                if event.type == blue_car.EXPLOSION:
                    if DEBUG_CRASH:
                        print('{} - Crash Timer triggerred'.format(pygame.time.get_ticks()))
                    if blue_car.crashing:
                        blue_car.display_explosion()
                #Draw Green Flag at Race Start
                if event.type == GREENFLAG:
                    if DEBUG_FLAG:
                        print('{} - Green Flag Timer triggerred'.format(pygame.time.get_ticks()))
                    if wave_up:
                        animation_index += 1
                    else:
                        animation_index -= 1
                    if animation_index >= len(green_flag_frames):
                        animation_index -= 1
                        flag_waves += 1
                        wave_up = False

                    if animation_index < 0:
                        animation_index += 1
                        wave_up = True

                    if flag_waves > 5:
                        race_start = False
                        pygame.time.set_timer(GREENFLAG, 00)

                #Draw White Flag for Last lap
                if event.type == WHITEFLAG:
                    if DEBUG_FLAG:
                        print('{} - White Flag Timer triggerred'.format(pygame.time.get_ticks()))
                    if wave_up:
                        animation_index += 1
                    else:
                        animation_index -= 1
                    if animation_index >= len(white_flag_frames):
                        animation_index -= 1
                        flag_waves += 1
                        wave_up = False

                    if animation_index < 0:
                        animation_index += 1
                        wave_up = True

                    if flag_waves > 5:
                        flag_waved = True
                        pygame.time.set_timer(WHITEFLAG, 00)

                #Draw Checkered Flag
                if event.type == CHECKEREDFLAG:
                    if DEBUG_FLAG:
                        print('{} - Checkered Flag Timer triggerred'.format(pygame.time.get_ticks()))
                    if wave_up:
                        animation_index += 1
                    else:
                        animation_index -= 1
                    if animation_index >= len(checkered_flag_frames):
                        animation_index -= 1
                        flag_waves += 1
                        wave_up = False

                    if animation_index < 0:
                        animation_index += 1
                        wave_up = True

                    if flag_waves > 5:
                        flag_waved = True
                        pygame.time.set_timer(CHECKEREDFLAG, 00)

            trace_frame_time("Managed all Events", frame_start)

            blue_car.draw(track1)
            trace_frame_time("Drawn car", frame_start)
            if not race_finish:
                race_finish = blue_car.test_finish_line(track1)
                #Draw Checkered Flag and finish race
                if race_finish:
                    animation_index = 0
                    flag_waves = 0
                    flag_waved = False
                    wave_up = True
                    blue_car.speed = 0
                    pygame.time.set_timer(CHECKEREDFLAG, 40)


            #Draw White Flag for Last lap
            if not last_lap and blue_car.lap_count == race_laps -1:
                animation_index = 0
                flag_waves = 0
                wave_up = True
                last_lap = True
                pygame.time.set_timer(WHITEFLAG, 40)

            trace_frame_time("Test Finish ", frame_start)
            game_display.blit(track1.background, (0, 0))
            if race_start:
                game_display.blit(green_flag_frames[animation_index],track1.flag_anchor)

            if last_lap and not flag_waved:
                game_display.blit(white_flag_frames[animation_index],track1.flag_anchor)

            if race_finish and not flag_waved:
                game_display.blit(checkered_flag_frames[animation_index],track1.flag_anchor)

            blue_car.blit(track1)
            pygame.display.update()
            trace_frame_time("Display Updated ", frame_start)
            if race_finish and flag_waved:
                game_exit = True
            frame_duration = pygame.time.get_ticks() - frame_start
            current_fps = round(1000/frame_duration)
            if DEBUG_FPS:
                print(' Frame: {} - {} FPS'.format(frame_duration, current_fps))
            clock.tick(FPS)
    screen_fadeout()
game_loop()
