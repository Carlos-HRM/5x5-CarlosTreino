import time
import sys
import argparse
from action import Robot2Position

import fouls
from bridge import (Actuator, Replacer, Vision, Referee)
from simClasses import *
from strategy import *

if __name__ == "__main__":

    # Fazer tratamento de entradas erradas

    # parser = argparse.ArgumentParser(description='Argumentos para execução do time no simulador FIRASim')

    # parser.add_argument('-t', '--team', type=str, default="blue", help="Define o time/lado que será executado: blue ou yellow")
    # parser.add_argument('-s', '--strategy', type=str, default="twoAttackers", help="Define a estratégia que será jogada: twoAttackers ou default" )
    # parser.add_argument('-op', '--offensivePenalty', type=str, default='spin', dest='op', help="Define o tipo de cobrança ofensiva de penalti: spin ou direct")
    # parser.add_argument('-dp', '--defensivePenalty', type=str, default='direct', dest='dp', help="Define o tipo de defesa de penalti: spin ou direct")
    # parser.add_argument('-aop', '--adaptativeOffensivePenalty', type=str, default='off', dest='aop', help="Controla a troca de estratégias de penalti durante o jogo")
    # parser.add_argument('-adp', '--adaptativeDffensivePenalty', type=str, default='off', dest='adp', help="Controla a troca de estratégias de penalti durante o jogo")

    # args = parser.parse_args()

    # # Choose team (my robots are yellow)
    # if args.team == "yellow":
    #     mray = True
    # else:
    #     mray = False

    mray = False
    
    # Initialize all clients
    actuator = Actuator(mray, "127.0.0.1", 20011)
    replacement = Replacer(mray, "224.5.23.2", 10004)
    vision = Vision(mray, "224.0.0.1", 10002)
    referee = Referee(mray, "224.5.23.2", 10003)

    # Initialize all  objects
    robot0 = Robot(0, actuator, mray)
    robot1 = Robot(1, actuator, mray)
    robot2 = Robot(2, actuator, mray)

    robotEnemy0 = Robot(0, actuator, not mray)
    robotEnemy1 = Robot(1, actuator, not mray)
    robotEnemy2 = Robot(2, actuator, not mray)

    ball = Ball()

    # list_strategies = [ args.strategy, args.op, args.dp, args.aop, args.adp ]
    # strategy = Strategy(robot0, robot1, robot2, robotEnemy0, robotEnemy1, robotEnemy2, ball, mray, list_strategies)

    # Main infinite loop
    while True:
        t1 = time.time()

        # Update the vision data
        vision.update()
        field = vision.get_field_data()

        data_our_bot = field["our_bots"]  # Save data from allied robots
        data_their_bots = field["their_bots"]  # Save data from enemy robots
        data_ball = field["ball"]  # Save the ball data

        # Updates vision data on each field object
        robot0.sim_get_pose(data_our_bot[0])
        robot1.sim_get_pose(data_our_bot[1])
        robot2.sim_get_pose(data_our_bot[2])
        robotEnemy0.sim_get_pose(data_their_bots[0])
        robotEnemy1.sim_get_pose(data_their_bots[1])
        robotEnemy2.sim_get_pose(data_their_bots[2])
        ball.sim_get_pose(data_ball)

        #robot, ball, friend1, friend2, enemy1, enemy2, enemy3, xpos: float, ypos: float, theta:float)
        Robot2Position(robot0, ball, robot1, robot2, robotEnemy0, robotEnemy1, robotEnemy2, 85, 75, 0)
        Robot2Position(robot1, ball, robot0, robot2, robotEnemy0, robotEnemy1, robotEnemy2, 85, 65, 0)
        Robot2Position(robot2, ball, robot0, robot1, robotEnemy0, robotEnemy1, robotEnemy2, 85, 55, 0)

        # # synchronize code execution based on runtime and the camera FPS
        t2 = time.time()
        if t2 - t1 < 1 / 60:
            time.sleep(1 / 60 - (t2 - t1))
