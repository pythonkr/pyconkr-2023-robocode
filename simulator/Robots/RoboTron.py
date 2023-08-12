#! /usr/bin/python
# -*- coding: utf-8 -*-

from robot import Robot  # Import a base Robot
import math


class RoboTron(Robot):  # Create a Robot

    def init(self):  # To initialyse your robot

        # Set the bot color in RGB
        self.setColor(36, 242, 225)
        self.setGunColor(110, 255, 175)
        self.setRadarColor(250, 255, 110)
        self.setBulletsColor(255, 0, 0)

        self.radarVisible(True)  # if True the radar field is visible

        self.lockRadar("gun")

        # Et radariga märgata esimene vastane.
        self.setRadarField("round")
        self.lastX = None
        self.lastY = None
        self.firePOWER = 1

    def run(self):  # main loop to command the bot
        # Kuna Pythonis saab igal ajahetkel ainult ühte asja teha, pole väga mõtet suurt vaeva liikumisega näha
        # Eeldame lihtsalt, et meil on parim relva ja radarisüsteem ja sellega võidame vastase.
        # Javas saab kasutada advanced robot klassi, millega saab igal ajahetkel teha mitut asja.
        # Seega Javas saaks nii lasta, pöörata relva, liikuda kui ka radariga vastast skäneerida kõike samal ajal.
        # get the map size
        size = self.getMapSize()
        pos = self.getPosition()
        size.width()  # x
        size.height()  # y

        # Proovime mitte seina sõita.
        # lagi
        if pos.y() - 80 < 0:
            if 90 > self.getHeading() % 360:
                self.turn(-20)
            elif self.getHeading() % 360 > 270:
                self.turn(20)
        # põrand
        elif pos.y() + 80 > size.height():
            if 180 < self.getHeading() % 360:
                self.turn(-20)
            else:  # self.getHeading() % 360 < 180:
                self.turn(20)

        # vasak sein
        elif pos.x() - 80 < 0:
            if 270 < (self.getHeading() % 360):
                self.turn(-20)
            else:  # elif self.getHeading() % 360 < 270:
                self.turn(20)

        # parem sein
        elif pos.x() + 80 > size.width():
            if 90 > self.getHeading() % 360:
                self.turn(20)
            elif self.getHeading() % 360 > 90:
                self.turn(-20)

        else:  # Mingi suht suvaline liikumine.
            self.gunTurn(15)
            self.turn(3)
            self.setRadarField("normal")
        self.move(10)

    def onHitWall(self):
        # kui eelnev kood toimib ei käivitu see kunagi :).
        self.turn(60)

    def sensors(self):
        pass

    def onRobotHit(self, robotId, robotName):  # when My bot hit another
        # rammime ja tulistame
        self.setRadarField('round')
        self.move(-1)
        self.move(2)

    def onHitByRobot(self, robotId, robotName):
        self.setRadarField('round')

    def onHitByBullet(self, bulletBotId, bulletBotName, bulletPower):  # NECESARY FOR THE GAME
        pass

    def onBulletHit(self, botId, bulletId):  # NECESARY FOR THE GAME
        # Suurendame lasu tugevust kuna me oleme lihtsalt nii täpsed.
        self.firePOWER = self.firePOWER + 1

    def onBulletMiss(self, bulletId):
        # Kui mööda laseme, siis suurendame radari vaatevälja, et rohkem roboteid näha.
        # Ja lähtestame kuuli tugevuse.
        self.setRadarField('large')
        self.firePOWER = 1

    def onRobotDeath(self):
        pass

    def onTargetSpotted(self, botId, botName, botPos):  # NECESARY FOR THE GAME
        # Proovitud on implementeerida lineaarset tulistamist, et eeldatakse, et vastane liigub samas suunas.
        # Pythonis raskem implementeerida, kuna siin on ainult vastase asukoht olemas.
        # Javas on olemas ka vastase liikumissuund ja kiirus mille abil on seda palju lihtsam teha.
        self.setRadarField('normal')
        pos = self.getPosition()
        if self.lastX == None or self.lastY == None or -10 > self.lastX - botPos.x() > 10 or -10 > self.lastY - botPos.y() > 10 or (
                self.lastX == botPos.x() and self.lastY == botPos.y()):
            dx = botPos.x() - pos.x()
            dy = botPos.y() - pos.y()
        else:  # Võtame arvesse viimase asukoha.
            dx = (botPos.x() - self.lastX) * (
                        18 * abs(botPos.x() - pos.x()) / self.getMapSize().width()) + botPos.x() - pos.x()
            dy = (botPos.y() - self.lastY) * (
                        18 * abs(botPos.y() - pos.y()) / self.getMapSize().height()) + botPos.y() - pos.y()
        a = self.getEnemyAngle(dx, dy)

        self.gunTurn(a)
        self.fire(self.firePOWER)
        # Hea üritus vastasega kere risti panna kuid see tegi laskmise palju aeglasemaks...
        #headingDiff = abs(self.getHeading() % 360 - self.getGunHeading() % 360)
        #if headingDiff > 10:
        #    if self.getHeading() % 360 > self.getGunHeading() % 360:
        #        if headingDiff > 180:
        #            self.turn(headingDiff - 270)
        #        else:
        #            self.turn(headingDiff - 90)
        #    else:
        #        if headingDiff > 180:
        #            self.turn(headingDiff - 90)
        #        else:
        #            self.turn(headingDiff - 270)

        self.lastX = botPos.x()
        self.lastY = botPos.y()

    def getEnemyAngle(self, dx, dy):
        # Võetud track_target.py robotilt.
        my_gun_angle = self.getGunHeading() % 360
        enemy_angle = math.degrees(math.atan2(dy, dx)) - 90
        a = enemy_angle - my_gun_angle
        if a < -180:
            a += 360
        elif 180 < a:
            a -= 360
        return a
