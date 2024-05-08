from .base import ObservableModel

class User_state(ObservableModel):
    def __init__(self):
        super().__init__()
        self.state = "page_main" 
        self.prev_state = None
    
    # def page_anastomosis(self):
    #     self.prev_state = self.state
    #     self.state = "page_anastomosis"
    #     self.trigger_event("move_to_page_anastomosis")

    # def page_main(self):
    #     self.prev_state = self.state
    #     self.state = "page_main"
    #     self.trigger_event("move_to_page_main")

    def move_to_new_page(self,new_page: str):
        self.prev_state = self.state
        self.state = new_page
        self.trigger_event("move_to_new_page")
    
    def exit(self):
        self.state = "exit"
        self.trigger_event("exit_app")

    def back_to_page_anastomosis_from_confirmation(self):
        if self.prev_state == "page_anastomosis_suturing_force":
            self.move_to_new_page("page_anastomosis_suturing_force")
        elif self.prev_state == "page_anastomosis_camera":
            self.move_to_new_page("page_anastomosis_camera")
        else:
            self.move_to_new_page("page_anastomosis")
