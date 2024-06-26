from .controller_base import Controller_base
from userinterface.page_confirmation_anastomosis_to_pump import Page_confirmation_anastomosis_to_pump
import logging

logger = logging.getLogger(__name__)

class Controller_page_confirmation_anastomosis_to_pump(Controller_base): 
    def __init__(self,model, userinterface):
        super().__init__(model,userinterface)
        self.page: Page_confirmation_anastomosis_to_pump = self.userinterface.current_page
        self._bind_with_userinterface()
        
    def _bind_with_userinterface(self):
        self.page.button_to_anastomosis.config(command = lambda: self._moveto_page_anastomosis())
        self.page.button_to_pump.config(command = lambda: self._moveto_page_pump())
      
    def _moveto_page_anastomosis(self):
        logger.info("button go to previous menu pressed, change app state")
        self.model.user_state.back_to_page_anastomosis_from_confirmation()
        
    def _moveto_page_pump(self):
        logger.info("button go to pump menu pressed, change app state")
        self.model.user_state.move_to_new_page("page_pump")