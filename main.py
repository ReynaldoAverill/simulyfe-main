from userinterface.userinterface import Userinterface
from controller.controller_page_main import Controller_page_main
import logging

# Set level for config
logging.basicConfig(level=logging.DEBUG)

def main():
    userinterface = Userinterface('Simulyfe Anastomosis Training Kit',(800,480))
    # model = None
    # controller = Controller_page_main(userinterface)

    # userinterface.switch_to("page_confirmation_anastomosis_to_main")
    userinterface.switch_to("page_anastomosis")
    userinterface.start_mainloop()

if __name__ == "__main__":
    main()