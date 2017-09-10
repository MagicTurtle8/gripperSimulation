import math

# This is the resting angle
def defaultAngle(isLeftHand,length, startX, startY):
    if(isLeftHand):
        endX = -length * math.cos(math.radians(45)) + startX
    else:
        endX = length * math.cos(math.radians(45)) + startX
    endY = length * math.sin(math.radians(45)) + startY
    return endX, endY

