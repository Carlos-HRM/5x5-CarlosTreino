from numpy import cos,sin,arctan2,sqrt,sign,pi,delete,append,array,angle, deg2rad
# Estas funções são utilizadas para alterar a execução das estratégias do jogador nos cantos
# Afim de impedir que ele fique travado

def targetInCorner(target, robot):

    corner = 0
    flagCorner = False
    if not robot.teamYellow:
        if target.xPos < 20:

            flagCorner = True
            corner = 1
            if target.xPos < 5:
                target.update(target.xPos+3, target.yPos, target.theta)
            else:
                target.update(target.xPos+1.5, target.yPos, target.theta)
        elif target.xPos > 150:

            flagCorner = True
            corner = 3
            if target.xPos > 155:
                target.update(target.xPos-3, target.yPos, target.theta)
            else:
                target.update(target.xPos-1.5, target.yPos, target.theta)
        if target.yPos < 10:

            flagCorner = True
            corner = 2
            if target.yPos < 5:
                target.update(target.xPos,target.yPos+3, target.theta)
            else:
                target.update(target.xPos,target.yPos+1.5, target.theta)
        elif target.yPos > 120:

            flagCorner = True
            corner = 4
            if target.yPos > 125:
                target.update(target.xPos,target.yPos-3, target.theta)
            else:
                target.update(target.xPos,target.yPos-1.5, target.theta)
    else:
        if target.xPos < 20:

            flagCorner = True
            corner = 1
            if target.xPos < 15:
                target.update(target.xPos+3, target.yPos, target.theta)
            else:
                target.update(target.xPos+1.5, target.yPos, target.theta)
        elif target.xPos > 150:

            flagCorner = True
            corner = 3
            if target.xPos > 155:
                target.update(target.xPos-3, target.yPos, target.theta)
            else:
                target.update(target.xPos-1.5, target.yPos, target.theta)
        if target.yPos < 10:

            flagCorner = True
            corner = 2
            if target.yPos < 5:
                target.update(target.xPos,target.yPos+3, target.theta)
            else:
                target.update(target.xPos,target.yPos+1.5, target.theta)
        elif target.yPos > 120:

            flagCorner = True
            corner = 4
            if target.yPos > 125:
                target.update(target.xPos,target.yPos-3, target.theta)
            else:
                target.update(target.xPos,target.yPos-1.5, target.theta)

    if flagCorner:
        changeTargetTheta(robot, target,corner)

    return flagCorner, corner

def changeTargetTheta(robot, target,corner):

    dist = sqrt((robot.xPos- target.xPos)**2 + (robot.yPos- target.yPos)**2)

    if not robot.teamYellow:
        if (corner == 2 or corner == 4):
            if dist < 6:
                if robot.yPos < 75:
                    thetaGol = angle(160- robot.xPos,75)

                else:
                    thetaGol = angle(160- robot.xPos,-75)
                target.update(target.xPos,target.yPos,thetaGol)
            else:
                target.update(target.xPos,target.yPos,0)

        elif robot.yPos > 110:
            if corner == 1:
                target.update(target.xPos,target.yPos,pi/2)
            elif corner == 3:
                target.update(target.xPos,target.yPos,-pi/2)
        elif robot.yPos < 40:
            if corner == 1:
                target.update(target.xPos,target.yPos,-pi/2)
            elif corner == 3:
                target.update(target.xPos,target.yPos,pi/2)
    else:
        if (corner == 2 or corner == 4):
            if dist < 6:
                if robot.yPos < 75:
                    thetaGol = angle(10- robot.xPos,75)

                else:
                    thetaGol = angle(10- robot.xPos,-75)
                target.update(target.xPos,target.yPos,thetaGol)
            else:
                if target.yPos > 65:
                    target.update(target.xPos,target.yPos,-pi+deg2rad(10))
                else:
                    target.update(target.xPos,target.yPos, pi-deg2rad(10))

        elif robot.yPos > 110:
            if corner == 1:
                target.update(target.xPos,target.yPos,-pi/2)
            elif corner == 3:
                target.update(target.xPos,target.yPos,pi/2)
        elif robot.yPos < 40:
            if corner == 1:
                target.update(target.xPos,target.yPos,pi/2)
            elif corner == 3:
                target.update(target.xPos,target.yPos,-pi/2)

    return None

def robotLockedCorner(target, robot):

    corner = 0
    flagLocked = False
    if (robot.xPos < 3 and (robot.yPos > 110 or robot.yPos < 40)):
        if (abs(robot.theta) < 0.35 or abs(robot.theta - pi) < 0.35):
            flagLocked = True
            corner = 1
    elif (robot.xPos > 147 and (robot.yPos > 110 or robot.yPos < 40)):
        if (abs(robot.theta) < 0.35 or abs(robot.theta - pi) < 0.35):
            flagLocked = True
            corner = 3
    if robot.yPos < 5:
        if ((abs(robot.theta) < ((pi/2)+0.35)) and (abs(robot.theta) > ((pi/2)-0.35))):
            flagLocked = True
            corner = 2
    elif robot.yPos > 125:
        if ((abs(robot.theta) < ((pi/2)+0.35)) and (abs(robot.theta) < ((pi/2)-0.35))):
            flagLocked = True
            corner = 4

    if flagLocked:
        changeTargetPos(robot, target,corner)

    return flagLocked, corner

def changeTargetPos(robot, target,corner):

    if corner == 1:
        target.update(robot.xPos+10,robot.yPos,0)
    if corner == 2:
        target.update(robot.xPos,robot.yPos+10,pi/2)
    if corner == 3:
        target.update(robot.xPos-10,robot.yPos,0)
    if corner == 4:
        target.update(robot.xPos,robot.yPos-10,-pi/2)
    return None
