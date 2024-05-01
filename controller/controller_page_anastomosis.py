from userinterface.userinterface import Userinterface
from model.model import Model
import logging

logger = logging.getLogger(__name__)

class Controller_page_anastomosis: 
    def __init__(self,model: Model,userinterface:Userinterface):
        self.model = model
        self.userinterface = userinterface
        self.page = self.userinterface.current_page
        # self.page = self.userinterface.page_classes["page_main"](self.userinterface)
        self._bind_with_userinterface()
    def _bind_with_userinterface(self):
        # pass
        self.page.button_confirmation_to_main.config(command = lambda: self._moveto_page_confirmation())
        # self.page.button_exit.config(command = lambda: self._exit_app())
        # self.page.button_exit.config(command = lambda: self._exit_app())
    # def _moveto_page_anastomosis(self):
    #     logger.debug("button start_pressed, change app state")
    #     self.model.user_state.page_anastomosis()
        # self.page.button_confirmation_to_main.config(command = lambda: self._moveto_page_confirmation())
    def _moveto_page_confirmation(self):
        logger.debug("button main menu pressed")
        self.model.user_state.move_to_new_page("page_main")