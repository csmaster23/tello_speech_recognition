

# constants
UP = "up"
UPWARD = "upward"
DOWN = "down"
DOWNWARD = "downward"
LEFT = "left"
RIGHT = "right"
WRITE = "write"
FORWARD = "forward"
BACKWARD = "backward"
BACK = "back"
CW = "cw"
CLOCKWISE = "clockwise"
CCW = "ccw"
COUNTER_CLOCKWISE = "counterclockwise"
#FLIP = "flip"

TAKEOFF = "takeoff"
TAKE_OFF = "take off"
#TAKE = "take"
LAND = "land"
EMERGENCY = "emergency"

GET = "get"
SPEED = "speed"
BATTERY = "battery"
TIME = "time"
HEIGHT = "height"
TEMP = "temp"
TEMPERATURE = "temperature"
ATTITUDE = "attitude"
BARO = "baro"
BARROW = "barrow"
ACCELERATION = "acceleration"
TOF = "tof"
TIME_OF_FLIGHT = "time of flight"
WIFI = "Wi-Fi"

MOVE = "move"
FLY = "fly"
GO = "go"
PULL = "pull"
DIP = "dip"
ROTATE = "rotate"
SPIN = "spin"
TURN = "turn"
#FLIP_AROUND = "flip around"

AND = "and"
DON_T = "don't"
DO_NOT = "do not"

SURVEILLANCE_MODE = "enter surveillance mode"

CONSTANTS = [ UP, UPWARD, DOWN, DOWNWARD, LEFT, RIGHT, WRITE, FORWARD, BACKWARD,
            CW, CLOCKWISE, CCW, COUNTER_CLOCKWISE, TAKEOFF, TAKE_OFF,
            LAND, EMERGENCY, GET, SPEED, BATTERY, TIME, HEIGHT, TEMP,
            TEMPERATURE, ATTITUDE, BARO, BARROW, ACCELERATION, TOF, TIME_OF_FLIGHT,
            WIFI, SURVEILLANCE_MODE, AND, DON_T, DO_NOT ]

MOVEMENT = [ UP, UPWARD, DOWN, DOWNWARD, LEFT, RIGHT, WRITE, FORWARD, BACKWARD, BACK,
            CW, CLOCKWISE, CCW, COUNTER_CLOCKWISE, MOVE, FLY, GO, PULL,
            DIP, ROTATE, SPIN, TURN ]

FINAL_MOVEMENT_COMMANDS = [ UP, DOWN, LEFT, RIGHT, FORWARD, BACK, CW, CCW ]

NON_MOVEMENT = [ GET, SPEED, BATTERY, TIME, HEIGHT, TEMP, TEMPERATURE, ATTITUDE,
                BARO, BARROW, ACCELERATION, TOF, TIME_OF_FLIGHT, WIFI, TAKEOFF, TAKE_OFF,
                LAND, EMERGENCY, SURVEILLANCE_MODE ]


CUSTOM = [ SURVEILLANCE_MODE ]

FLAGGED_WORDS = [ AND, DON_T, DO_NOT ]
