from Managers.BrokerManager import BrokerManager
from Managers.InstrumentManager import InstrumentManager
from Managers.MarketDataManager import MarketDataManager
from Managers.OrderManager import OrderManager


class Manager():

    def __init__(self):
        MarketDataManager.get_instance()
        InstrumentManager.get_instance()
        BrokerManager.get_instance()
        MarketDataManager.get_instance().initialize_datasource(BrokerManager.get_instance().get_broker())
        OrderManager.get_instance()
print(__name__)
if __name__=="__main__":
    print("manager called")
    Manager()