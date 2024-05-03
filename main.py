from userinterface.userinterface import Userinterface
from controller.controller_userinterface import Controller_userinterface
from model.model import Model
from test_module.stopwatch_test import start_stopwatch_test

import logging
import os

# Set level for config
logging.basicConfig(level=logging.CRITICAL)
logger = logging.getLogger(__name__)

def main():
    logger.debug("Program Started")
    if os.environ.get('DISPLAY','') == '':
        logger.debug('no display found. Using :0.0')
        os.environ.__setitem__('DISPLAY', ':0.0')
    model = Model()
    userinterface = Userinterface('Simulyfe Anastomosis Training Kit',(800,480))
    controller = Controller_userinterface(model,userinterface)
    controller.start_app()
    # start_stopwatch_test()

    # userinterface.switch_to("page_confirmation_anastomosis_to_main")
    # userinterface.switch_to("page_main")
    # userinterface.start_mainloop()

if __name__ == "__main__":
    main()