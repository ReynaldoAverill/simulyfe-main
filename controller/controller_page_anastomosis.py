from .controller_base import Controller_base
from userinterface.page_anastomosis import Page_anastomosis
import logging

logger = logging.getLogger(__name__)

class Controller_page_anastomosis(Controller_base): 
    def __init__(self,model,userinterface):
        super().__init__(model,userinterface)
        self.page: Page_anastomosis = self.userinterface.current_page
        self._bind_with_userinterface()

    def _bind_with_userinterface(self):
        # pass
        self.page.button_confirmation_to_main.config(command = lambda: self._moveto_page_confirmation())
        self.page.button_start_stopwatch.config(command = lambda: self.model.stopwatch.change_stopwatch_state())
        self.page.button_stop_stopwatch.config(command = lambda: self.model.stopwatch.change_stopwatch_state())
        self.page.button_reset_stopwatch.config(command = lambda: self.model.stopwatch.reset_stopwatch())
        
    def _moveto_page_confirmation(self):
        logger.info("button main menu pressed")
        self.model.user_state.move_to_new_page("page_confirmation_anastomosis_to_main")