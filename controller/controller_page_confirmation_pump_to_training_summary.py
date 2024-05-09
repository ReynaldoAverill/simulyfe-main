from .controller_base import Controller_base
from userinterface.page_confirmation_pump_to_training_summary import Page_confirmation_pump_to_training_summary
import logging

logger = logging.getLogger(__name__)

class Controller_page_confirmation_pump_to_training_summary(Controller_base): 
    def __init__(self,model, userinterface):
        super().__init__(model,userinterface)
        self.page: Page_confirmation_pump_to_training_summary = self.userinterface.current_page
        self._bind_with_userinterface()
        
    def _bind_with_userinterface(self):
        self.page.button_to_training_summary.config(command = lambda: self._moveto_page_training_summary())
        self.page.button_to_pump.config(command = lambda: self._moveto_page_pump())
      
    def _moveto_page_training_summary(self):
        logger.info("button go to traning_summary pressed, change app state")
        self.model.user_state.move_to_new_page("page_training_summary")
        
    def _moveto_page_pump(self):
        logger.info("button go to pump menu pressed, change app state")
        self.model.user_state.move_to_new_page("page_pump")