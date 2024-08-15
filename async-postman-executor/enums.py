from enum import Enum
class TaskStatus(Enum):
    NOT_STARTED="NOT_STARTED"
    IN_PROGRESS="IN_PROGRESS"
    SUCCESS="SUCCESS"
    FAILED="FAILED"