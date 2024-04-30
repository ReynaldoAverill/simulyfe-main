from userinterface.userinterface import Userinterface
from model.model import Model
import logging
from pprint import pprint
import inspect

logger = logging.getLogger(__name__)

class Controller_page_main: 
    def __init__(self,model: Model, userinterface:Userinterface):
        self.model = model
        self.userinterface = userinterface
        self.page = self.userinterface.current_page
        # self.page = self.userinterface.page_classes["page_main"](self.userinterface)
        self._bind_with_userinterface()
        # print(self.page.x)
    def _bind_with_userinterface(self):
        # pass
        self.page.button_start.config(command = lambda: self._moveto_page_anastomosis())
        self.page.button_exit.config(command = lambda: self._exit_app())
        # self.page.button_exit.config(command = lambda: self._exit_app())
    def _moveto_page_anastomosis(self):
        logger.debug("button start_pressed, change app state")
        self.model.user_state.page_anastomosis()
    def _exit_app(self):
        logger.debug("button exit pressed, change app state")
        self.model.user_state.exit()
