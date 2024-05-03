from .controller_page_main import Controller_page_main
from .controller_page_anastomosis import Controller_page_anastomosis
from .controller_page_confirmation_anastomosis_to_main import Controller_page_confirmation_anastomosis_to_main
from userinterface.userinterface import Userinterface
from model.model import Model
from model.user_state import User_state
from model.stopwatch import Stopwatch
import time

import logging

logger = logging.getLogger(__name__)

def format_time_string(time_passed):
    seconds = time_passed % 60
    minutes = time_passed // 60
    hours   = minutes // 60
    return f"{int(hours):02d}:{int(minutes):02d}:{int(seconds):02d}:{int(time_passed%1*100):02d}"

class Controller_userinterface:
    def __init__(self, model:Model, userinterface: Userinterface):
        self.model = model
        self.userinterface = userinterface
        self.pagecontroller_classes = {
            "page_main" : Controller_page_main,
            "page_anastomosis" : Controller_page_anastomosis,
            "page_confirmation_anastomosis_to_main" : Controller_page_confirmation_anastomosis_to_main
            # "page_confirmation_anastomosis_to_main" : Controller_page_confirmation_anastomosis_to_main
        }
        self.current_pagecontroller = None
        self.add_controller_userinterface_event_listener()
    
    def add_controller_userinterface_event_listener(self):
        self.model.user_state.add_event_listener("move_to_new_page",self.movepage_and_constructcontroller)
        self.model.user_state.add_event_listener("exit_app",self.exit_app)
        self.model.stopwatch.add_event_listener("count_stopwatch",self.count_stopwatch)

    def start_app(self):
        if self.model.user_state.state == "page_main":
            self.userinterface.switch_to("page_main")
            self.controller_page_main = Controller_page_main(self.model,self.userinterface)
        self.userinterface.start_mainloop()

    def count_stopwatch(self,stopwatch: Stopwatch):
        logger.debug("Start Stopwatch Count")
        # self.trigger_event("count_stopwatch")
        start = time.time()
        if stopwatch.started: # Case stopwatch already started
            until_now = stopwatch.passed
        else: # Case stopwatch not started yet
            until_now = 0
            stopwatch.started = True
        while stopwatch.running:
            stopwatch_text = self.userinterface.current_page.text_stopwatch
            stopwatch.passed = time.time() - start + until_now
            self.userinterface.current_page.itemconfigure(stopwatch_text,text=format_time_string(stopwatch.passed))

    def movepage_and_constructcontroller(self,user_state: User_state):
        logger.info("Processing to Move to "+str(user_state.state))
        self.userinterface.switch_to(str(user_state.state))
        new_controller = self.pagecontroller_classes[user_state.state](self.model,self.userinterface)
        self.current_pagecontroller = new_controller
    
    def exit_app(self,user_state: User_state):
        logger.info("Processing to close the app")
        self.userinterface.exit_app()
