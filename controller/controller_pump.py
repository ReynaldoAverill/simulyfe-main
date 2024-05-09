from .controller_base import Controller_base
from model.component.pump.pump import Pump
from userinterface.page_enter_debit import Page_enter_debit
from userinterface.page_pump import Page_pump
import model.constant as const
import logging

logger = logging.getLogger(__name__)

class Controller_pump(Controller_base):
    def __init__(self, model, userinterface):
        super().__init__(model,userinterface)
        self.model.pump.add_event_listener("get_pump_setpoint_debit",self.get_pump_setpoint_debit)
        self.model.pump.add_event_listener("delete_digit_setpoint_debit",self.delete_digit_setpoint_debit)
        self.model.pump.add_event_listener("turn_off_pump",self.turn_off_pump)
        self.model.pump.add_event_listener("turn_on_pump",self.turn_on_pump)
        self.model.pump.add_event_listener("change_button_layout",self.change_button_layout)
        self.model.pump.add_event_listener("update_setpoint_debit_view",self.update_setpoint_debit_view)

    def get_pump_setpoint_debit(self, pump: Pump):
        pump.total_debit_digit += 1
        if pump.total_debit_digit > const.MAX_DIGIT_DEBIT:
            pump.total_debit_digit = const.MAX_DIGIT_DEBIT
        pump.setpoint_debit = (pump.setpoint_debit % (10**(const.MAX_DIGIT_DEBIT-1))) * 10 +  pump.current_digit
        self.update_setpoint_debit_view(pump)
        
    def delete_digit_setpoint_debit(self, pump: Pump):
        if pump.total_debit_digit > 0:
            pump.total_debit_digit -= 1
        else:
            pump.total_debit_digit = 0
        pump.setpoint_debit = pump.setpoint_debit // 10
        self.update_setpoint_debit_view(pump)
    
    def update_setpoint_debit_view(self,pump: Pump):
        debit_string = f"{int(pump.setpoint_debit):03d}"
        # Validate page
        if self.model.user_state.state == "page_enter_debit":
            enter_debit_page: Page_enter_debit = self.userinterface.current_page
            logger.info("update input value on screen")
            enter_debit_page.itemconfigure(enter_debit_page.text_debit_value,text=debit_string)
        elif self.model.user_state.state == "page_pump":
            pump_page: Page_pump = self.userinterface.current_page
            debit_string_with_unit = "{debit}\n{unit}".format(debit = debit_string,unit = const.DEBIT_UNIT)
            logger.info("update setpoint debit value on screen into {debit}".format(debit=pump.setpoint_debit))
            pump_page.itemconfigure(pump_page.text_setpoint_debit,text=debit_string_with_unit)
        else:
            logger.error("Current page doesn't have to show the debit. Debit update skipped")

    def turn_off_pump(self, pump: Pump):
        self.change_button_layout(pump)
        if const.RASPBERRYPI:
            import RPi.GPIO as GPIO
            GPIO.output(const.PIN_PUMP_ENABLE_A, GPIO.LOW)
            GPIO.output(const.PIN_PUMP_ENABLE_B, GPIO.LOW)
            pump.pwm.ChangeDutyCycle(0)
    
    def turn_on_pump(self, pump: Pump):
        self.change_button_layout(pump)
        logger.info("Pump is activated with debit {debit} {unit}".format(debit=pump.setpoint_debit,unit=const.DEBIT_UNIT))
        if const.RASPBERRYPI:
            import RPi.GPIO as GPIO
            if const.DIR_A_TO_B:
                GPIO.output(const.PIN_PUMP_ENABLE_A,GPIO.HIGH)
                GPIO.output(const.PIN_PUMP_ENABLE_B,GPIO.LOW)
            else:
                GPIO.output(const.PIN_PUMP_ENABLE_B,GPIO.HIGH)
                GPIO.output(const.PIN_PUMP_ENABLE_A,GPIO.LOW)
            pump.converter_setpoint_debit_to_pmw(pump.setpoint_debit)
            pump.pwm.ChangeDutyCycle(pump.duty_cycle)

    def change_button_layout(self, pump: Pump):
        pump_page: Page_pump = self.userinterface.current_page
        if pump.state:
            pump_page.pump_turned_on_view()
            pump_page.itemconfigure(pump_page.text_pump,text="ON",fill="#00FF00")
        else:
            pump_page.pump_turned_off_view()
            pump_page.itemconfigure(pump_page.text_pump,text="OFF",fill="#FF0000")




