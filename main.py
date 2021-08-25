#!/usr/bin/env python3
'''
from bridge import (Actuator, Replacer, Vision, Referee,
                        NUM_BOTS, convert_angle, Entity)

from math import pi, fmod, atan2, fabs

def main_strategy(field):
    """Sets all objetives to ball coordinates."""
    ball = field["ball"]
    objectives = [Entity(index=i) for i in range(NUM_BOTS)]
    for obj in objectives:
        obj.x = ball.x
        obj.y = ball.y

    return objectives

def smallestAngleDiff(target, source):
    """Gets the smallest angle between two points in a arch"""
    a = fmod(target + 2*pi, 2*pi) - fmod(source + 2 * pi, 2 * pi)

    if (a > pi):
        a -= 2 * pi
    else:
        if (a < -pi):
            a += 2 * pi

    return a


def controller(field, objectives):
    """
        Basic PID controller that sets the speed of each motor
        sends robot to objective coordinate
        Courtesy of RoboCin
    """

    speeds = [{"index": i} for i in range(NUM_BOTS)]
    our_bots = field["our_bots"]

    # for each bot
    for i, s in enumerate(speeds):
        Kp = 20
        Kd = 2.5

        try:
            controller.lastError
        except AttributeError:
            controller.lastError = 0

        right_motor_speed = 0
        left_motor_speed = 0

        reversed = False

        objective = objectives[i]
        our_bot = our_bots[i]

        angle_rob = our_bot.a

        angle_obj = atan2( objective.y - our_bot.y,
                            objective.x - our_bot.x )

        error = smallestAngleDiff(angle_rob, angle_obj)

        if (fabs(error) > pi / 2.0 + pi / 20.0):
            reversed = True
            angle_rob = convert_angle(angle_rob + pi)
            error = smallestAngleDiff(angle_rob, angle_obj)

        # set motor speed based on error and K constants
        error_speed = (Kp * error) + (Kd * (error - controller.lastError))

        controller.lastError = error

        baseSpeed = 30

        # normalize
        error_speed = error_speed if error_speed < baseSpeed else baseSpeed
        error_speed = error_speed if error_speed > -baseSpeed else -baseSpeed

        if (error_speed > 0):
            left_motor_speed = baseSpeed
            right_motor_speed = baseSpeed - error_speed
        else:
            left_motor_speed = baseSpeed + error_speed
            right_motor_speed = baseSpeed

        if (reversed):
            if (error_speed > 0):
                left_motor_speed = -baseSpeed + error_speed
                right_motor_speed = -baseSpeed
            else:
                left_motor_speed = -baseSpeed
                right_motor_speed = -baseSpeed - error_speed

        s["left"] = left_motor_speed
        s["right"] = right_motor_speed
    return speeds

if __name__ == "__main__":

    # Choose team (my robots are yellow)
    mray = False

    # Initialize all clients
    actuator = Actuator(mray, "127.0.0.1", 20011)
    replacement = Replacer(mray, "224.5.23.2", 10004)
    vision = Vision(mray, "224.0.0.1", 10002)
    referee = Referee(mray, "224.5.23.2", 10003)

    # Main infinite loop
    while True:
     # Atualiza a situação das faltas
        referee.update()
        ref_data = referee.get_data()

        # Atualiza os dados da visão
        vision.update()
        field = vision.get_field_data()

        data_our_bot = field["our_bots"]        #Salva os dados dos robôs aliados
        data_their_bots = field["their_bots"]   #Salva os dados dos robôs inimigos
        data_ball = field["ball"]               #Salva os dados da bola

        # Atualiza em cada objeto do campo os dados da visão
        robot0.simGetPose(data_our_bot[0])
        robot1.simGetPose(data_our_bot[1])
        robot2.simGetPose(data_our_bot[2])
        robotEnemy0.simGetPose(data_their_bots[0])
        robotEnemy1.simGetPose(data_their_bots[1])
        robotEnemy2.simGetPose(data_their_bots[2])
        ball.simGetPose(data_ball)

        if ref_data["game_on"]:
            # Se o modo de jogo estiver em "Game on"

            action.shoot(robot2,ball,leftSide= not mray, friend1 = robot0, friend2 = robot1, enemy1=robotEnemy0,  enemy2=robotEnemy1, enemy3=robotEnemy2)
            action.protectGoal(robot1, ball,50, leftSide= not mray)
            action.screenOutBall(robot0,ball,10,leftSide= not mray)


        #elif ref_data["foul"] != 7:
            # foul behaviour
            #actuator.stop()

       # elif ref_data["foul"] == 1:

        #elif ref_data["foul"] == 2:

        #elif ref_data["foul"] == 3:

        elif ref_data["foul"] == 4:
            replacement.place(0,-0.2, 0, 0)
            replacement.place(1,-0.2, 0.2, 0)
            replacement.place(2,-0.2, -0.2, 0)
            actuator.send_all()


       # elif ref_data["foul"] == 5:
       '''

       #!/usr/bin/env python3

from bridge import (Actuator, Replacer, Vision, Referee,
                        NUM_BOTS, convert_angle, Entity)

from math import pi, fmod, atan2, fabs

from simClasses import *
import action
import fouls

if __name__ == "__main__":

    # Choose team (my robots are yellow)
    mray = True

    # Initialize all clients
    actuator = Actuator(mray, "127.0.0.1", 20011)
    replacement = Replacer(mray, "224.5.23.2", 10004)
    vision = Vision(mray, "224.0.0.1", 10002)
    referee = Referee(mray, "224.5.23.2", 10003)

    # Initialize all  objects
    robot0 = Robot(0, actuator)
    robot1 = Robot(1, actuator)
    robot2 = Robot(2, actuator)

    robotEnemy0 = Robot(0, actuator)
    robotEnemy1 = Robot(1, actuator)
    robotEnemy2 = Robot(2, actuator)

    ball = Ball()

    # Main infinite loop
    while True:
        # Atualiza a situação das faltas
        referee.update()
        ref_data = referee.get_data()

        # Atualiza os dados da visão
        vision.update()
        field = vision.get_field_data()

        data_our_bot = field["our_bots"]        #Salva os dados dos robôs aliados
        data_their_bots = field["their_bots"]   #Salva os dados dos robôs inimigos
        data_ball = field["ball"]               #Salva os dados da bola

        # Atualiza em cada objeto do campo os dados da visão
        robot0.simGetPose(data_our_bot[0])
        robot1.simGetPose(data_our_bot[1])
        robot2.simGetPose(data_our_bot[2])
        robotEnemy0.simGetPose(data_their_bots[0])
        robotEnemy1.simGetPose(data_their_bots[1])
        robotEnemy2.simGetPose(data_their_bots[2])
        ball.simGetPose(data_ball)

        if ref_data["game_on"]:
            # Se o modo de jogo estiver em "Game on"

            action.shoot(robot2,ball,leftSide= not mray, friend1 = robot0, friend2 = robot1, enemy1=robotEnemy0,  enemy2=robotEnemy1, enemy3=robotEnemy2)
            action.protectGoal(robot1, ball,50, leftSide= not mray)
            action.screenOutBall(robot0,ball,10,leftSide= not mray)
     
        if ref_data["foul"] == 2:
            print("robot0:", robot0.xPos, ",", robot0.yPos, "\nrobot1:", robot1.xPos, ",", robot1.yPos, "\nrobot2:", robot2.xPos, ",", robot2.yPos)

        '''else:
            fouls.replacement_fouls(replacement,ref_data,mray)
'''