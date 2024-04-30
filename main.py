from userinterface.userinterface import Userinterface
from controller.controller_userinterface import Controller_userinterface
from model.model import Model

import logging

# Set level for config
logging.basicConfig(level=logging.DEBUG)

def main():
    model = Model()
    userinterface = Userinterface('Simulyfe Anastomosis Training Kit',(800,480))
    controller = Controller_userinterface(model,userinterface)
    controller.start_app()

    # userinterface.switch_to("page_confirmation_anastomosis_to_main")
    # userinterface.switch_to("page_main")
    # userinterface.start_mainloop()

if __name__ == "__main__":
    main()