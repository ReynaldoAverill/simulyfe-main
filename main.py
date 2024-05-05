from userinterface.userinterface import Userinterface
from controller.controller import Controller
from model.model import Model
from userinterface.page_confirmation_anastomosis_to_pump import Page_confirmation_anastomosis_to_pump

import logging
import os

# Set level for config
logging.basicConfig(level=logging.ERROR)
logger = logging.getLogger(__name__)

def main():
    logger.debug("Program Started")
    if os.environ.get('DISPLAY','') == '':
        logger.debug('no display found. Using :0.0')
        os.environ.__setitem__('DISPLAY', ':0.0')
        
    model = Model()
    userinterface = Userinterface('Simulyfe Anastomosis Training Kit',(800,480))
    # userinterface.switch_to("page_confirmation_pump_to_anastomosis")
    # userinterface.start_mainloop()
    controller = Controller(model,userinterface)
    controller.start_app()

    # userinterface.switch_to("page_confirmation_anastomosis_to_main")
    # userinterface.switch_to("page_main")
    # userinterface.start_mainloop()

if __name__ == "__main__":
    main()