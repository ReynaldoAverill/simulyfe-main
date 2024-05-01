from userinterface.userinterface import Userinterface
from model.model import Model
import logging

logger = logging.getLogger(__name__)

class Controller_page_confirmation_anastomosis_to_main: 
    def __init__(self,model: Model, userinterface:Userinterface):
        self.model = model
        self.userinterface = userinterface
        self.page = self.userinterface.current_page

        self._bind_with_userinterface()
        # print(self.page.x)
    def _bind_with_userinterface(self):
        # pass
        self.page.button_to_anastomosis.config(command = lambda: self._moveto_page_anastomosis())
        self.page.button_to_main.config(command = lambda: self._moveto_page_main())
        # self.page.button_exit.config(command = lambda: self._exit_app())
    def _moveto_page_anastomosis(self):
        logger.debug("button go to previous menu pressed, change app state")
        self.model.user_state.move_to_new_page("page_anastomosis")
    def _moveto_page_main(self):
        logger.debug("button go to main menu pressed, change app state")
        self.model.user_state.move_to_new_page("page_main")