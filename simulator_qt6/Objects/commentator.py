#! /usr/bin/python
# -*- coding: utf-8 -*-
import re
import time, os, random

from robot import Robot
from collections import Counter


class Commentator():

    def __init__(self, allowed, window, name="COMMENTATOR", betting=True, chattiness=3):
        self.__chattiness = chattiness
        self.window = window
        self.allowed = allowed
        self.allowBetting = betting
        self.name = name
        self.spottingDict = dict()
        self.bets = []

    def commentHealth(self):
        print(f'{self.name}: Current status:')
        for item in self.window.getScene().items():
            if isinstance(item, Robot) and item.getHealth() > 0:
                print(f'{item} health: {item.getHealth()}')

    def commentDeath(self, bot):
        print(f'{self.name}: {bot} died')
        self.commentHealth()

    def commentSpotted(self, bot, target):
        if bot in self.spottingDict:
            if target in self.spottingDict[bot]:
                return
            print(f'{self.name}: {bot} spotted by {target}')
            self.spottingDict[bot].append(target)
            return
        self.spottingDict[bot] = [target]
        print(f'{self.name}: {bot} spotted by {target}')

    def commentHit(self, target, attacker, dmg):
        print(f'{self.name}: {target} was hit by {attacker} for {dmg} damage.')

    def initBetting(self):
        robs = []
        for item in self.window.getScene().items():
            if isinstance(item, Robot):
                robs.append(str(item))
        amounts = (Counter(robs))
        print("You have infinite money. Example bet might look something like this:  I will bet 10000 on MegaRobot")
        print(f"Participants:")
        ctr = 1
        ids = dict()
        for bot, amount in amounts.items():
            print(
                f"#{ctr} Robot type: {bot}, on battlefield: {amount}. Coefficient: {round(len(robs) / amounts[bot], 2)}")
            ids[ctr] = bot
            ctr += 1

        while True:
            bet = input("Place your bets: ")
            if bet=="-1":
                return
            robot = None
            for i in ids.keys():
                if re.search(r"\B" + re.escape("#" + str(i)) + r"\b", bet, re.IGNORECASE) or\
                        re.search(r'\b'+re.escape(ids[i])+r'\b', bet, re.IGNORECASE):
                    robot = ids[i]
            if robot:
                k = re.search(r'(?<!#)\b\d+\.\d+\b|(?<!#)\b\d+,\d+\b|(?<!#)\b\d+\b', bet, re.IGNORECASE)
                if k:
                    confirmed = input(f"Confirm {k.group(0)} bet on {robot}?(y/N): ")
                    if confirmed == "y":
                        self.bets = (robot, k.group(0), round(len(robs) / amounts[robot], 2))
                        break
                    elif confirmed == "-1":
                        break
                    else:
                        continue
                else:
                    print("Did not catch it. Can you try again please or press -1 to escape betting")
            else:
                print("Did not catch it. Can you try again please or press -1 to escape betting")

    def resolveBetting(self, data):
        if not self.bets:
            return
        if self.bets[0] == str(data):
            print(f"Correct bet! Received {round(float(self.bets[1]) * float(self.bets[2]),2)} currency")
        else:
            print(f"Wrong bet! Lost {self.bets[1]} currency")
        self.bets=[]

