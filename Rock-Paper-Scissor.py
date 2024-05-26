import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QPixmap,QFont
from PyQt5.QtCore import QTimer
from random import randint
computerscore=0
playerscore=0

font=QFont("Times",13)
buttonfont=QFont("Arial",12)

class window(QWidget):
    def __init__(self):
        super().__init__()
        self.setGeometry(100,100,500,700)
        self.setWindowTitle("Rock Paper Scissors")
        self.UI()

    def UI(self):
        ####################SCORES######################
        self.computerscore=QLabel("Computer Score: ",self)
        self.playerscore=QLabel("Your Score: ",self)
        self.computerscore.setFont(font)
        self.playerscore.setFont(font)
        self.computerscore.move(40,30)
        self.playerscore.move(340,30)
        ####################IMAGES#######################
        self.computerimage=QLabel(self)
        self.computerimage.setPixmap(QPixmap("rock.png"))
        self.computerimage.move(40,140)
        self.playerimage=QLabel(self)
        self.playerimage.setPixmap(QPixmap("rock.png"))
        self.playerimage.move(340,140)
        self.gameimage=QLabel(self)
        self.gameimage.setPixmap(QPixmap("game.png"))
        self.gameimage.move(240,170)
        ####################BUTTONS#######################
        self.startbtn=QPushButton("START",self)
        self.startbtn.setFont(buttonfont)
        self.stopbtn=QPushButton("STOP",self)
        self.stopbtn.setFont(buttonfont)
        self.startbtn.move(150,300)
        self.stopbtn.move(250,300)
        self.startbtn.clicked.connect(self.start)
        self.stopbtn.clicked.connect(self.stop)
        ##################TIMER##########################
        self.timer=QTimer()
        self.timer.setInterval(100)
        self.timer.timeout.connect(self.PlayGame)
        self.show()
    def start(self):
        self.timer.start()
    def PlayGame(self):
        self.randcomputer=randint(1,3)
        if self.randcomputer == 1:
            self.computerimage.setPixmap(QPixmap("rock.png"))
        elif self.randcomputer == 2:
            self.computerimage.setPixmap(QPixmap("paper.png"))
        else :
            self.computerimage.setPixmap(QPixmap("scissors.png"))
        self.randplayer=randint(1,3)
        if self.randplayer == 1:
            self.playerimage.setPixmap(QPixmap("rock.png"))
        elif self.randplayer == 2:
            self.playerimage.setPixmap(QPixmap("paper.png"))
        else:
            self.playerimage.setPixmap(QPixmap("scissors.png"))



    def stop(self):
        global computerscore
        global playerscore
        self.timer.stop()
        if self.randcomputer == 1 and self.randplayer == 1:
            mbox = QMessageBox.information(self,"Information","Draw Game")
        elif self.randcomputer == 1 and self.randplayer == 2:
            mbox = QMessageBox.information(self,"Information","You Win")
            playerscore += 1
            self.playerscore.setText("Your Score:{}".format(playerscore))
        elif self.randcomputer == 1 and self.randplayer == 3:
            mbox = QMessageBox.information(self, "Information", "Computer Win")
            computerscore += 1
            self.computerscore.setText("Computer Score:{}".format(computerscore))
        elif self.randcomputer == 2 and self.randplayer == 2:
            mbox = QMessageBox.information(self, "Information", "Draw Game")
        elif self.randcomputer == 2 and self.randplayer == 1:
            mbox = QMessageBox.information(self, "Information", "Computer Win")
            computerscore += 1
            self.computerscore.setText("Computer Score:{}".format(computerscore))
        elif self.randcomputer == 2 and self.randplayer == 3:
            mbox = QMessageBox.information(self, "Information", "You Win")
            playerscore += 1
            self.playerscore.setText("Your Score:{}".format(playerscore))
        elif self.randcomputer == 3 and self.randplayer == 3:
            mbox = QMessageBox.information(self, "Information", "Draw Game")
        elif self.randcomputer == 3 and self.randplayer == 1:
            mbox = QMessageBox.information(self, "Information", "You Win")
            playerscore += 1
            self.playerscore.setText("Your Score:{}".format(playerscore))
        elif self.randcomputer == 3 and self.randplayer == 2:
            mbox = QMessageBox.information(self, "Information", "Computer Win")
            computerscore += 1
            self.computerscore.setText("Computer Score:{}".format(computerscore))

        if computerscore == 3 or playerscore == 3:
            mbox = QMessageBox.information(self,"Information","GameOver")
            sys.exit()



def main():
    App=QApplication(sys.argv)
    Window=window()
    sys.exit(App.exec_())

if __name__ == "__main__" :
    main()