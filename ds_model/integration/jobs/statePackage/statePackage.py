from enum import Enum

class StatePackage(Enum):
    READY = 1
    READY_FOR_ENRICH = 2
    ENRICH = 3