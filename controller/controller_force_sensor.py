from .controller_base import Controller_base
from model.component.force_sensor.force_sensor import Force_sensor
from model.component.force_sensor.hx711 import HX711
from userinterface.page_anastomosis_suturing_force import Page_anastomosis_suturing_force
import model.constant as const
import threading
import os
from pathlib import Path

import logging

logger = logging.getLogger(__name__)

class Controller_force_sensor(Controller_base):
    def __init__(self, model, userinterface):
        super().__init__(model,userinterface)
        self.model.force_sensor.add_event_listener("activate_force_sensor_left",self.activate_force_sensor_left)
        self.model.force_sensor.add_event_listener("retrieve_data_left",self.retrieve_data_left)
        self.model.force_sensor.add_event_listener("retrieve_data_right",self.retrieve_data_right)
    
    def activate_force_sensor_left(self, force_sensor: Force_sensor):
        try:
            force_sensor.force_sensor_left = HX711(const.D_OUT_LEFT,const.PD_SCK_LEFT)
        except:
            logger.error("Fail to create left force sensor")
        else:
            force_sensor.force_sensor_left.setReadingFormat("MSB","MSB")
            logger.info("Automatically setting the offset.")
            force_sensor.force_sensor_left.autosetOffset()
            offsetValue = force_sensor.force_sensor_left.getOffset()
            logger.info(f"Finished automatically setting the offset. The new value is '{offsetValue}'.")
            logger.info(f"Setting the 'referenceUnit' at {const.REF_UNIT_LEFT}.")
            force_sensor.force_sensor_left.setReferenceUnit(const.REF_UNIT_LEFT)
            logger.info(f"Finished setting the 'referenceUnit' at {const.REF_UNIT_LEFT}.")

    def retrieve_data_left(self, force_sensor: Force_sensor):
        while force_sensor.update_left:
            rawBytes = force_sensor.force_sensor_left.getRawBytes()
            # longValue = force_sensor.force_sensor_left.rawBytesToLong(rawBytes)
            force_sensor.longWithOffset_left    = force_sensor.force_sensor_left.rawBytesToLongWithOffset(rawBytes)
            force_sensor.weightValue_left       = force_sensor.force_sensor_left.rawBytesToWeight(rawBytes)
            force_sensor.category_left          = self.evaluate_force(force_sensor.weightValue_left)
            #print(f"[INFO] POLLING_BASED | longValue: {longValue} | longWithOffsetValue: {longWithOffsetValue} | weight (grams): {weightValue}")
            logger.debug(f"LEFT | longWithOffsetValue: {force_sensor.longWithOffset_left} | weight (grams): {force_sensor.weightValue_left} | {force_sensor.category_left}")
            self.update_measurement_category(force_sensor)

    def retrieve_data_right(self, force_sensor: Force_sensor):
        pass

    def update_measurement_category(self, force_sensor: Force_sensor):
        suturing_force_page: Page_anastomosis_suturing_force = self.userinterface.current_page
        suturing_force_page.itemconfigure(suturing_force_page.text_suturing_force_left,text=force_sensor.category_left)
        if force_sensor.category_left == "STRONG":
            suturing_force_page.itemconfigure(suturing_force_page.box_suturing_force_left,fill="#FF0000")
        elif force_sensor.category_left == "MEDIUM":
            suturing_force_page.itemconfigure(suturing_force_page.box_suturing_force_left,fill="#FFF500")
        else:
            suturing_force_page.itemconfigure(suturing_force_page.box_suturing_force_left,fill="#00FF00")
        
    def evaluate_force(self, weightValue: float) -> str:
        if weightValue >= const.STRONG_START:
            return "STRONG"
        elif weightValue >= const.MEDIUM_START:
            return "MEDIUM"
        else:
            return "WEAK"
        