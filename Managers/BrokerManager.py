from Brokers.PaperTrading import PaperTradingBroker
from Brokers.ZerodhaBroker import ZerodhaBroker
from config import broker

class BrokerManager():

    __brokers = { }
    __datasource = None

    def get_broker(self):
        return self.__datasource

    def __load_brokers_from_config(self):
            if(broker["broker"]=="ZERODHA"):
                self.__brokers[broker["broker_alias"]]=ZerodhaBroker(broker["config"])
                self.__brokers[broker["broker_alias"]].connect()
            elif(broker["broker"]=="PAPER"):
                self.__brokers[broker["broker_alias"]]=PaperTradingBroker(broker["config"])
            self.__datasource=self.__brokers[broker["broker_alias"]]
    __instance = None

    @staticmethod
    def get_instance():
        if BrokerManager.__instance == None:
            BrokerManager()
        return BrokerManager.__instance

    def __init__(self):
        if BrokerManager.__instance != None:
            raise Exception("This class is a singleton!")
        else:
            BrokerManager.__instance = self
        self.__load_brokers_from_config()
        self.__datasource.load_instruments()
        print(len(self.__brokers))

if __name__=="__main__":
    BrokerManager.get_instance()