import math

def defaultAngle(length, startX, startY):
    endX = -length * math.cos(math.radians(45)) + startX
    endY = length * math.sin(math.radians(45)) + startY
    return endX, endY

def rightAngle(length, startX, startY):


    return