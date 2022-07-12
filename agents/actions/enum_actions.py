from enum import Enum
class LocalizationActions(Enum):
    Stop = 0
    IncreaseTop = 1
    IncreaseBottom = 2
    IncreaseLeft = 3
    IncreaseRight = 4
    IncreaseVertical = 5
    Increase
    
    
class PoseActions(Enum):
    Stop = 0
    MoveNoseLeft = 1
    MoveNoseRight = 2
    MoveNoseTop = 3
    MoveNoseBottom = 4
    