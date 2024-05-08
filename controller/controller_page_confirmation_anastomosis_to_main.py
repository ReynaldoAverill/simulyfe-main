from .controller_base import Controller_base
from userinterface.page_confirmation_anastomosis_to_main import Page_confirmation_anastomosis_to_main
import logging

logger = logging.getLogger(__name__)

class Controller_page_confirmation_anastomosis_to_main(Controller_base): 
    def __init__(self,model, userinterface):
        super().__init__(model,userinterface)
        self.page: Page_confirmation_anastomosis_to_main = self.userinterface.current_page
        self._bind_with_userinterface()
        
    def _bind_with_userinterface(self):
        # pass
        self.page.button_to_anastomosis.config(command = lambda: self._moveto_page_anastomosis())
        self.page.button_to_main.config(command = lambda: self._moveto_page_main())

    def _moveto_page_anastomosis(self):
        logger.info("button go to previous menu pressed, change app state")
        self.model.user_state.back_to_page_anastomosis_from_confirmation()
        
    def _moveto_page_main(self):
        logger.info("button go to main menu pressed, change app state")
        self.model.user_state.move_to_new_page("page_main")
        self.model.stopwatch.reset_stopwatch()