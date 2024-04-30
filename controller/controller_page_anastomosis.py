from userinterface.userinterface import Userinterface
from model.model import Model
import logging

logger = logging.getLogger(__name__)

class Controller_page_anastomosis: 
    def __init__(self,model: Model,userinterface:Userinterface):
        self.model = model
        self.userinterface = userinterface
        self.page = self.userinterface.page_classes["page_anastomosis"]
        # self.page = self.userinterface.page_classes["page_main"](self.userinterface)
        self._bind_with_userinterface()
    def _bind_with_userinterface(self):
        pass
        # self.page.button_confirmation_to_main.config(command = lambda: self._moveto_page_confirmation())
    def _moveto_page_confirmation(self):
        logger.debug("button main menu pressed")
        self.model.user_state.page_main()