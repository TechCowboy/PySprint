import numpy as np
from PIL import Image

red_color = (238, 0, 34) #EE0022
blue_color = (68, 102, 238) # 4466EE
yellow_color = (238, 238, 102)  #EEEE66
green_color = (34, 170, 102) #22AA66
green_secondary_color = (170, 204, 102) #AACC66
blue_secondary_color = (170, 204, 238) #AACCEE
red_secondary_color = (170, 0, 0) #AA0000
yellow_secondary_color = (170, 170, 0) #AAAA00
yellow_tertiary_color = (238, 204, 102) #EECC66



#Yellow HElicopter Horizontal

for i in range(0,4):
    im = Image.open('Assets/BlueHelicopter{}.png'.format(i))
    data = np.array(im)

    r1, g1, b1 = 68, 102, 238 # Original value
    r2, g2, b2 = 238, 238, 102 # Value that we want to replace it with

    red, green, blue = data[:,:,0], data[:,:,1], data[:,:,2]
    mask = (red == r1) & (green == g1) & (blue == b1)
    data[:,:,:3][mask] = [r2, g2, b2]

    im = Image.fromarray(data)

    data = np.array(im)

    r1, g1, b1 = 170, 204, 238 # Original value
    r2, g2, b2 = 170, 170, 0 # Value that we want to replace it with

    red, green, blue = data[:,:,0], data[:,:,1], data[:,:,2]
    mask = (red == r1) & (green == g1) & (blue == b1)
    data[:,:,:3][mask] = [r2, g2, b2]

    im = Image.fromarray(data)

    im.save('Assets/YellowHelicopter{}.png'.format(i))



#RED HElicopter Horizontal

for i in range(0,4):
    im = Image.open('Assets/BlueHelicopter{}.png'.format(i))
    data = np.array(im)

    r1, g1, b1 = 68, 102, 238 # Original value
    r2, g2, b2 = 238, 0, 34 # Value that we want to replace it with

    red, green, blue = data[:,:,0], data[:,:,1], data[:,:,2]
    mask = (red == r1) & (green == g1) & (blue == b1)
    data[:,:,:3][mask] = [r2, g2, b2]

    im = Image.fromarray(data)

    data = np.array(im)

    r1, g1, b1 = 170, 204, 238 # Original value
    r2, g2, b2 = 170, 0, 0 # Value that we want to replace it with

    red, green, blue = data[:,:,0], data[:,:,1], data[:,:,2]
    mask = (red == r1) & (green == g1) & (blue == b1)
    data[:,:,:3][mask] = [r2, g2, b2]

    im = Image.fromarray(data)

    im.save('Assets/RedHelicopter{}.png'.format(i))



#GREEN HElicopter Horizontal

for i in range(0,4):
    im = Image.open('Assets/BlueHelicopter{}.png'.format(i))
    data = np.array(im)

    r1, g1, b1 = 68, 102, 238 # Original value
    r2, g2, b2 = 34, 170, 102 # Value that we want to replace it with

    red, green, blue = data[:,:,0], data[:,:,1], data[:,:,2]
    mask = (red == r1) & (green == g1) & (blue == b1)
    data[:,:,:3][mask] = [r2, g2, b2]

    im = Image.fromarray(data)

    data = np.array(im)

    r1, g1, b1 = 170, 204, 238 # Original value
    r2, g2, b2 = 170, 204, 102 # Value that we want to replace it with

    red, green, blue = data[:,:,0], data[:,:,1], data[:,:,2]
    mask = (red == r1) & (green == g1) & (blue == b1)
    data[:,:,:3][mask] = [r2, g2, b2]

    im = Image.fromarray(data)

    im.save('Assets/GreenHelicopter{}.png'.format(i))





#GREEN HElicopter

# for i in range(0,4):
#     im = Image.open('Assets/YellowHelicopterV{}.png'.format(i))
#     data = np.array(im)

#     r1, g1, b1 = 238, 238, 102 # Original value
#     r2, g2, b2 = 170, 204, 102 # Value that we want to replace it with

#     red, green, blue = data[:,:,0], data[:,:,1], data[:,:,2]
#     mask = (red == r1) & (green == g1) & (blue == b1)
#     data[:,:,:3][mask] = [r2, g2, b2]

#     im = Image.fromarray(data)

#     data = np.array(im)

#     r1, g1, b1 = 170, 170, 0 # Original value
#     r2, g2, b2 = 34, 170, 102 # Value that we want to replace it with

#     red, green, blue = data[:,:,0], data[:,:,1], data[:,:,2]
#     mask = (red == r1) & (green == g1) & (blue == b1)
#     data[:,:,:3][mask] = [r2, g2, b2]

#     im = Image.fromarray(data)


#     im.save('Assets/GreenHelicopterV{}.png'.format(i))



# # #RED HElicopter

# for i in range(0,4):
#     im = Image.open('Assets/YellowHelicopterV{}.png'.format(i))
#     data = np.array(im)

#     r1, g1, b1 = 238, 238, 102 # Original value
#     r2, g2, b2 = 238, 0, 34 # Value that we want to replace it with

#     red, green, blue = data[:,:,0], data[:,:,1], data[:,:,2]
#     mask = (red == r1) & (green == g1) & (blue == b1)
#     data[:,:,:3][mask] = [r2, g2, b2]

#     im = Image.fromarray(data)

#     data = np.array(im)

#     r1, g1, b1 = 170, 170, 0 # Original value
#     r2, g2, b2 = 170, 0, 0 # Value that we want to replace it with

#     red, green, blue = data[:,:,0], data[:,:,1], data[:,:,2]
#     mask = (red == r1) & (green == g1) & (blue == b1)
#     data[:,:,:3][mask] = [r2, g2, b2]

#     im = Image.fromarray(data)


#     im.save('Assets/RedHelicopterV{}.png'.format(i))




# #BLUE HElicopter

# for i in range(0,4):
#     im = Image.open('Assets/YellowHelicopterV{}.png'.format(i))
#     data = np.array(im)

#     r1, g1, b1 = 238, 238, 102 # Original value
#     r2, g2, b2 = 170, 204, 238 # Value that we want to replace it with

#     red, green, blue = data[:,:,0], data[:,:,1], data[:,:,2]
#     mask = (red == r1) & (green == g1) & (blue == b1)
#     data[:,:,:3][mask] = [r2, g2, b2]

#     im = Image.fromarray(data)

#     data = np.array(im)

#     r1, g1, b1 = 170, 170, 0 # Original value
#     r2, g2, b2 = 68, 102, 238 # Value that we want to replace it with

#     red, green, blue = data[:,:,0], data[:,:,1], data[:,:,2]
#     mask = (red == r1) & (green == g1) & (blue == b1)
#     data[:,:,:3][mask] = [r2, g2, b2]

#     im = Image.fromarray(data)


#     im.save('Assets/BlueHelicopterV{}.png'.format(i))



# im = Image.open('Assets/SuperSprintRacePodiumFourthCarGreenCarDrone.png')
# data = np.array(im)

# r1, g1, b1 = 238, 238, 0 # Original value
# r2, g2, b2 = 136, 136, 136 # Value that we want to replace it with

# red, green, blue = data[:,:,0], data[:,:,1], data[:,:,2]
# mask = (red == r1) & (green == g1) & (blue == b1)
# data[:,:,:3][mask] = [r2, g2, b2]
# im = Image.fromarray(data)
# im.save('Assets/SuperSprintRacePodiumFourthCarGreenCarDrone.png')

# im = Image.open('Assets/SuperSprintRacePodiumFourthCarGreenCarDrone.png')
# data = np.array(im)

# r1, g1, b1 = 136, 136, 136 # Original value
# r2, g2, b2 = 34, 170, 102 # Value that we want to replace it with

# red, green, blue = data[:,:,0], data[:,:,1], data[:,:,2]
# mask = (red == r1) & (green == g1) & (blue == b1)
# data[:,:,:3][mask] = [r2, g2, b2]

# im = Image.fromarray(data)
# im.save('Assets/SuperSprintRacePodiumFourthCarGreenCar.png')


# #BLUE CARS

# im = Image.open('Assets/SuperSprintRacePodiumFourthCarYellowCar.png')
# data = np.array(im)

# r1, g1, b1 = 238, 204, 102 # Original value
# r2, g2, b2 = 170, 204, 238 # Value that we want to replace it with

# red, green, blue = data[:,:,0], data[:,:,1], data[:,:,2]
# mask = (red == r1) & (green == g1) & (blue == b1)
# data[:,:,:3][mask] = [r2, g2, b2]

# im = Image.fromarray(data)

# data = np.array(im)

# r1, g1, b1 = 238, 238, 0 # Original value
# r2, g2, b2 = 136, 136, 136 # Value that we want to replace it with

# red, green, blue = data[:,:,0], data[:,:,1], data[:,:,2]
# mask = (red == r1) & (green == g1) & (blue == b1)
# data[:,:,:3][mask] = [r2, g2, b2]
# im = Image.fromarray(data)

# r1, g1, b1 = 170, 136, 0 # Original value
# r2, g2, b2 = 102, 102, 102 # Value that we want to replace it with

# red, green, blue = data[:,:,0], data[:,:,1], data[:,:,2]
# mask = (red == r1) & (green == g1) & (blue == b1)
# data[:,:,:3][mask] = [r2, g2, b2]

# im = Image.fromarray(data)

# im.save('Assets/SuperSprintRacePodiumFourthCarBlueCarDrone.png')

# im = Image.open('Assets/SuperSprintRacePodiumFourthCarBlueCarDrone.png')
# data = np.array(im)

# r1, g1, b1 = 136, 136, 136 # Original value
# r2, g2, b2 = 68, 102, 238 # Value that we want to replace it with

# red, green, blue = data[:,:,0], data[:,:,1], data[:,:,2]
# mask = (red == r1) & (green == g1) & (blue == b1)
# data[:,:,:3][mask] = [r2, g2, b2]

# im = Image.fromarray(data)
# im.save('Assets/SuperSprintRacePodiumFourthCarBlueCar.png')

# #RED CARS
# im = Image.open('Assets/SuperSprintRacePodiumFourthCarYellowCar.png')
# data = np.array(im)

# r1, g1, b1 = 238, 204, 102 # Original value
# r2, g2, b2 = 170, 0, 0 # Value that we want to replace it with

# red, green, blue = data[:,:,0], data[:,:,1], data[:,:,2]
# mask = (red == r1) & (green == g1) & (blue == b1)
# data[:,:,:3][mask] = [r2, g2, b2]

# im = Image.fromarray(data)

# data = np.array(im)

# r1, g1, b1 = 238, 238, 0 # Original value
# r2, g2, b2 = 136, 136, 136 # Value that we want to replace it with

# red, green, blue = data[:,:,0], data[:,:,1], data[:,:,2]
# mask = (red == r1) & (green == g1) & (blue == b1)
# data[:,:,:3][mask] = [r2, g2, b2]
# im = Image.fromarray(data)

# r1, g1, b1 = 170, 136, 0 # Original value
# r2, g2, b2 = 102, 102, 102 # Value that we want to replace it with

# red, green, blue = data[:,:,0], data[:,:,1], data[:,:,2]
# mask = (red == r1) & (green == g1) & (blue == b1)
# data[:,:,:3][mask] = [r2, g2, b2]

# im = Image.fromarray(data)

# im.save('Assets/SuperSprintRacePodiumFourthCarRedCarDrone.png')

# im = Image.open('Assets/SuperSprintRacePodiumFourthCarRedCarDrone.png')
# data = np.array(im)

# r1, g1, b1 = 136, 136, 136 # Original value
# r2, g2, b2 = 238, 0, 34 # Value that we want to replace it with

# red, green, blue = data[:,:,0], data[:,:,1], data[:,:,2]
# mask = (red == r1) & (green == g1) & (blue == b1)
# data[:,:,:3][mask] = [r2, g2, b2]

# im = Image.fromarray(data)
# im.save('Assets/SuperSprintRacePodiumFourthCarRedCar.png')


# #YELLOW CARS
# im = Image.open('Assets/SuperSprintRacePodiumFourthCarYellowCar.png')
# data = np.array(im)

# r1, g1, b1 = 238, 238, 0 # Original value
# r2, g2, b2 = 136, 136, 136 # Value that we want to replace it with

# red, green, blue = data[:,:,0], data[:,:,1], data[:,:,2]
# mask = (red == r1) & (green == g1) & (blue == b1)
# data[:,:,:3][mask] = [r2, g2, b2]

# im = Image.fromarray(data)

# r1, g1, b1 = 170, 136, 0 # Original value
# r2, g2, b2 = 102, 102, 102 # Value that we want to replace it with

# red, green, blue = data[:,:,0], data[:,:,1], data[:,:,2]
# mask = (red == r1) & (green == g1) & (blue == b1)
# data[:,:,:3][mask] = [r2, g2, b2]

# im = Image.fromarray(data)

# im.save('Assets/SuperSprintRacePodiumFourthCarYellowCarDrone.png')

# im = Image.open('Assets/SuperSprintRacePodiumSecondCarYellowCarDrone.png')
# data = np.array(im)

# r1, g1, b1 = 136, 136, 136 # Original value
# r2, g2, b2 = 238, 238, 102 # Value that we want to replace it with

# red, green, blue = data[:,:,0], data[:,:,1], data[:,:,2]
# mask = (red == r1) & (green == g1) & (blue == b1)
# data[:,:,:3][mask] = [r2, g2, b2]

# im = Image.fromarray(data)
# im.save('Assets/SuperSprintRacePodiumSecondCarYellowCar.png')


# #THIRD CAR


# #GREEN CARS

# im = Image.open('Assets/SuperSprintRacePodiumThirdCarBlueCarDrone.png')
# data = np.array(im)

# r1, g1, b1 = 170, 204, 238 # Original value
# r2, g2, b2 = 170, 204, 102 # Value that we want to replace it with

# red, green, blue = data[:,:,0], data[:,:,1], data[:,:,2]
# mask = (red == r1) & (green == g1) & (blue == b1)
# data[:,:,:3][mask] = [r2, g2, b2]

# im = Image.fromarray(data)
# im.save('Assets/SuperSprintRacePodiumThirdCarGreenCarDrone.png')

# im = Image.open('Assets/SuperSprintRacePodiumThirdCarGreenCarDrone.png')
# data = np.array(im)

# r1, g1, b1 = 136, 136, 136 # Original value
# r2, g2, b2 = 34, 170, 102 # Value that we want to replace it with

# red, green, blue = data[:,:,0], data[:,:,1], data[:,:,2]
# mask = (red == r1) & (green == g1) & (blue == b1)
# data[:,:,:3][mask] = [r2, g2, b2]

# im = Image.fromarray(data)
# im.save('Assets/SuperSprintRacePodiumThirdCarGreenCar.png')


# #BLUE CARS

# # im = Image.open('Assets/SuperSprintRacePodiumThirdCarBlueCarDrone.png')
# # data = np.array(im)

# # r1, g1, b1 = 170, 204, 238 # Original value
# # r2, g2, b2 = 170, 204, 238 # Value that we want to replace it with

# # red, green, blue = data[:,:,0], data[:,:,1], data[:,:,2]
# # mask = (red == r1) & (green == g1) & (blue == b1)
# # data[:,:,:3][mask] = [r2, g2, b2]

# # im = Image.fromarray(data)
# # im.save('Assets/SuperSprintRacePodiumSecondCarBlueCarDrone.png')

# im = Image.open('Assets/SuperSprintRacePodiumThirdCarBlueCarDrone.png')
# data = np.array(im)

# r1, g1, b1 = 136, 136, 136 # Original value
# r2, g2, b2 = 68, 102, 238 # Value that we want to replace it with

# red, green, blue = data[:,:,0], data[:,:,1], data[:,:,2]
# mask = (red == r1) & (green == g1) & (blue == b1)
# data[:,:,:3][mask] = [r2, g2, b2]

# im = Image.fromarray(data)
# im.save('Assets/SuperSprintRacePodiumThirdCarBlueCar.png')

# #RED CARS
# im = Image.open('Assets/SuperSprintRacePodiumThirdCarBlueCarDrone.png')
# data = np.array(im)

# r1, g1, b1 = 170, 204, 238 # Original value
# r2, g2, b2 = 170, 0, 0 # Value that we want to replace it with

# red, green, blue = data[:,:,0], data[:,:,1], data[:,:,2]
# mask = (red == r1) & (green == g1) & (blue == b1)
# data[:,:,:3][mask] = [r2, g2, b2]

# im = Image.fromarray(data)
# im.save('Assets/SuperSprintRacePodiumThirdCarRedCarDrone.png')

# im = Image.open('Assets/SuperSprintRacePodiumThirdCarRedCarDrone.png')
# data = np.array(im)

# r1, g1, b1 = 136, 136, 136 # Original value
# r2, g2, b2 = 238, 0, 34 # Value that we want to replace it with

# red, green, blue = data[:,:,0], data[:,:,1], data[:,:,2]
# mask = (red == r1) & (green == g1) & (blue == b1)
# data[:,:,:3][mask] = [r2, g2, b2]

# im = Image.fromarray(data)
# im.save('Assets/SuperSprintRacePodiumThirdCarRedCar.png')


# #YELLOW CARS
# im = Image.open('Assets/SuperSprintRacePodiumThirdCarBlueCarDrone.png')
# data = np.array(im)

# r1, g1, b1 = 170, 204, 238 # Original value
# r2, g2, b2 = 170, 170, 0 # Value that we want to replace it with

# red, green, blue = data[:,:,0], data[:,:,1], data[:,:,2]
# mask = (red == r1) & (green == g1) & (blue == b1)
# data[:,:,:3][mask] = [r2, g2, b2]

# im = Image.fromarray(data)
# im.save('Assets/SuperSprintRacePodiumThirdCarYellowCarDrone.png')

# im = Image.open('Assets/SuperSprintRacePodiumThirdCarYellowCarDrone.png')
# data = np.array(im)

# r1, g1, b1 = 136, 136, 136 # Original value
# r2, g2, b2 = 238, 238, 102 # Value that we want to replace it with

# red, green, blue = data[:,:,0], data[:,:,1], data[:,:,2]
# mask = (red == r1) & (green == g1) & (blue == b1)
# data[:,:,:3][mask] = [r2, g2, b2]

# im = Image.fromarray(data)
# im.save('Assets/SuperSprintRacePodiumThirdCarYellowCar.png')