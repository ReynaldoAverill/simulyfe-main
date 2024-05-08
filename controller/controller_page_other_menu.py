from .controller_base import Controller_base
from userinterface.page_other_menu import Page_other_menu
import logging

logger = logging.getLogger(__name__)

class Controller_page_other_menu(Controller_base): 
    def __init__(self,model,userinterface):
        super().__init__(model,userinterface)
        self.page: Page_other_menu = self.userinterface.current_page
        self._bind_with_userinterface()

    def _bind_with_userinterface(self):
        self.page.button_to_main.config(command = lambda: self._moveto_page_main())
        self.page.button_to_history.config(command= lambda: self._moveto_page_action_history())

    def _moveto_page_main(self):
        logger.info("button back pressed, change app state")
        self.model.user_state.move_to_new_page("page_main")

    def _moveto_page_action_history(self):
        logger.info("button history pressed, change app state")
        self.model.user_state.move_to_new_page("page_action_history")
