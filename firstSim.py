
import numpy as np
import time
import numpy as np
import matplotlib.pyplot as plt
import math as m



def updatePositions(POSITIONS, HEADINGS, SPEED):
    # each individual moves in the direction its heading by an amount determined by SPEED
    # x coordinates are changed by cos(HEADING) while y coordinates sin(HEADING)
    POSITIONS = POSITIONS + np.hstack((np.cos(HEADINGS)*SPEED, np.sin(HEADINGS)*SPEED))

    # next we wrap the positions so if a sheep goes off the edge of the field he reappears at the other side
    POSITIONS[POSITIONS<0]=POSITIONS[POSITIONS<0]+1
    POSITIONS[POSITIONS>1]=POSITIONS[POSITIONS>1]-1

    return POSITIONS




# setup figure for showing positions
fig = plt.figure()
ax = fig.add_subplot(111)


TIMESTEPS = 100 # how long to run the simulation
SHEEP = 100 # how many individuals to simulate


POSITIONS = np.zeros((SHEEP,2)).astype(np.float64)  # each individual has a location stored as an x-y coordinate
HEADINGS = m.pi*np.ones((SHEEP,1)).astype(np.float64) # each individual has a direction that its moving, this is an angle that will be between 0 and 2pi 
SPEED = 0.01*np.ones((SHEEP,1)).astype(np.float64) # each individual has a speed which we'll make quite small as the area is only 1x1


# set initial positions of the sheep to a random location
POSITIONS = np.random.uniform(size=POSITIONS.shape)

for t in range(TIMESTEPS):
    # everybody moves a little bit at each time step
    POSITIONS = updatePositions(POSITIONS,HEADINGS,SPEED)

    # plot the sheep
    ax.clear()
    ax.axis([0, 1, 0, 1])
    ax.scatter(POSITIONS[:,0],POSITIONS[:,1])
    plt.pause(0.1)
