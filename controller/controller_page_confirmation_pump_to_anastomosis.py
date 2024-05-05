from .controller_base import Controller_base
from userinterface.page_confirmation_pump_to_anastomosis import Page_confirmation_pump_to_anastomosis
import logging

logger = logging.getLogger(__name__)

class Controller_page_confirmation_pump_to_anastomosis(Controller_base): 
    def __init__(self,model, userinterface):
        super().__init__(model,userinterface)
        self.page: Page_confirmation_pump_to_anastomosis = self.userinterface.current_page
        self._bind_with_userinterface()
        
    def _bind_with_userinterface(self):
        self.page.button_to_anastomosis.config(command = lambda: self._moveto_page_anastomosis())
        self.page.button_to_pump.config(command = lambda: self._moveto_page_pump())
      
    def _moveto_page_anastomosis(self):
        logger.info("button go to previous menu pressed, change app state")
        self.model.user_state.move_to_new_page("page_anastomosis")
        
    def _moveto_page_pump(self):
        logger.info("button go to pump menu pressed, change app state")
        self.model.user_state.move_to_new_page("page_pump")