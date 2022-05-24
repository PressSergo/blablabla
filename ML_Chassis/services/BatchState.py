from enum import Enum

class BatchState(Enum):
    CREATED = 1
    ENRICH = 2
    TARGET_COMPUTED = 3