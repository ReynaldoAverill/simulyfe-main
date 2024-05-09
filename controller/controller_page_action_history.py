from .controller_base import Controller_base
from userinterface.page_action_history import Page_action_history
import logging

logger = logging.getLogger(__name__)

class Controller_page_action_history(Controller_base): 
    def __init__(self,model,userinterface):
        super().__init__(model,userinterface)
        self.page: Page_action_history = self.userinterface.current_page
        self._bind_with_userinterface()

    def _bind_with_userinterface(self):
        self.page.button_to_other_menu.config(command = lambda: self._moveto_page_other_menu())

    def _moveto_page_other_menu(self):
        logger.info("button back pressed, change app state")
        self.model.user_state.move_to_new_page("page_other_menu")
