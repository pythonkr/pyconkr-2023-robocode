#! /usr/bin/python
# -*- coding: utf-8 -*-

import sys
import os

sys.path.append(os.getcwd() + "/GUI")
sys.path.append(os.getcwd() + "/Objects")
sys.path.append(os.getcwd() + "/robotImages")
sys.path.append(os.getcwd() + "/Robots")
from window import MainWindow
from robot import Robot

from PyQt5.QtWidgets import QApplication

if __name__ == "__main__":
    cli_input = False
    app = QApplication(sys.argv)
    app.setApplicationName("Python-Robocode")
    commentator = True

    if cli_input:
        listBots = {}
        botnames = []
        sz=500
        botFiles = os.listdir(os.getcwd() + "/Robots")
        for botFile in botFiles:
            if botFile.endswith('.py'):
                botName = botPath = botFile[:botFile.rfind('.')]
                if botName not in botnames:
                    botnames.append(botName)
                    try:
                        botModule = __import__(botPath)
                        for name in dir(botModule):
                            if getattr(botModule, name) in Robot.__subclasses__():
                                someBot = getattr(botModule, name)
                                bot = someBot
                                listBots[str(bot).replace("<class '", "").replace("'>", "")] = bot
                                break
                    except Exception as e:
                        print("Problem with bot file '{}': {}".format(botFile, str(e)))

        alive_robots = []
        temp_dict = {}
        for i, key in enumerate(listBots.keys()):
            temp_dict[i + 1] = key
        gui = False
        bots = []
        while True:
            k = input(f"Press 1 to pick tanks. Current tanks: {alive_robots}\n"+
                      f"Press 2 to change field size. Current size: {sz}\n"+
                      f"Press 3 to start battles.\n"+
                      f"Press 4 to turn on/off GUI. Showing GUI: {gui}.\n" +
                      f"Press 5 to turn on/off Commentator. Commentartor allowed: {commentator}.\n" +
                      f"Your input: ")
            if k == "1":
                for key, value in temp_dict.items():
                    print(f'[{key}] {value.split(".")[1]}')
                ctr = 1
                while True:
                    robot_nr = input(f"Select robot {ctr}: ")
                    if robot_nr == "-1" and ctr > 2:
                        break
                    elif str.isdigit(robot_nr):
                        alive_robots.append(temp_dict[int(robot_nr)])
                        bots.append(listBots[temp_dict[int(robot_nr)]])
                        ctr += 1
                    else:
                        continue
                    if ctr > 2:
                        print(f'Selected robot(s): {alive_robots}. Press -1 to stop adding')
                    elif ctr == 2:
                        print(f'Selected robot: {alive_robots}')


            elif k == "2":
                sz = input("New size of the field: ")
                if str.isnumeric(sz) and int(sz)>0:

                    bots = []
            elif k=="3":
                myapp = MainWindow(allowCommentator=commentator, cli_input=True)
                if gui:
                    myapp.show()
                myapp.setUpBattle(sz, sz, bots)
                myapp.startBattle()
                break
            elif k=="4":
                gui = not gui
            elif k=="5":
                commentator = not commentator
    else:
        myapp = MainWindow(allowCommentator=commentator)
        myapp.show()
    sys.exit(app.exec_())
