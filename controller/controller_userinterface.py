from .controller_page_main import Controller_page_main
from .controller_page_anastomosis import Controller_page_anastomosis
from .controller_page_confirmation_anastomosis_to_main import Controller_page_confirmation_anastomosis_to_main
from .controller_page_confirmation_anastomosis_to_pump import Controller_page_confirmation_anastomosis_to_pump
from .controller_base import Controller_base
from model.user_state import User_state

import logging

logger = logging.getLogger(__name__)

class Controller_userinterface(Controller_base):
    def __init__(self, model, userinterface):
        super().__init__(model,userinterface)
        self.pagecontroller_classes = {
            "page_main" : Controller_page_main,
            "page_anastomosis" : Controller_page_anastomosis,
            "page_confirmation_anastomosis_to_main" : Controller_page_confirmation_anastomosis_to_main,
            "page_confirmation_anastomosis_to_pump" : Controller_page_confirmation_anastomosis_to_pump
        }
        self.current_pagecontroller = None
        self.add_controller_userinterface_event_listener()
    
    def add_controller_userinterface_event_listener(self):
        self.model.user_state.add_event_listener("move_to_new_page",self.movepage_and_constructcontroller)
        self.model.user_state.add_event_listener("exit_app",self.exit_app)

    def movepage_and_constructcontroller(self,user_state: User_state):
        logger.info("Processing to Move to "+str(user_state.state))
        self.userinterface.switch_to(str(user_state.state))
        new_controller = self.pagecontroller_classes[user_state.state](self.model,self.userinterface)
        self.current_pagecontroller = new_controller
    
    def exit_app(self,user_state: User_state):
        logger.info("Processing to close the app")
        self.userinterface.exit_app()
