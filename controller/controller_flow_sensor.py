from .controller_base import Controller_base
from model.component.flow_sensor.flow_sensor import Flow_sensor
from userinterface.page_enter_debit import Page_enter_debit
from userinterface.page_pump import Page_pump
import model.constant as const
import logging

logger = logging.getLogger(__name__)

class Controller_flow_sensor(Controller_base):
    def __init__(self, model, userinterface):
        super().__init__(model,userinterface)
        self.model.flow_sensor.add_event_listener("update_measured_debit_view",self.update_measured_debit_view)
        self.model.flow_sensor.add_event_listener("read_debit",self.read_debit)

    def update_measured_debit_view(self,flow_sensor: Flow_sensor):
        self.read_debit(flow_sensor)
        debit_string = f"{int(flow_sensor.measured_debit):03d}"
        try:
            accuracy_percentage = flow_sensor.measured_debit*100/self.model.pump.setpoint_debit
        except ZeroDivisionError:
            accuracy_percentage = 0
        else:
            logger.error("accuracy percentage can't be calculated. Check the value")
        finally:
            flow_sensor.debit_accuracy = accuracy_percentage
        accuracy_string = f"{int(flow_sensor.debit_accuracy)} %"
        if self.model.user_state.state == "page_pump":
            pump_page: Page_pump = self.userinterface.current_page
            measured_debit_with_unit = "{debit}\n{unit}".format(debit = debit_string,unit = const.DEBIT_UNIT)
            logger.info("update measured debit value & percentage on screen into {debit} and {percentage}".format(
                debit = measured_debit_with_unit,
                percentage = accuracy_string
            ))
            pump_page.itemconfigure(pump_page.text_measured_debit,text=measured_debit_with_unit)
            pump_page.itemconfigure(pump_page.text_debit_accuracy,text=accuracy_string)
        else:
            logger.error("Current page doesn't have to show the debit. Debit update skipped")
    
    def read_debit(self,flow_sensor: Flow_sensor):
        # Need adjustment later
        flow_sensor.measured_debit = 50
