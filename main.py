import matplotlib.pyplot as plt
from matplotlib.widgets import Button
import math
import position
import IK
from random import randint

currentStep = 0
l1 = 350  # length of link1
l2 = 350  # length of link2
beamLength = 500

# link 1 starting coordinates
link1startX = 0
link1startY = 0

#global values
beamOriginX = -1
beamOriginY = -1
updatedLink1length = -1
updatedLink2length = -1

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
    print('next button pressed')
    # redraw links to correct length
    if currentStep == 0:

        plt.clf()
        # plot the beam profile back
        plt.plot([beamOriginX, beamOriginX + beamLength], [beamOriginY, beamOriginY], 'b-')
        plt.plot([beamOriginX, beamOriginX], [beamOriginY, beamOriginY + beamLength], 'b-')

        # plot updated member 1
        link1EndX = link1startX - getL1End(updatedLink1length)[0]  # also link2startX
        link1EndY = getL1End(updatedLink1length)[1]  # also link2startY
        plt.plot([link1startX, link1EndX], [link1startY, link1EndY], 'r-')

        # plot updated member 2
        link2EndX = position.defaultAngle(updatedLink2length, link1EndX, link1EndY)[0]
        link2EndY = position.defaultAngle(updatedLink2length, link1EndX, link1EndY)[1]
        plt.plot([link1EndX, link2EndX], [link1EndY, link2EndY], 'o-')

        axnext = plt.axes([0.81, 0.05, 0.1, 0.075])
        bnext = Button(axnext, 'step2')
        bnext.on_clicked(next2)

        plt.axis('equal')
        plt.show()


# update link 2 to be in the correct position
def next2(event):

    plt.clf()

    # plot the beam profile back
    plt.plot([beamOriginX, beamOriginX + beamLength], [beamOriginY, beamOriginY], 'b-')
    plt.plot([beamOriginX, beamOriginX], [beamOriginY, beamOriginY + beamLength], 'b-')

    # plot updated member 1
    link1EndX = link1startX - getL1End(updatedLink1length)[0]  # also link2startX
    link1EndY = getL1End(updatedLink1length)[1]  # also link2startY
    plt.plot([link1startX, link1EndX], [link1startY, link1EndY], 'r-')

    # plot member 2 in right angled
    plt.plot([link1EndX, link1EndX], [link1EndY, link1EndY + updatedLink2length], 'o-')

    axnext = plt.axes([0.81, 0.05, 0.1, 0.075])
    bnext = Button(axnext, 'reset')
    bnext.on_clicked(next3)

    plt.axis('equal')
    plt.show()


def next3(event):



    plt.clf()
    main()



def main():

    link1EndX = link1startX - getL1End(l1)[0]  # also link2startX
    link1EndY = getL1End(l1)[1]  # also link2startY
    link2EndX = position.defaultAngle(l2, link1EndX, link1EndY)[0]
    link2EndY = position.defaultAngle(l2, link1EndX, link1EndY)[1]

    print('LINK1 START: (' + str(link1startX) + ',' + str(link1startY) + ')')
    print('LINK1 END: (' + str(link1EndX) + ',' + str(link1EndY) + ')')
    print('LINK2 END: (' + str(link2EndX) + ',' + str(link2EndY) + ')')

    # plot link1
    plt.plot([link1startX, link1EndX], [link1startY, link1EndY], 'r-')
    # plot link2
    plt.plot([link1EndX, link2EndX], [link1EndY, link2EndY], 'o-')

    # plot link1 finger 2
    




    global beamOriginX
    global beamOriginY
    beamOriginX = randint(int(link1EndX), int(link1startX))
    beamOriginY = randint(int(link1EndY), int(link1EndY) + 100)

    # plot beam horizontal member
    print('BEAM ORIGIN: (' + str(beamOriginX) + ',' + str(beamOriginY) + ')')
    plt.plot([beamOriginX, beamOriginX + beamLength], [beamOriginY, beamOriginY], 'b-')

    # plot beam vertical member
    plt.plot([beamOriginX, beamOriginX], [beamOriginY, beamOriginY + beamLength], 'b-')

    #beam top left corner coordinates
    goalX = beamOriginX
    goalY = beamOriginY + beamLength

    print('length2:' +  str(IK.solveL22(goalX, goalY)))
    print('length1: ' + str(IK.solveL11(goalX)))
    global updatedLink1length
    global updatedLink2length

    updatedLink1length = abs(IK.solveL11(goalX))
    updatedLink2length = abs(IK.solveL22(goalX, goalY))

    plt.axis('equal')
    axnext = plt.axes([0.81, 0.05, 0.1, 0.075])
    bnext = Button(axnext, 'step1')
    bnext.on_clicked(next)
    plt.show()


if __name__ == '__main__':
    main()






