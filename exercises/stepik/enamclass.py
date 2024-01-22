from enum import Enum
 
class Season(Enum):
    SPRING = 1
    SUMMER = 2
    AUTUMN = 3
    WINTER = 4
 
print(Season.SPRING)
print(Season.SPRING.name)
print(Season.SPRING.value)

from enum import Enum


class Direction(Enum):
    NORTH = "N"
    SOUTH = "S"
    EAST = "E"
    WEST = "W"


print(Direction.WEST.value)
print(Direction.SOUTH.value)