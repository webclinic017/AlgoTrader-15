import threading
import time
import datetime
import schedule
# from Managers.BrokerManager import BrokerManager
from Managers.InstrumentManager import InstrumentManager
from Managers.MarketDataManager import MarketDataManager
from Managers.OrderManager import OrderManager
from MessageClasses import Messages
from Models.Models import Instrument, Order
from core_classes.Strategy import Strategy
import functools
import time

def timer(func):
    """ Print the runtime of the decorated function """
    @functools.wraps(func)
    def wrapper_timer(*args, **kwargs):
        start_time = time.perf_counter()    # 1
        value = func(*args, **kwargs)
        end_time = time.perf_counter()      # 2
        run_time = end_time - start_time    # 3
        print(f"Finished {func.__name__!r} in {run_time:.4f} secs")
        return value
    return wrapper_timer

class DemoStrategy(Strategy):

    def define_inputs(self):
        return {
            "x":5,
            "y":14
        }

    def on_create(self,inputs):
        self.x=inputs["x"]
        pass

    def on_start(self):
        print("Start function called")
        pass

    def every_second(self):
        print("every second called portfolio "+str(self.portfolio_id)+"  "+str(datetime.datetime.now()))
        Messages.getInstance().usermessages.info("every second called portfolio "+str(self.portfolio_id)+"  "+str(datetime.datetime.now()))
        # order=Order(order_id=1232,status=self.state)
        # Messages.getInstance().orders.addOrder(order)

    def on_ticks(self, ticks):
        print("TICKS RECEIVED " + str(ticks))

    def schedule_tasks(self):
        print(f"SCHEDULE TASKS CALLED {self.portfolio_id}")
        # t=threading.Timer(int(self.x),self.every_second).start()
        # t.
        schedule.every(int(self.x)).seconds.do(self.every_second)
        # self.subscribe(Instrument(symbol="RELIANCE"),self.on_ticks)

if __name__=="__main__":
    InstrumentManager.get_instance()
    # BrokerManager.get_instance()
    time.sleep(0.5)
    MarketDataManager.get_instance()
    OrderManager.get_instance()
    strategy = DemoStrategy()
    # strategy.main()
    # strategy.on_create()
