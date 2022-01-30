import schedule
import datetime
from Managers.MarketDataManager import MarketDataManager
from core_classes.Enums import StrategyState
import time

class Strategy():

    portfolio_id=1;
    state=StrategyState.STOPPED

    def define_inputs(self):
        pass

    def stop(self):
        self.state = StrategyState.STOPPED
        pass

    def stop_with_squareoff(self):
        pass

    def pause(self):
        pass

    def pause_with_squareoff(self):
        pass

    def get_total_pnl(self):
        pass

    def get_unrealized_pnl(self):
        pass

    def get_realized_pnl(self):
        pass

    def on_create(self,inputs):
        pass

    def subscribe(self,instrument,callback):
        MarketDataManager.get_instance().subscribe(instrument,callback)

    def schedule_tasks(self):
        pass

    def main(self,inputs):
        print(" STARTED:  " + str(datetime.datetime.now()))
        self.on_create(inputs)
        self.schedule=schedule
        self.schedule_tasks()
        from Managers.BrokerManager import BrokerManager
        self.brokers = BrokerManager.get_instance().get_broker()
        while True:
            # if(self.state=="RUNNING"):
            #     time.sleep(0.1)
                schedule.run_pending()

