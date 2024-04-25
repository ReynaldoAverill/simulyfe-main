from userinterface.userinterface import Userinterface
import logging

# Set level for config
logging.basicConfig(level=logging.DEBUG)

def main():
    userinterface = Userinterface('Simulyfe Anastomosis Training Kit',(800,480))
    userinterface.switch_to("page_main")
    userinterface.start_mainloop()

if __name__ == "__main__":
    main()