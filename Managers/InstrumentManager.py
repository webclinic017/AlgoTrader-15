from Models.Models import Instrument


class InstrumentManager():
    
    instrument_list=[]

    def get_instrument_from_symbol(self,symbol):
        for instrument in self.instrument_list:
            if(instrument.trading_symbol==symbol):
                return instrument
        return None

    def find_instrument(self,symbol=None,token=None):
        if(symbol!=None):
            for instrument in self.instrument_list:
                if instrument.tradingsymbol == symbol:
                    return instrument
        elif(token!=None):
            for instrument in self.instrument_list:
                if str(instrument.instrument_token) == str(token):
                    return instrument
        raise Exception("INSTRUMENT NOT FOUND "+str(symbol)+str(token))

    def add_instrument(self,instrument):
        if isinstance(instrument,Instrument):
            self.instrument_list.append(instrument)
        else:
            raise Exception( " Required Type Instrument" )
        pass

    __instance = None

    @staticmethod
    def get_instance():
        if InstrumentManager.__instance == None:
            InstrumentManager()
        return InstrumentManager.__instance

    def __init__(self):
        if InstrumentManager.__instance != None:
            raise Exception("This class is a singleton!")
        else:
            InstrumentManager.__instance = self

if __name__=="main":
    InstrumentManager.get_instance()