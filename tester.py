from abc import abstractmethod


class Broker():

    @abstractmethod
    def get_ltp(self):
        print("LTP REQUESTED")
        pass
class ZerodhaBroker(Broker):

    pass


broker=ZerodhaBroker()
broker.get_ltp()