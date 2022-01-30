from PyQt5 import QtCore, QtWidgets
from MessageClasses import Messages
from UIElements.StrategyInputs import StrategyInputBox
import os
from config import strategies

class GUIFunctions():

    def add_update_order(self,order):
        root = self.GUI.ordersDisplay.invisibleRootItem()
        child_count = root.childCount()
        for i in range(child_count):
            item = root.child(i)
            order_id = item.text(0)
            if(str(order_id) == str(order["order_id"])):
                keys=order.keys()
                for j in range(0,len(keys)):
                    item.setText(j, str(order[keys[j]]))
                return
        if(child_count==0):
            self.GUI.ordersDisplay.setHeaderLabels(list(order.keys()))
        item = QtWidgets.QTreeWidgetItem(self.GUI.ordersDisplay)
        for j in range(0, len(list(order.keys()))):
            item.setText(j, str(order[list(order.keys())[j]]))

    def add_user_message(self,message):
        item = QtWidgets.QTreeWidgetItem(self.GUI.userMessageDisplay)
        for j in range(0, len(list(message.keys()))):
            item.setText(j, str(message[list(message.keys())[j]]))

    def add_broker_message(self,message):
        item = QtWidgets.QTreeWidgetItem(self.GUI.brokerMessageDisplay)
        for j in range(0, len(list(message.keys()))):
            item.setText(j, str(message[list(message.keys())[j]]))

    def populateUserMessages(self):
        self.GUI.userMessageDisplay.clear();
        usermessages = Messages.getInstance().usermessages.getMessages()
        if (len(usermessages) != 0):
            headers = list(usermessages[0].keys())
            self.GUI.userMessageDisplay.clear()
            self.GUI.userMessageDisplay.setHeaderLabels(headers)
            for i in usermessages:
                item = QtWidgets.QTreeWidgetItem(self.GUI.userMessageDisplay)
                for j in range(0, len(headers)):
                    item.setText(j, str(i[headers[j]]))


    def populateBrokerMessages(self):
        self.GUI.brokerMessagesDisplay.clear();
        brokermessages = Messages.getInstance().brokermessages.getMessages()
        if (len(brokermessages) != 0):
            headers = list(brokermessages[0].keys())
            self.GUI.brokerMessagesDisplay.clear()
            self.GUI.brokerMessagesDisplay.setHeaderLabels(headers)
            for i in brokermessages:
                item = QtWidgets.QTreeWidgetItem(self.GUI.brokerMessagesDisplay)
                for j in range(0, len(headers)):
                    item.setText(j, str(i[headers[j]]))


    def populateOrders(self):
        orders = Messages.getInstance().orders.getMessages()
        self.GUI.ordersDisplay.clear()
        if (len(orders) != 0):
            headers = list(orders[0].keys())
            self.GUI.ordersDisplay.setHeaderLabels(headers)
            for i in orders:
                item = QtWidgets.QTreeWidgetItem(self.GUI.ordersDisplay)
                for j in range(0, len(headers)):
                    item.setText(j, str(i[headers[j]]))

    def populateTrades(self):
        orders = Messages.getInstance().trades.getMessages()
        if(len(orders)!=0):
            headers = list(orders[0].keys())
            self.GUI.tradesDisplay.clear()
            self.GUI.tradesDisplay.setHeaderLabels(headers)
            for i in orders:
                item = QtWidgets.QTreeWidgetItem(self.GUI.tradesDisplay)
                for j in range(0, len(headers)):
                    item.setText(j, str(i[headers[j]]))

    def populatePositions(self):
        positions = Messages.getInstance().positions.getMessages()
        if (len(positions) != 0):
            headers = list(positions[0].keys())
            self.GUI.positionsDisplay.clear()
            self.GUI.positionsDisplay.setHeaderLabels(headers)
            for i in positions:
                item = QtWidgets.QTreeWidgetItem(self.GUI.positionsDisplay)
                for j in range(0, len(headers)):
                    item.setText(j, str(i[headers[j]]))

    def populateStrategies(self):
        self.GUI.strategyBox.clear()
        self.GUI.strategyBox.setHeaderLabels(["Strategy"])
        keys=strategies.keys()
        print(keys)
        for i in range (0,len(keys)):
            item=QtWidgets.QTreeWidgetItem(self.GUI.strategyBox)
            item.setText(0,list(keys)[i])


    def startButtonClicked(self):
        print("start button clicked")
        root = self.GUI.strategyBox.invisibleRootItem()
        child_count = root.childCount()
        for i in range(child_count):
            item = root.child(i)
            checked=item.isSelected()
            strategy = item.text(0)
            strategy_to_execute = strategies[strategy]
            print(strategy_to_execute)
            if(checked):
                Dialog = QtWidgets.QDialog()
                ui = StrategyInputBox()
                strategy_to_execute = strategy_to_execute()
                ui.setupUi(Dialog,strategy_to_execute)
                inputs=strategy_to_execute.define_inputs()
                for input, value in inputs.items():
                    ui.addAttr(input, value)
                Dialog.exec()
                return
        error_dialog = QtWidgets.QErrorMessage()
        error_dialog.showMessage('Oh no! Nothing is clicked')
        error_dialog.exec()

    def createButtonClicked(self):
        print("CREATE CLICKED")

    def editButtonClicked(self):
        print("EDIT BUTTON CLICKED")

    def stopButtonClicked(self):
        print("STOP BUTTON CLICKED")

    def pauseButtonClicked(self):
        print("PAUSE BUTTON CLICKED")

    def stopAllButtonClicked(self):
        print("STOP ALL BUTTON CLICKED")

    def connect_components(self):
        self.GUI.startButton.clicked.connect(self.startButtonClicked)
        self.GUI.createButton.clicked.connect(self.createButtonClicked)
        self.GUI.editButton.clicked.connect(self.editButtonClicked)
        self.GUI.stopButton.clicked.connect(self.stopButtonClicked)
        self.GUI.stopAllButton.clicked.connect(self.stopAllButtonClicked)
        self.GUI.pauseButton.clicked.connect(self.pauseButtonClicked)

    def executeInitialFunctions(self,GUI=None):
        self.GUI=GUI
        self.populateTrades()
        self.populatePositions()
        self.populateUserMessages()
        self.populateBrokerMessages()
        self.populateOrders()
        self.populateStrategies()
        self.connect_components()

    __instance = None

    @staticmethod
    def get_instance():
        if GUIFunctions.__instance == None:
            GUIFunctions()
        return GUIFunctions.__instance

    def __init__(self):
        if GUIFunctions.__instance != None:
            raise Exception("This class is a singleton!")
        else:
            GUIFunctions.__instance = self

