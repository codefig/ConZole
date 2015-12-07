__author__ = '0code'


from PyQt4.QtCore import *
from PyQt4.QtGui import *
import sys



class Konsole(QMainWindow):
    def __init__(self, parent=None):
        super(Konsole,self).__init__(parent)
        self.setWindowTitle("Konsole")
        self.setWindowIcon(QIcon("./cmd2.png"))
        self.setMinimumSize(600, 450)

        self.tabcount = 1

        #create the statusBar
        statusBar = QStatusBar()
        statusBar.setToolTip("Ready")
        statusBar.setStatusTip("Not ready")
        self.setStatusBar(statusBar)

        #create the Menu
        self.createMenu()

        #create the Toolbar
        self.createToolBar()

        #create the main Layout
        mainLayout = QVBoxLayout()
        self.tabWidget = QTabWidget()

        firstPane = QWidget()
        firstPaneLayout = QGridLayout()
        firstPaneLayout.addWidget(QTextEdit(), 0,1)
        firstPane.setLayout(firstPaneLayout)

        self.tabWidget.addTab(firstPane, "Konsole - " + str(self.tabcount))

        mainLayout.addWidget(self.tabWidget)
        self.setCentralWidget(self.tabWidget)






    def resizeEvent(self, event):
        '''i wanna work on this to help resize the centr4al widge t'''
        pass

    def createToolBar(self):
        """
            thsi function creates all the items in the Toolbar
        """
        self.prevTabAction = QAction(QIcon("left.png"), "Previous Tab", self)
        self.prevTabAction.triggered.connect(self.moveToPreviousTab)

        self.nextTabAction = QAction(QIcon("right.png"), "NextTab", self)
        self.nextTabAction.triggered.connect(self.moveToNextTab)

        self.toolbar = self.addToolBar("ToolBar")
        self.toolbar.addAction(self.prevTabAction)
        self.toolbar.addAction(self.nextTabAction)


    def createMenu(self):
        """
            this function creates all menuBar items
        """
        menuBar = QMenuBar()
        self.setMenuBar(menuBar)
        filemenu = menuBar.addMenu("&File")
        editmenu = menuBar.addMenu("&Edit")
        viewmenu = menuBar.addMenu("&View")
        helpmenu = menuBar.addMenu("&Tabs")

        #NewTabAction -FileMenu
        newTabAction = QAction("New Tab", self)
        newTabAction.setShortcut("Ctrl+N")
        newTabAction.setStatusTip("New Console Tab")
        newTabAction.triggered.connect(self.createNewTab)

        #closTab - FileMenu
        closeTabAction = QAction("Close Tab", self)
        #closeTabAction.setShortcut("Ctrl+C", self)
        closeTabAction.setStatusTip("Close current Tab")

        #connect the closeTabAction to the slot
        closeTabAction.triggered.connect(self.closeTab)

        #closeToRight - FileMenu
        closeToRightAction = QAction("Close To Right", self)
        closeToRightAction.setShortcut("Ctrl+R")
        closeToRightAction.setStatusTip("Close All Tabs To Right of This")

        #closeToLeft - FileMenu
        closeToLeftAction = QAction("Close To Left", self)
        closeToLeftAction.setShortcut("Ctrl+L")
        closeToLeftAction.setStatusTip("Close All Tabs To Left Of This")

        #closeAllButThis - FileMenu
        closeAllButThisAction = QAction("Close All But This", self)
        closeAllButThisAction.setShortcut("Ctrl+T")
        closeAllButThisAction.setStatusTip("Close All Tabs But This")
        closeAllButThisAction.setToolTip("Close All ut")

        #exitAction - FileMenu
        exitAction = QAction("Exit", self)
        exitAction.setStatusTip("Exit Konsole")

        #connect the exitAction to
        exitAction.triggered.connect(self.printTabinfo)

        #add all the created actions
        filemenu.addAction(newTabAction)
        filemenu.addAction(closeTabAction)
        filemenu.addAction(closeToRightAction)
        filemenu.addAction(closeToLeftAction)
        filemenu.addAction(closeAllButThisAction)
        filemenu.addSeparator()
        filemenu.addAction(exitAction)

    def createNewTab(self):
        """
            This method creates the new tab for the New Tab Action
        """
        pageWidget = QWidget()
        pageWidgetLayout = QVBoxLayout()
        pageWidgetLayout.addWidget(QTextEdit())
        pageWidget.setLayout(pageWidgetLayout)
        self.tabcount += 1 #increment the tab counter
        self.tabWidget.addTab(pageWidget,"Konsole - " + str(self.tabcount))
        self.tabWidget.setCurrentIndex(self.tabWidget.currentIndex()+1)

    def closeTab(self):
        """
            This is meant to remove the tab from the TabWidget
            -> gets the index of the current tab in focuse
            -> removes the index from the list of index if  index not 0
        """
        tabindex = self.tabWidget.currentIndex()

        #remove the widget in the currentIndex in focus
        if tabindex is not 0:
            #then remove the tab
            self.tabWidget.removeTab(tabindex)
            self.tabcount -= 1 #remove 1 from the tabs

    def printTabinfo(self):
        print(self.tabWidget.currentIndex())
        self.tabWidget.update()

    def moveToNextTab(self):
        """
          algo : get the current tab index:
            if there is one greater than that
            move
            else:
            dont move
        """
        thisTabIndex = self.tabWidget.currentIndex()
        nextTabIndex = thisTabIndex + 1
        self.tabWidget.setCurrentIndex(nextTabIndex)

    def moveToPreviousTab(self):
        thisTabIndex = self.tabWidget.currentIndex()
        previousTabIndex = thisTabIndex - 1
        self.tabWidget.setCurrentIndex(previousTabIndex)

    def splitTabVertical(self):
        """
            This method splits the current tab in view into Vertical Layouts
        """
        print("this splits the tab vertical")

    def splitTabHorizontal(self):
        """
            This method splits the current tab in view into Horizontal panes
        """
        print("this splits the tab horizontal")


app = QApplication(sys.argv)
win = Konsole()
win.show()
app.exec_()