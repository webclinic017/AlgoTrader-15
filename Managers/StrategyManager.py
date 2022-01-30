import threading

from MessageClasses import Messages


class StrategyManager():

    latest_portfolio_id=0;
    strategy_map={}

    def add_strategy(self,strategy):
           self.latest_portfolio_id+=1
           strategy.portfolio_id=self.latest_portfolio_id
           self.strategy_map[self.latest_portfolio_id]=strategy

    def start_strategy(self,strategy,inputs):
        threading.Thread(target=strategy.main,args=[inputs]).start()
        Messages.getInstance().usermessages.info("STARTING STARTEGY "+str(strategy.__class__) +" INPUTS "+ str(inputs) )
        pass

    __instance = None

    @staticmethod
    def get_instance():
        if StrategyManager.__instance == None:
            StrategyManager()
        return StrategyManager.__instance

    def __init__(self):
        if StrategyManager.__instance != None:
            raise Exception("This class is a singleton!")
        else:
            StrategyManager.__instance = self
