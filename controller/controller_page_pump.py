from .controller_base import Controller_base
from userinterface.page_pump import Page_pump
import logging

logger = logging.getLogger(__name__)

class Controller_page_pump(Controller_base): 
    def __init__(self,model,userinterface):
        super().__init__(model,userinterface)
        self.page: Page_pump = self.userinterface.current_page
        self._bind_with_userinterface()
        self._activate_flow_sensor()
        self._update_view()

    def _bind_with_userinterface(self):
        self.page.button_back_to_anastomosis.config(command = lambda: self._moveto_page_anastomosis_confirmation())
        self.page.button_change_debit.config(command = lambda: self._moveto_page_enter_debit())
        self.page.button_change_pump_state.config(command = lambda: self._change_pump_state())
        self.page.button_finalize.config(command = lambda: self._moveto_page_training_summary_confirmation())

    def _moveto_page_anastomosis_confirmation(self):
        logger.info("button back to anastomosis pressed")
        self.model.user_state.move_to_new_page("page_confirmation_pump_to_anastomosis")

    def _moveto_page_enter_debit(self):
        logger.info("button go to enter debit pressed")
        self.model.user_state.move_to_new_page("page_enter_debit")

    def _moveto_page_training_summary_confirmation(self):
        logger.info("button go to training summary pressed")
        self.model.user_state.move_to_new_page("page_confirmation_pump_to_training_summary")
    
    def _change_pump_state(self):
        logger.info("button pump pressed, change pump state")
        # Update data from flow sensor
        self.model.pump.change_pump_state()
        self.model.flow_sensor.change_listening_state()
    
    def _activate_flow_sensor(self):
        # Activate flow sensor
        logger.info("Activate flow sensor")
        self.model.flow_sensor.activate()        

    def _update_view(self):
        logger.info("renew all data in the page")
        # Readjust and update setpoint debit view
        self.model.pump.trigger_event("readjust_setpoint_debit")
        # self.model.pump.trigger_event("update_setpoint_debit_view")
        # Update measured debit view
        self.model.flow_sensor.trigger_event("update_measured_debit_view")
        