import math

# This is the resting angle
def defaultAngle(isLeftHand,length, startX, startY):
    if(isLeftHand):
        endX = -length * math.cos(math.radians(45)) + startX
    else:
        endX = length * math.cos(math.radians(45)) + startX
    endY = length * math.sin(math.radians(45)) + startY
    return endX, endY

def hatCoordinate(length, startX, startY):
    x = startX + length * math.cos(math.radians(45))
    y = startY + length * math.sin(math.radians(45))
    return x,y

def hatCoordinateRight(length, startX, startY):
    x = startX - length * math.sin(math.radians(45))
    y = startY + length * math.cos(math.radians(45))
    return x,y