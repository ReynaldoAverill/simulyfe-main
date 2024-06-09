from userinterface.userinterface import Userinterface
from controller.controller import Controller
from model.model import Model

import logging
import os

# Set level for config
logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)

def main():
    logger.debug("Program Started")
    if os.environ.get('DISPLAY','') == '':
        logger.debug('no display found. Using :0.0')
        os.environ.__setitem__('DISPLAY', ':0.0')
        
    model = Model()
    userinterface = Userinterface('Simulyfe Anastomosis Training Kit',(800,480))
    # userinterface.switch_to("page_pump")
    # userinterface.start_mainloop()
    controller = Controller(model,userinterface)
    try:
        controller.start_app()
    except KeyboardInterrupt:
        logger.error("Program Stopped because of Keyboard Interrupt")
    finally:
        model.user_state.exit()
        # controller.exit_app(model.user_state)

if __name__ == "__main__":
    main()