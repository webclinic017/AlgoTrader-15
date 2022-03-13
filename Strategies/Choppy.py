import schedule
import pandas as pd
# from Managers.BrokerManager import
from Managers.InstrumentManager import InstrumentManager
from Core.Strategy import Strategy


class ChoppyLevels:
    r1 = "r1"
    r2 = "r2"
    r3 = "r3"
    r4 = "r4"
    pdh = "pdh"
    pdl = "pdl"
    bc = "bc"
    tc = "tc"
    s1 = "s1"
    s2 = "s2"
    s3 = "s3"
    s4 = "s4"


class Choppy(Strategy):

    def on_create(self,inputs):
        input_file = inputs['input_file']
        input_df = None
        if input_file.endswith('.csv'):
            input_df = pd.read_csv(input_file)
        elif input_file.endswith('.xlsx'):
            input_df = pd.read_excel(input_file)
        print("on create for choppy called")

    def define_inputs(self):
        return {
            "input_file" : "starter.xlsx",
        }

    def on_start(self):
        print("Start function for choppy called")
        pass

    def on_ticks(self, ticks):
        print("TICKS RECEIVED " + str(ticks))

    def schedule_tasks(self):
        print(f"SCHEDULE TASKS CALLED {self.portfolio_id}")
