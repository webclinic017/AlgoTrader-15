from enum import Enum

class StrategyState(Enum):
    CREATED = "CREATED"
    RUNNING = "RUNNING"
    STOPPED = "STOPPED"
    PAUSE = "PAUSE"
