# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'UI.ui'
#
# Created by: PyQt5 UI code generator 5.15.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.
from PyQt5 import QtCore, QtGui, QtWidgets
from GUIFunctions import GUIFunctions

class Ui_MainWindow(object):

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1021, 766)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setAutoFillBackground(False)
        MainWindow.setDocumentMode(False)
        MainWindow.setTabShape(QtWidgets.QTabWidget.Rounded)
        MainWindow.setDockNestingEnabled(False)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setMinimumSize(QtCore.QSize(1021, 711))
        font = QtGui.QFont()
        font.setPointSize(13)
        font.setBold(False)
        font.setWeight(50)
        self.tabWidget.setFont(font)
        self.tabWidget.setTabPosition(QtWidgets.QTabWidget.North)
        self.tabWidget.setTabShape(QtWidgets.QTabWidget.Rounded)
        self.tabWidget.setIconSize(QtCore.QSize(15, 16))
        self.tabWidget.setElideMode(QtCore.Qt.ElideRight)
        self.tabWidget.setUsesScrollButtons(False)
        self.tabWidget.setDocumentMode(True)
        self.tabWidget.setTabsClosable(False)
        self.tabWidget.setMovable(True)
        self.tabWidget.setTabBarAutoHide(False)
        self.tabWidget.setObjectName("tabWidget")
        self.dashboardTab = QtWidgets.QWidget()
        self.dashboardTab.setObjectName("dashboardTab")
        self.gridLayout_6 = QtWidgets.QGridLayout(self.dashboardTab)
        self.gridLayout_6.setObjectName("gridLayout_6")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.gridLayout_6.addLayout(self.verticalLayout_2, 2, 0, 1, 1)
        self.splitter_2 = QtWidgets.QSplitter(self.dashboardTab)
        self.splitter_2.setOrientation(QtCore.Qt.Vertical)
        self.splitter_2.setObjectName("splitter_2")
        self.frame_2 = QtWidgets.QFrame(self.splitter_2)
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.gridLayout_7 = QtWidgets.QGridLayout(self.frame_2)
        self.gridLayout_7.setObjectName("gridLayout_7")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.startButton = QtWidgets.QPushButton(self.frame_2)
        self.startButton.setCheckable(False)
        self.startButton.setChecked(False)
        self.startButton.setObjectName("startButton")
        self.horizontalLayout_2.addWidget(self.startButton)
        self.editButton = QtWidgets.QPushButton(self.frame_2)
        self.editButton.setObjectName("editButton")
        self.horizontalLayout_2.addWidget(self.editButton)
        self.createButton = QtWidgets.QPushButton(self.frame_2)
        self.createButton.setObjectName("createButton")
        self.horizontalLayout_2.addWidget(self.createButton)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem)
        self.stopButton = QtWidgets.QPushButton(self.frame_2)
        self.stopButton.setObjectName("stopButton")
        self.horizontalLayout_2.addWidget(self.stopButton)
        self.stopAllButton = QtWidgets.QPushButton(self.frame_2)
        self.stopAllButton.setObjectName("stopAllButton")
        self.horizontalLayout_2.addWidget(self.stopAllButton)
        self.pauseButton = QtWidgets.QPushButton(self.frame_2)
        self.pauseButton.setObjectName("pauseButton")
        self.horizontalLayout_2.addWidget(self.pauseButton)
        self.gridLayout_7.addLayout(self.horizontalLayout_2, 1, 0, 1, 1)
        self.splitter_3 = QtWidgets.QSplitter(self.frame_2)
        self.splitter_3.setOrientation(QtCore.Qt.Horizontal)
        self.splitter_3.setObjectName("splitter_3")
        self.strategyBox = QtWidgets.QTreeWidget(self.splitter_3)
        self.strategyBox.setMaximumSize(QtCore.QSize(200, 16777215))
        self.strategyBox.setObjectName("strategyBox")
        item_0 = QtWidgets.QTreeWidgetItem(self.strategyBox)
        item_0.setCheckState(0, QtCore.Qt.Unchecked)
        self.layoutWidget = QtWidgets.QWidget(self.splitter_3)
        self.layoutWidget.setObjectName("layoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.layoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.statusLabel = QtWidgets.QLabel(self.layoutWidget)
        self.statusLabel.setObjectName("statusLabel")
        self.horizontalLayout.addWidget(self.statusLabel)
        self.label_7 = QtWidgets.QLabel(self.layoutWidget)
        self.label_7.setObjectName("label_7")
        self.horizontalLayout.addWidget(self.label_7)
        self.label_8 = QtWidgets.QLabel(self.layoutWidget)
        self.label_8.setObjectName("label_8")
        self.horizontalLayout.addWidget(self.label_8)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.runningStrategyBox = QtWidgets.QTreeWidget(self.layoutWidget)
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(230, 230, 230))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(230, 230, 230))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Light, brush)
        brush = QtGui.QBrush(QtGui.QColor(230, 230, 230))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(230, 230, 230))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Light, brush)
        brush = QtGui.QBrush(QtGui.QColor(230, 230, 230))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(230, 230, 230))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Light, brush)
        self.runningStrategyBox.setPalette(palette)
        self.runningStrategyBox.setObjectName("runningStrategyBox")
        self.verticalLayout.addWidget(self.runningStrategyBox)
        self.gridLayout_7.addWidget(self.splitter_3, 0, 0, 1, 1)
        self.splitter = QtWidgets.QSplitter(self.splitter_2)
        self.splitter.setOrientation(QtCore.Qt.Horizontal)
        self.splitter.setObjectName("splitter")
        self.brokerInformation = QtWidgets.QTabWidget(self.splitter)
        self.brokerInformation.setObjectName("brokerInformation")
        self.Orders = QtWidgets.QWidget()
        self.Orders.setObjectName("Orders")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.Orders)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.ordersDisplay = QtWidgets.QTreeWidget(self.Orders)
        self.ordersDisplay.setDragEnabled(True)
        self.ordersDisplay.setObjectName("ordersDisplay")
        item_0 = QtWidgets.QTreeWidgetItem(self.ordersDisplay)
        item_0 = QtWidgets.QTreeWidgetItem(self.ordersDisplay)
        self.gridLayout_2.addWidget(self.ordersDisplay, 0, 0, 1, 1)
        self.brokerInformation.addTab(self.Orders, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.tab_2)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.tradesDisplay = QtWidgets.QTreeWidget(self.tab_2)
        self.tradesDisplay.setObjectName("tradesDisplay")
        item_0 = QtWidgets.QTreeWidgetItem(self.tradesDisplay)
        item_0 = QtWidgets.QTreeWidgetItem(self.tradesDisplay)
        self.gridLayout_3.addWidget(self.tradesDisplay, 0, 0, 1, 1)
        self.brokerInformation.addTab(self.tab_2, "")
        self.tab_4 = QtWidgets.QWidget()
        self.tab_4.setObjectName("tab_4")
        self.gridLayout_9 = QtWidgets.QGridLayout(self.tab_4)
        self.gridLayout_9.setObjectName("gridLayout_9")
        self.positionsDisplay = QtWidgets.QTreeWidget(self.tab_4)
        self.positionsDisplay.setObjectName("positionsDisplay")
        item_0 = QtWidgets.QTreeWidgetItem(self.positionsDisplay)
        item_0 = QtWidgets.QTreeWidgetItem(self.positionsDisplay)
        self.gridLayout_9.addWidget(self.positionsDisplay, 0, 0, 1, 1)
        self.brokerInformation.addTab(self.tab_4, "")
        self.brokerMessageDisplay = QtWidgets.QTabWidget(self.splitter)
        self.brokerMessageDisplay.setObjectName("brokerMessageDisplay")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.gridLayout_4 = QtWidgets.QGridLayout(self.tab)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.userMessageDisplay = QtWidgets.QTreeWidget(self.tab)
        self.userMessageDisplay.setDragEnabled(True)
        self.userMessageDisplay.setUniformRowHeights(False)
        self.userMessageDisplay.setObjectName("userMessageDisplay")
        item_0 = QtWidgets.QTreeWidgetItem(self.userMessageDisplay)
        item_0 = QtWidgets.QTreeWidgetItem(self.userMessageDisplay)
        self.userMessageDisplay.header().setHighlightSections(False)
        self.gridLayout_4.addWidget(self.userMessageDisplay, 0, 0, 1, 1)
        self.brokerMessageDisplay.addTab(self.tab, "")
        self.tab_3 = QtWidgets.QWidget()
        self.tab_3.setObjectName("tab_3")
        self.gridLayout_5 = QtWidgets.QGridLayout(self.tab_3)
        self.gridLayout_5.setObjectName("gridLayout_5")
        self.brokerMessagesDisplay = QtWidgets.QTreeWidget(self.tab_3)
        self.brokerMessagesDisplay.setObjectName("brokerMessagesDisplay")
        item_0 = QtWidgets.QTreeWidgetItem(self.brokerMessagesDisplay)
        item_0 = QtWidgets.QTreeWidgetItem(self.brokerMessagesDisplay)
        item_0 = QtWidgets.QTreeWidgetItem(self.brokerMessagesDisplay)
        self.gridLayout_5.addWidget(self.brokerMessagesDisplay, 0, 0, 1, 1)
        self.brokerMessageDisplay.addTab(self.tab_3, "")
        self.gridLayout_6.addWidget(self.splitter_2, 0, 0, 1, 1)
        self.tabWidget.addTab(self.dashboardTab, "")
        self.gridLayout.addWidget(self.tabWidget, 0, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1021, 22))
        self.menubar.setObjectName("menubar")
        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        self.menuView = QtWidgets.QMenu(self.menubar)
        self.menuView.setObjectName("menuView")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionSettings = QtWidgets.QAction(MainWindow)
        self.actionSettings.setObjectName("actionSettings")
        self.actionBroker_Configuration = QtWidgets.QAction(MainWindow)
        self.actionBroker_Configuration.setObjectName("actionBroker_Configuration")
        self.menuFile.addAction(self.actionSettings)
        self.menuFile.addAction(self.actionBroker_Configuration)
        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuView.menuAction())
        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(0)
        self.brokerInformation.setCurrentIndex(2)
        self.brokerMessageDisplay.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        GUIFunctions.get_instance().executeInitialFunctions(GUI=self)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.startButton.setText(_translate("MainWindow", "START"))
        self.editButton.setText(_translate("MainWindow", "EDIT"))
        self.createButton.setText(_translate("MainWindow", "CREATE"))
        self.stopButton.setText(_translate("MainWindow", "STOP"))
        self.stopAllButton.setText(_translate("MainWindow", "STOP ALL"))
        self.pauseButton.setText(_translate("MainWindow", "PAUSE"))
        self.strategyBox.headerItem().setText(0, _translate("MainWindow", "STRATEGY"))
        __sortingEnabled = self.strategyBox.isSortingEnabled()
        self.strategyBox.setSortingEnabled(False)
        # self.strategyBox.topLevelItem(0).setText(0, _translate("MainWindow", "MASQ"))
        self.strategyBox.setSortingEnabled(__sortingEnabled)
        # self.statusLabel.setText(_translate("MainWindow", "Strategy: MASQ"))
        # self.label_7.setText(_translate("MainWindow", "Total PNL : 1414"))
        self.label_8.setText(_translate("MainWindow", "Mode : LIVE"))
        self.runningStrategyBox.headerItem().setText(0, _translate("MainWindow", "portfolio_id"))
        self.runningStrategyBox.headerItem().setText(1, _translate("MainWindow", "state"))
        # self.runningStrategyBox.headerItem().setText(2, _translate("MainWindow", "SYMBOL"))
        # self.runningStrategyBox.headerItem().setText(3, _translate("MainWindow", "QUANTITY"))
        # self.runningStrategyBox.headerItem().setText(4, _translate("MainWindow", "START"))
        # self.runningStrategyBox.headerItem().setText(5, _translate("MainWindow", "END"))
        # self.runningStrategyBox.headerItem().setText(6, _translate("MainWindow", "EMA1"))
        # self.runningStrategyBox.headerItem().setText(7, _translate("MainWindow", "EMA2"))
        # self.runningStrategyBox.headerItem().setText(8, _translate("MainWindow", "RR"))
        # self.runningStrategyBox.headerItem().setText(9, _translate("MainWindow", "TSL"))
        # self.runningStrategyBox.headerItem().setText(10, _translate("MainWindow", "POSITION"))
        # self.runningStrategyBox.headerItem().setText(11, _translate("MainWindow", "PNL"))
        self.ordersDisplay.headerItem().setText(0, _translate("MainWindow", "TIME"))
        self.ordersDisplay.headerItem().setText(1, _translate("MainWindow", "SYMBOL"))
        self.ordersDisplay.headerItem().setText(2, _translate("MainWindow", "SIDE"))
        self.ordersDisplay.headerItem().setText(3, _translate("MainWindow", "STATUS"))
        self.ordersDisplay.headerItem().setText(4, _translate("MainWindow", "PRICE"))
        self.ordersDisplay.headerItem().setText(5, _translate("MainWindow", "QTY"))
        self.brokerInformation.setTabText(self.brokerInformation.indexOf(self.Orders), _translate("MainWindow", "Orders"))
        self.tradesDisplay.headerItem().setText(0, _translate("MainWindow", "TIME"))
        self.tradesDisplay.headerItem().setText(1, _translate("MainWindow", "SYMBOL"))
        self.tradesDisplay.headerItem().setText(2, _translate("MainWindow", "SIDE"))
        self.tradesDisplay.headerItem().setText(3, _translate("MainWindow", "STATUS"))
        self.tradesDisplay.headerItem().setText(4, _translate("MainWindow", "PRICE"))
        self.tradesDisplay.headerItem().setText(5, _translate("MainWindow", "QTY"))
        self.brokerInformation.setTabText(self.brokerInformation.indexOf(self.tab_2), _translate("MainWindow", "Trades"))
        self.positionsDisplay.headerItem().setText(0, _translate("MainWindow", "SYMBOL"))
        self.positionsDisplay.headerItem().setText(1, _translate("MainWindow", "POSITION"))
        self.positionsDisplay.headerItem().setText(2, _translate("MainWindow", "PRICE"))
        self.positionsDisplay.headerItem().setText(3, _translate("MainWindow", "QTY"))
        self.brokerInformation.setTabText(self.brokerInformation.indexOf(self.tab_4), _translate("MainWindow", "Positions"))
        self.userMessageDisplay.headerItem().setText(0, _translate("MainWindow", "TYPE"))
        self.userMessageDisplay.headerItem().setText(1, _translate("MainWindow", "TIME"))
        self.userMessageDisplay.headerItem().setText(2, _translate("MainWindow", "MESSAGE"))
        self.brokerMessageDisplay.setTabText(self.brokerMessageDisplay.indexOf(self.tab), _translate("MainWindow", "System Messages"))
        self.brokerMessagesDisplay.headerItem().setText(0, _translate("MainWindow", "TYPE"))
        self.brokerMessagesDisplay.headerItem().setText(1, _translate("MainWindow", "TIME"))
        self.brokerMessagesDisplay.headerItem().setText(2, _translate("MainWindow", "MESSAGE"))
        self.brokerMessageDisplay.setTabText(self.brokerMessageDisplay.indexOf(self.tab_3), _translate("MainWindow", "Broker Messages"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.dashboardTab), _translate("MainWindow", "Dashboard"))
        self.menuFile.setTitle(_translate("MainWindow", "File"))
        self.menuView.setTitle(_translate("MainWindow", "View"))
        self.actionSettings.setText(_translate("MainWindow", "Settings"))
        self.actionBroker_Configuration.setText(_translate("MainWindow", "Broker Configuration"))

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
