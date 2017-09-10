import matplotlib.pyplot as plt
from matplotlib.widgets import Button
import math
import position
import IK
from random import randint

l1 = 350  # starting length of link1
l2 = 350  # starting length of link2
beamLength = 500
hatLength = 100

# link 1 starting coordinates
link1startX = 0
link1startY = 0

# link 1 starting coordinates - RH
link1startXrh = 0
link1startYrh= 0

#global values
beamOriginX = -1
beamOriginY = -1
updatedLink1length = -1
updatedLink2length = -1
updatedLink1lengthRH = -1
updatedLink2lengthRH = -1

# get end coordinates of link1
def getL1End(linkLength):
    horizontal = linkLength * math.cos(math.radians(45))
    vertical = linkLength * math.sin(math.radians(45))
    return horizontal, vertical


# get start coordinates of link2
def getL2End(l1EndX, l1EndY):
    return l1EndX, l1EndY + l2

# update links with updated lengths
def next(event):
    # redraw links to correct length

    plt.clf()
    plt.axis('equal')

    # plot the beam profile back
    plt.plot([beamOriginX, beamOriginX + beamLength], [beamOriginY, beamOriginY], 'g-')
    plt.plot([beamOriginX, beamOriginX], [beamOriginY, beamOriginY + beamLength], 'g-')

    # plot updated member 1
    link1EndX = link1startX - getL1End(updatedLink1length)[0]  # also link2startX
    link1EndY = getL1End(updatedLink1length)[1]  # also link2startY
    plt.plot([link1startX, link1EndX], [link1startY, link1EndY], 'r-')

    print('link1startXrh:', str(link1startXrh))
    print('updatedLink1lengthRH:', str(updatedLink1lengthRH))
    print('updatedLink2lengthRH', str(updatedLink2lengthRH))
    # plot updated member 1 -RH
    link1EndXrh = getL1End(updatedLink1lengthRH)[0]  # also link2startX
    link1EndYrh = getL1End(updatedLink1lengthRH)[1]  # also link2startY
    plt.plot([link1startXrh, link1EndXrh], [link1startYrh, link1EndYrh], 'r-')

    print('link1endX', link1EndXrh)
    print('link1endYrh', link1EndYrh)


    # plot updated member 2
    link2EndX = position.defaultAngle(True, updatedLink2length, link1EndX, link1EndY)[0]
    link2EndY = position.defaultAngle(True, updatedLink2length, link1EndX, link1EndY)[1]
    plt.plot([link1EndX, link2EndX], [link1EndY, link2EndY], 'bo-')

    # plot updated member 2 - RH
    link2EndXrh = position.defaultAngle(False, updatedLink2lengthRH, link1EndXrh, link1EndYrh)[0]
    link2EndYrh = position.defaultAngle(False, updatedLink2lengthRH, link1EndXrh, link1EndYrh)[1]
    plt.plot([link1EndXrh, link2EndXrh], [link1EndYrh, link2EndYrh], 'bo-')

    # plot hat
    hatCoord = position.hatCoordinate(hatLength, link2EndX, link2EndY)
    plt.plot([link2EndX, hatCoord[0]], [link2EndY, hatCoord[1]], 'r-')

    # plot hat - RH
    hatCoord = position.hatCoordinateRight(hatLength, link2EndXrh, link2EndYrh)
    plt.plot([link2EndXrh, hatCoord[0]], [link2EndYrh, hatCoord[1]], 'r-')

    axnext = plt.axes([0.81, 0.05, 0.1, 0.075])
    bnext = Button(axnext, 'step2')
    bnext.on_clicked(next2)

    plt.show()


# update link 2 to be in the correct position
def next2(event):

    plt.clf()
    plt.axis('equal')

    # plot the beam profile back
    plt.plot([beamOriginX, beamOriginX + beamLength], [beamOriginY, beamOriginY], 'g-')
    plt.plot([beamOriginX, beamOriginX], [beamOriginY, beamOriginY + beamLength], 'g-')

    # plot updated member 1
    link1EndX = link1startX - getL1End(updatedLink1length)[0]  # also link2startX
    link1EndY = getL1End(updatedLink1length)[1]  # also link2startY
    plt.plot([link1startX, link1EndX], [link1startY, link1EndY], 'r-')

    # plot updated member 1 - RH
    link1EndXrh = getL1End(updatedLink1lengthRH)[0]  # also link2startX
    link1EndYrh = getL1End(updatedLink1lengthRH)[1]  # also link2startY
    plt.plot([link1startXrh, link1EndXrh], [link1startYrh, link1EndYrh], 'r-')

    # plot member 2 in right angled
    plt.plot([link1EndX, link1EndX], [link1EndY, link1EndY + updatedLink2length], 'bo-')

    # plot member 2 in right angled - RH
    plt.plot([link1EndXrh, link1EndXrh], [link1EndYrh, link1EndYrh + updatedLink2lengthRH], 'bo-')

    # plot hat
    plt.plot([link1EndX, link1EndX + hatLength], [link1EndY + updatedLink2length , link1EndY + updatedLink2length], 'r-')

    # plot hat - RH
    plt.plot([link1EndXrh, link1EndXrh - hatLength], [link1EndYrh + updatedLink2lengthRH , link1EndYrh + updatedLink2lengthRH], 'r-')

    axnext = plt.axes([0.81, 0.05, 0.1, 0.075])
    bnext = Button(axnext, 'reset')
    bnext.on_clicked(next3)

    plt.show()


def next3(event):

    plt.clf()
    main()



def main():
    #LH
    link1EndX = link1startX - getL1End(l1)[0]  # also link2startX
    link1EndY = getL1End(l1)[1]  # also link2startY
    link2EndX = position.defaultAngle(True,l2, link1EndX, link1EndY)[0]
    link2EndY = position.defaultAngle(True,l2, link1EndX, link1EndY)[1]

    #RH
    link1EndXrh = link1startXrh + getL1End(l1)[0]  # also link2startX
    link1EndYrh = getL1End(l1)[1]  # also link2startY
    link2EndXrh = position.defaultAngle(False, l2, link1EndXrh, link1EndYrh)[0]
    link2EndYrh = position.defaultAngle(False, l2, link1EndXrh, link1EndYrh)[1]

    plt.axis('equal')

    # plot link1
    plt.plot([link1startX, link1EndX], [link1startY, link1EndY], 'r-')
    # plot link2
    plt.plot([link1EndX, link2EndX], [link1EndY, link2EndY], 'bo-')
    # plot hat
    hatCoord = position.hatCoordinate(hatLength, link2EndX, link2EndY)
    plt.plot([link2EndX, hatCoord[0]], [link2EndY, hatCoord[1]], 'r-')


    # plot link1 -RH
    plt.plot([link1startXrh, link1EndXrh], [link1startYrh, link1EndYrh], 'r-')
    # plot link2 -RH
    plt.plot([link1EndXrh, link2EndXrh], [link1EndYrh, link2EndYrh], 'bo-')
    # plot hat - RH
    hatCoord = position.hatCoordinateRight(hatLength, link2EndXrh, link2EndYrh)
    plt.plot([link2EndXrh, hatCoord[0]], [link2EndYrh, hatCoord[1]], 'r-')

    global beamOriginX
    global beamOriginY
    beamOriginX = randint(int(link1EndX), int(link1startX) - 100)
    beamOriginY = randint(int(link1EndY)+ 800, int(link1EndY) + 1000)

    # plot beam horizontal member
    plt.plot([beamOriginX, beamOriginX + beamLength], [beamOriginY, beamOriginY], 'g-')
    # plot beam vertical member
    plt.plot([beamOriginX, beamOriginX], [beamOriginY, beamOriginY + beamLength], 'g-')

    # beam top left corner coordinates
    goalX = beamOriginX
    goalY = beamOriginY + beamLength
    # beam bottom right corner coordinates
    goalXbottom = beamOriginX + beamLength
    goalYbottom = beamOriginY


    global updatedLink1length
    global updatedLink2length
    global updatedLink1lengthRH
    global updatedLink2lengthRH

    # solve for the end coordinates
    updatedLink1length = abs(IK.solveL11(goalX))
    updatedLink2length = abs(IK.solveL22(goalX, goalY))
    updatedLink1lengthRH = abs(IK.solveL11(goalXbottom))

    # Hardcoded
    # updatedLink2lengthRH = abs(IK.solveL222(goalXbottom, goalYbottom))
    link1EndYrh = getL1End(updatedLink1lengthRH)[1]  # also link2startY
    updatedLink2lengthRH = goalYbottom - link1EndYrh

    print('goalX', goalX)
    print('goalY', goalY)
    print('goalXbottom: ', goalXbottom)
    print('goalYbottom: ', goalYbottom)
    print('updatedlink2length: ', updatedLink2length)
    print('updatedlink2lengthRH: ', updatedLink2lengthRH)

    axnext = plt.axes([0.81, 0.05, 0.1, 0.075])
    bnext = Button(axnext, 'step1')
    bnext.on_clicked(next)
    plt.show()


if __name__ == '__main__':
    main()






