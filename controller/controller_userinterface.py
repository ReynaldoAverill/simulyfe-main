from .controller_base import Controller_base
from .controller_page_main import Controller_page_main
from .controller_page_other_menu import Controller_page_other_menu
from .controller_page_action_history import Controller_page_action_history
from .controller_page_help import Controller_page_help
from .controller_page_anastomosis import Controller_page_anastomosis
from .controller_page_confirmation_anastomosis_to_main import Controller_page_confirmation_anastomosis_to_main
from .controller_page_confirmation_anastomosis_to_pump import Controller_page_confirmation_anastomosis_to_pump
from .controller_page_confirmation_pump_to_anastomosis import Controller_page_confirmation_pump_to_anastomosis
from .controller_page_confirmation_pump_to_training_summary import Controller_page_confirmation_pump_to_training_summary
from .controller_page_pump import Controller_page_pump
from .controller_page_enter_debit import Controller_page_enter_debit
from .controller_page_training_summary import Controller_page_training_summary
from model.user_state import User_state

import logging

logger = logging.getLogger(__name__)

class Controller_userinterface(Controller_base):
    def __init__(self, model, userinterface):
        super().__init__(model,userinterface)
        self.pagecontroller_classes = {
            "page_main" : Controller_page_main,
            "page_other_menu" : Controller_page_other_menu,
            "page_action_history" : Controller_page_action_history,
            "page_help" : Controller_page_help,
            "page_anastomosis" : Controller_page_anastomosis,
            "page_confirmation_anastomosis_to_main" : Controller_page_confirmation_anastomosis_to_main,
            "page_confirmation_anastomosis_to_pump" : Controller_page_confirmation_anastomosis_to_pump,
            "page_confirmation_pump_to_anastomosis" : Controller_page_confirmation_pump_to_anastomosis,
            "page_confirmation_pump_to_training_summary" : Controller_page_confirmation_pump_to_training_summary,
            "page_pump" : Controller_page_pump,
            "page_enter_debit" : Controller_page_enter_debit,
            "page_training_summary" : Controller_page_training_summary
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
