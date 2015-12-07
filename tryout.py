# -*- coding: utf-8 -*-
from __future__ import unicode_literals


from PyQt4.QtGui import *
from PyQt4.QtCore import *
import sys
import os

class MyTextEdit(QTextEdit):
	def __init__(self,newparent, parent=None):
		super(MyTextEdit, self).__init__(parent)
		self.newparent = newparent

	def keyPressEvent(self, event):
		if event.key() == Qt.Key_Backspace:
			print("that was the back")
		if event.key() == Qt.Key_Escape:
			print("the escape key")
			self.newparent.close()

		if event.key() == Qt.Key_Return:
			print("that was the enter")
			curtext = self.toPlainText()
			# self.append(self.newparent.fulltext+ "\r")


class Window(QWidget):
	def __init__(self, parent=None):
		super(Window, self).__init__(parent)

		self.menuBar = QMenuBar()
		filemenu = self.menuBar.addMenu("&File")

		self.lineEdit = MyTextEdit(newparent=self)

		layout = QGridLayout()
		layout.addWidget(self.menuBar)
		layout.addWidget(self.lineEdit)
		self.setGeometry(50, 50, 300, 300)
		self.updatedir()
		self.setLayout(layout)
		self.connect(self.lineEdit, SIGNAL("returnPressed()"), self.getkey)

	def keyPressEvent(self, ev):
		print("something was pressed")
		print(ev.text())
		print(ev.key())

	def updatedir(self):
		self.curdir = os.getcwd()
		print(self.curdir)
		self.fulltext = self.curdir + "> "
		self.lineEdit.setText(self.fulltext)

	def getkey(self, event):
		print("something pressed")



app = QApplication(sys.argv)
win = Window()
win.show()
app.exec_()