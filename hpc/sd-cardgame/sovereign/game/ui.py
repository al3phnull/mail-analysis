#/usr/bin/env python

import sys, os
import itertools
import argparse
from PyQt4 import QtCore, QtGui


class Sovereign(object):
    def __init__(self):
        super(Sovereign, self).__init__()

        self.initUI()

    def initUI(self):
        self.cboard = Board(self)
        self.setCentralWidget(self.cboard)

        self.statusbar = self.StatusBar()
        self.cboard.msg2statusbar[str].connect(self.statusbar.showMessage)

        self.cboard.start()

        self.setGeometry(300, 300, 250, 150)
        self.center()
        self.setWindowTitle('Sovereign')
        self.show

def main():
    app = QtGui.QApplication([])
    game = Sovereign()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()
