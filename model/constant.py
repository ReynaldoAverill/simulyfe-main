# OS Constant
RASPBERRYPI = True
FULLSCREEN = True

# Pump Constant
PIN_PWM = 13
FREQ_PWM = 1000
PIN_PUMP_ENABLE_A = 19
PIN_PUMP_ENABLE_B = 26
DIR_A_TO_B = True
MAX_DIGIT_DEBIT = 3
DEBIT_UNIT = "ml/min"
MIN_DEBIT = 10
MAX_DEBIT = 52

# Flow sensor constant
CREATE_COMMAND_RASPBERRY    = ['sudo','make']
RUN_COMMAND_RASPBERRY       = ['./version7']
CREATE_COMMAND_WINDOWS      = ['gcc','-o','client_windows','client_windows.c','-lws2_32']
RUN_COMMAND_WINDOWS         = [".\client_windows"]
# CREATE_COMMAND  = ['gcc','client_raspberry.c','-o','client_raspberry']
# RUN_COMMAND     = ["./client_raspberry"]

HOST        = '127.0.0.1' # Standard loopback interface address (localhost)
PORT        = 65432 # Port to listen on (non-privileged ports are > 1023)

# Force Sensor Constant
MEDIUM_START    = 11
STRONG_START    = 16 

ACTIVE_LEFT     = True
D_OUT_LEFT      = 22
PD_SCK_LEFT     = 10
REF_UNIT_LEFT   = 7371

ACTIVE_RIGHT    = True
D_OUT_RIGHT     = 17
PD_SCK_RIGHT    = 27
REF_UNIT_RIGHT  = 6563

# Camera Constant
FRAME_WIDTH     = 640
FRAME_HEIGHT    = 480
FPS             = 30.0
FORMAT          = 'mp4v'
EXTERNAL        = False
EXTERNAL_PATH   = '/media/simulyfe/DATAVIDEO'

