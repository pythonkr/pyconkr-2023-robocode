# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/home/charlie/Documents/Python/RobotCode/PyQt-Robocode/Python-Robocode/GUI/window.ui'
#
# Created: Fri Dec 20 17:46:14 2013
#      by: PyQt4 UI code generator 4.10
# Modified: Thu Oct 17 12:30:00JST 2019
#      by: hjmr
#
# WARNING! All changes made in this file will be lost!


from PyQt6.QtWidgets import QApplication, QMainWindow, QWidget, QTableWidget, QGraphicsView
from PyQt6.QtWidgets import QTableWidget, QTableWidgetItem, QPushButton, QSlider, QLabel
from PyQt6.QtWidgets import QSpinBox, QSpacerItem, QMenuBar, QMenu, QStatusBar
from PyQt6.QtWidgets import QSizePolicy, QVBoxLayout, QHBoxLayout, QWidgetAction as QAction
from PyQt6.QtGui import QIcon, QPixmap
from PyQt6.QtCore import Qt, QSize, QRect, QMetaObject


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(792, 464)
        icon = QIcon()
        icon.addPixmap(QPixmap("robotImages/smallRed.png"), QIcon.Mode.Normal, QIcon.State.Off)
        MainWindow.setWindowIcon(icon)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout_4 = QVBoxLayout(self.centralwidget)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.tableWidget = QTableWidget(self.centralwidget)
        self.tableWidget.setAutoFillBackground(False)
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(5)
        self.tableWidget.setRowCount(0)
        item = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, item)
        item = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, item)
        item = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(3, item)
        item = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(4, item)
        self.tableWidget.horizontalHeader().setStretchLastSection(False)
        self.verticalLayout_3.addWidget(self.tableWidget)
        self.graphicsView = QGraphicsView(self.centralwidget)
        self.graphicsView.setEnabled(True)
        self.graphicsView.setStyleSheet("background-color: rgba(206, 206, 206, 162);")
        self.graphicsView.setObjectName("graphicsView")
        self.verticalLayout_3.addWidget(self.graphicsView)
        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.pushButton = QPushButton(self.centralwidget)
        self.pushButton.setObjectName("pushButton")
        self.verticalLayout.addWidget(self.pushButton)
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label_2 = QLabel(self.centralwidget)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout.addWidget(self.label_2)
        self.spinBox = QSpinBox(self.centralwidget)
        self.spinBox.setMaximum(10000)
        self.spinBox.setProperty("value", 3)
        self.spinBox.setObjectName("spinBox")
        self.horizontalLayout.addWidget(self.spinBox)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.horizontalLayout_2.addLayout(self.verticalLayout)
        spacerItem = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem)
        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label = QLabel(self.centralwidget)
        self.label.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.label.setStyleSheet("")
        self.label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.label.setObjectName("label")
        self.verticalLayout_2.addWidget(self.label)
        self.horizontalSlider = QSlider(self.centralwidget)
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.horizontalSlider.sizePolicy().hasHeightForWidth())
        self.horizontalSlider.setSizePolicy(sizePolicy)
        self.horizontalSlider.setMinimumSize(QSize(200, 0))
        self.horizontalSlider.setLayoutDirection(Qt.LayoutDirection.RightToLeft)
        self.horizontalSlider.setMaximum(120)
        self.horizontalSlider.setProperty("value", 70)
        self.horizontalSlider.setOrientation(Qt.Orientation.Horizontal)
        self.horizontalSlider.setInvertedAppearance(False)
        self.horizontalSlider.setInvertedControls(True)
        self.horizontalSlider.setObjectName("horizontalSlider")
        self.verticalLayout_2.addWidget(self.horizontalSlider)
        self.horizontalLayout_2.addLayout(self.verticalLayout_2)
        self.verticalLayout_3.addLayout(self.horizontalLayout_2)
        self.horizontalLayout_3.addLayout(self.verticalLayout_3)
        self.graphicsView_2 = QGraphicsView(self.centralwidget)
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.graphicsView_2.sizePolicy().hasHeightForWidth())
        self.graphicsView_2.setSizePolicy(sizePolicy)
        self.graphicsView_2.setMinimumSize(QSize(200, 0))
        self.graphicsView_2.setMaximumSize(QSize(200, 16777215))
        self.graphicsView_2.setStyleSheet("background-color: rgba(194, 194, 194, 167);")
        self.graphicsView_2.setObjectName("graphicsView_2")
        self.horizontalLayout_3.addWidget(self.graphicsView_2)
        self.verticalLayout_4.addLayout(self.horizontalLayout_3)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setGeometry(QRect(0, 0, 792, 23))
        self.menubar.setObjectName("menubar")
        self.menuBattle = QMenu(self.menubar)
        self.menuBattle.setObjectName("menuBattle")
        self.menuRobot = QMenu(self.menubar)
        self.menuRobot.setObjectName("menuRobot")
        self.menuHelp = QMenu(self.menubar)
        self.menuHelp.setObjectName("menuHelp")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionNew = QAction(MainWindow)
        self.actionNew.setObjectName("actionNew")
        self.actionNew_2 = QAction(MainWindow)
        self.actionNew_2.setObjectName("actionNew_2")
        self.actionOpen = QAction(MainWindow)
        self.actionOpen.setObjectName("actionOpen")
        self.actionClass_Reference = QAction(MainWindow)
        self.actionClass_Reference.setObjectName("actionClass_Reference")
        self.actionAbout = QAction(MainWindow)
        self.actionAbout.setObjectName("actionAbout")
        self.menuBattle.addAction(self.actionNew)
        self.menuRobot.addAction(self.actionNew_2)
        self.menuRobot.addAction(self.actionOpen)
        self.menuHelp.addSeparator()
        self.menuHelp.addAction(self.actionClass_Reference)
        self.menuHelp.addAction(self.actionAbout)
        self.menubar.addAction(self.menuBattle.menuAction())
        self.menubar.addAction(self.menuRobot.menuAction())
        self.menubar.addAction(self.menuHelp.menuAction())

        self.retranslateUi(MainWindow)
        QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QApplication.translate("MainWindow", "Python Robocode"))
        self.tableWidget.setSortingEnabled(True)
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(QApplication.translate("MainWindow", "Name"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(QApplication.translate("MainWindow", "1st"))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(QApplication.translate("MainWindow", "2nd"))
        item = self.tableWidget.horizontalHeaderItem(3)
        item.setText(QApplication.translate("MainWindow", "3rd"))
        item = self.tableWidget.horizontalHeaderItem(4)
        item.setText(QApplication.translate("MainWindow", "Points"))
        self.pushButton.setText(QApplication.translate("MainWindow", "Start Last Battle"))
        self.label_2.setText(QApplication.translate("MainWindow", "Battle\'s Number"))
        self.label.setText(QApplication.translate("MainWindow", "Game Speed"))
        self.menuBattle.setTitle(QApplication.translate("MainWindow", "Battle"))
        self.menuRobot.setTitle(QApplication.translate("MainWindow", "Robot"))
        self.menuHelp.setTitle(QApplication.translate("MainWindow", "Help"))
        self.actionNew.setText(QApplication.translate("MainWindow", "New"))
        self.actionNew_2.setText(QApplication.translate("MainWindow", "New"))
        self.actionOpen.setText(QApplication.translate("MainWindow", "Open"))
        self.actionClass_Reference.setText(QApplication.translate("MainWindow", "Class Reference"))
        self.actionAbout.setText(QApplication.translate("MainWindow", "About"))


if __name__ == "__main__":
    import sys
    app = QApplication(sys.argv)
    MainWindow = QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec())
