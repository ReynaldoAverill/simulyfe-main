from .controller_base import Controller_base
from model.component.pump.pump import Pump
from userinterface.page_enter_debit import Page_enter_debit
import model.constant as const
import logging

logger = logging.getLogger(__name__)

class Controller_pump(Controller_base):
    def __init__(self, model, userinterface):
        super().__init__(model,userinterface)
        self.model.pump.add_event_listener("get_pump_setpoint_debit",self.get_pump_setpoint_debit)
        self.model.pump.add_event_listener("delete_digit_setpoint_debit",self.delete_digit_setpoint_debit)
        self.model.pump.add_event_listener("change_pump_state",self.change_pump_state)
        self.model.pump.add_event_listener("finalize_pump_setpoint_debit",self.finalize_pump_setpoint_debit)

    def get_pump_setpoint_debit(self, pump: Pump):
        pump.total_debit_digit += 1
        if pump.total_debit_digit > const.MAX_DIGIT_DEBIT:
            pump.total_debit_digit = const.MAX_DIGIT_DEBIT
        pump.setpoint_debit = (pump.setpoint_debit % (10**(const.MAX_DIGIT_DEBIT-1))) * 10 +  pump.current_digit
        self.update_setpoint_debit_view(pump.setpoint_debit)
        
    def delete_digit_setpoint_debit(self, pump: Pump):
        if pump.total_debit_digit > 0:
            pump.total_debit_digit -= 1
        else:
            pump.total_debit_digit = 0
        pump.setpoint_debit = pump.setpoint_debit // 10
        self.update_setpoint_debit_view(pump.setpoint_debit)
    
    def update_setpoint_debit_view(self,debit_value):
        debit_string = f"{int(debit_value):03d}"
        enter_debit_page: Page_enter_debit = self.userinterface.current_page
        # Validate button existence
        try:
            logger.info("update input value on screen")
            enter_debit_page.itemconfigure(enter_debit_page.text_debit_value,text=debit_string)
        except:
            logger.error("Not in the page change debit. Debit update skipped")

    def change_pump_state(self, pump: Pump):
        pass

    def finalize_pump_setpoint_debit(self, pump: Pump):
        pass



