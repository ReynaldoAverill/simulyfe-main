from .base import ObservableModel

class User_state(ObservableModel):
    def __init__(self):
        super().__init__()
        self.state = "page_main" 
        self.prev_state = None
    
    def page_anastomosis(self):
        self.prev_state = self.state
        self.state = "page_anastomosis"
        self.trigger_event = "move_to_page_anastomosis"

    def page_main(self):
        self.prev_state = self.state
        self.state = "page_main"
        self.trigger_event = "move_to_page_main"
    
    def exit(self):
        self.state = "exit"
        self.trigger_event = "exit_app"
