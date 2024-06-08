from .controller_base import Controller_base
from model.component.flow_sensor.flow_sensor import Flow_sensor
from userinterface.page_pump import Page_pump
from userinterface.page_training_summary import Page_training_summary
import model.constant as const
from subprocess import Popen, PIPE, STDOUT
import socket
import threading
import os
from pathlib import Path

import logging

logger = logging.getLogger(__name__)

class Controller_flow_sensor(Controller_base):
    def __init__(self, model, userinterface):
        super().__init__(model,userinterface)
        self.model.flow_sensor.add_event_listener("update_measured_debit_view",self.update_measured_debit_view)
        self.model.flow_sensor.add_event_listener("read_debit",self.process_debit)
        self.model.flow_sensor.add_event_listener("start_subprocess",self.start_subprocess)
        self.model.flow_sensor.add_event_listener("open_connection",self.open_connection)
        self.model.flow_sensor.add_event_listener("retrieve_data",self.retrieve_data)
        self.model.flow_sensor.add_event_listener("terminate_and_close",self.terminate_and_close)

    def update_measured_debit_view(self,flow_sensor: Flow_sensor):
        debit_string = f"{int(flow_sensor.measured_debit):03d}"
        measured_debit_with_unit = "{debit}\n{unit}".format(debit = debit_string,unit = const.DEBIT_UNIT)
        try:
            accuracy_percentage = flow_sensor.measured_debit*100/self.model.pump.setpoint_debit
        except ZeroDivisionError:
            accuracy_percentage = 0
        except:
            logger.error("accuracy percentage can't be calculated due to unexpected error. Check the value")
            raise
        else:
            if accuracy_percentage > 100:
                logger.error("Accuracy exceed 100%, please check the sensor")
            flow_sensor.debit_accuracy = accuracy_percentage
        accuracy_string = f"{int(flow_sensor.debit_accuracy)} %"
        if self.model.user_state.state == "page_pump":
            pump_page: Page_pump = self.userinterface.current_page
            logger.info("update measured debit value & percentage on screen into {debit} and {percentage}".format(
                debit = measured_debit_with_unit,
                percentage = accuracy_string
            ))
            pump_page.itemconfigure(pump_page.text_measured_debit,text=measured_debit_with_unit)
            pump_page.itemconfigure(pump_page.text_debit_accuracy,text=accuracy_string)
        elif self.model.user_state.state == "page_training_summary":
            training_summary_page: Page_training_summary = self.userinterface.current_page
            logger.info("update measured debit value & percentage for summary into {debit} and {percentage}".format(
                debit = measured_debit_with_unit,
                percentage = accuracy_string
            ))
            training_summary_page.itemconfigure(training_summary_page.text_measured_debit,text=measured_debit_with_unit)
            training_summary_page.itemconfigure(training_summary_page.text_debit_accuracy,text=accuracy_string)
        else:
            logger.error("Current page doesn't have to show the debit. Debit update skipped")
    
    def process_debit(self, flow_sensor: Flow_sensor):
        flow_sensor.raw_debit = flow_sensor.raw_debit.replace("Debit = ","")
        flow_sensor.measured_debit = int(flow_sensor.raw_debit)
        # Need adjustment later
        self.update_measured_debit_view(flow_sensor)
    
    def start_subprocess(self, flow_sensor: Flow_sensor):
        cwd = os.getcwd()
        subprocess_path = Path(__file__).parent.parent / "model" / "component" / "flow_sensor"
        os.chdir(subprocess_path)
        create_subprocess   = Popen(const.CREATE_COMMAND)
        create_subprocess.wait()
        logger.info("Subprocess succesfully created")
        flow_sensor.subprocess  = Popen(const.RUN_COMMAND, stdout=PIPE,stderr=PIPE,text=True,universal_newlines=True)
        logger.info("Subprocess succesfully opened")
        os.chdir(cwd)

    def open_connection(self, flow_sensor: Flow_sensor):
        flow_sensor.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        flow_sensor.socket.bind((const.HOST, const.PORT))
        flow_sensor.socket.listen()
        logger.info(f"Server listening on {const.HOST}:{const.PORT}")

    def retrieve_data(self, flow_sensor: Flow_sensor):
        flow_sensor.connection, flow_sensor.address = flow_sensor.socket.accept()
        logger.info(f"Connected by {flow_sensor.address}")
        with flow_sensor.connection:
            while flow_sensor.state == "listening" or flow_sensor.state == "idle":
                data = flow_sensor.connection.recv(1024)
                flow_sensor.raw_debit = data.decode()
                if not data:
                    break
                logger.debug(f"Received from {flow_sensor.address}: {data.decode()}")
                if flow_sensor.state == "listening":
                    self.process_debit(flow_sensor)
        self.terminate_and_close(flow_sensor)            

    def terminate_and_close(self, flow_sensor: Flow_sensor):
        flow_sensor.socket.close()
        flow_sensor.subprocess.terminate()
        logger.info("connection terminated and subprogram closed")
