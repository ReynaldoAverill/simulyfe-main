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
        self.model.force_sensor.add_event_listener("activate_force_sensor_left",self.activate_force_sensor_right)
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

    def activate_force_sensor_right(self, force_sensor: Force_sensor):
        try:
            force_sensor.force_sensor_right = HX711(const.D_OUT_RIGHT,const.PD_SCK_RIGHT)
        except:
            logger.error("Fail to create right force sensor")
        else:
            force_sensor.force_sensor_right.setReadingFormat("MSB","MSB")
            logger.info("Automatically setting the offset.")
            force_sensor.force_sensor_right.autosetOffset()
            offsetValue = force_sensor.force_sensor_right.getOffset()
            logger.info(f"Finished automatically setting the offset. The new value is '{offsetValue}'.")
            logger.info(f"Setting the 'referenceUnit' at {const.REF_UNIT_RIGHT}.")
            force_sensor.force_sensor_right.setReferenceUnit(const.REF_UNIT_RIGHT)
            logger.info(f"Finished setting the 'referenceUnit' at {const.REF_UNIT_RIGHT}.")        

    def retrieve_data_left(self, force_sensor: Force_sensor):
        while force_sensor.update_left:
            rawBytes = force_sensor.force_sensor_left.getRawBytes()
            # longValue = force_sensor.force_sensor_left.rawBytesToLong(rawBytes)
            force_sensor.longWithOffset_left    = force_sensor.force_sensor_left.rawBytesToLongWithOffset(rawBytes)
            force_sensor.weightValue_left       = force_sensor.force_sensor_left.rawBytesToWeight(rawBytes)
            force_sensor.weight_adjusted_left   = force_sensor.weightValue_left - force_sensor.zero_left
            force_sensor.category_left          = self.evaluate_force(force_sensor.weight_adjusted_left)
            #print(f"[INFO] POLLING_BASED | longValue: {longValue} | longWithOffsetValue: {longWithOffsetValue} | weight (grams): {weightValue}")
            logger.debug(f"LEFT | longWithOffsetValue: {force_sensor.longWithOffset_left} | weight adjusted (grams): {force_sensor.weight_adjusted_left:.2f} | {force_sensor.category_left}")
            self.update_measurement_category(force_sensor)

    def retrieve_data_right(self, force_sensor: Force_sensor):
        while force_sensor.update_right:
            rawBytes = force_sensor.force_sensor_right.getRawBytes()
            # longValue = force_sensor.force_sensor_right.rawBytesToLong(rawBytes)
            force_sensor.longWithOffset_right    = force_sensor.force_sensor_right.rawBytesToLongWithOffset(rawBytes)
            force_sensor.weightValue_right       = force_sensor.force_sensor_right.rawBytesToWeight(rawBytes)
            force_sensor.weight_adjusted_right   = force_sensor.weightValue_right - force_sensor.zero_right
            force_sensor.category_right          = self.evaluate_force(force_sensor.weight_adjusted_right)
            #print(f"[INFO] POLLING_BASED | longValue: {longValue} | longWithOffsetValue: {longWithOffsetValue} | weight (grams): {weightValue}")
            logger.debug(f"RIGHT | longWithOffsetValue: {force_sensor.longWithOffset_right} | weight adjusted (grams): {force_sensor.weight_adjusted_right:.2f} | {force_sensor.category_right}")
            self.update_measurement_category(force_sensor)

    def update_measurement_category(self, force_sensor: Force_sensor):
        suturing_force_page: Page_anastomosis_suturing_force = self.userinterface.current_page
        if const.ACTIVE_LEFT:
            # Give enter for no force category 
            if force_sensor.category_left != "NO FORCE":
                suturing_force_page.itemconfigure(suturing_force_page.text_suturing_force_left,text=force_sensor.category_left)
            else:
                suturing_force_page.itemconfigure(suturing_force_page.text_suturing_force_left,text="NO\nFORCE")
            # Update box color
            if force_sensor.category_left == "STRONG":
                force_sensor.strong_count_left+=1
                suturing_force_page.itemconfigure(suturing_force_page.box_suturing_force_left,fill="#FF0000")
            elif force_sensor.category_left == "MEDIUM":
                force_sensor.medium_count_left+=1
                suturing_force_page.itemconfigure(suturing_force_page.box_suturing_force_left,fill="#FFF500")
            elif force_sensor.category_left == "SAFE":
                force_sensor.safe_count_left+=1
                suturing_force_page.itemconfigure(suturing_force_page.box_suturing_force_left,fill="#00FF00")
            else:
                force_sensor.noforce_count_left+=1
                suturing_force_page.itemconfigure(suturing_force_page.box_suturing_force_left,fill="#F2F2F2")
        if const.ACTIVE_RIGHT:
            # Give enter for no force category 
            if force_sensor.category_right != "NO FORCE":
                suturing_force_page.itemconfigure(suturing_force_page.text_suturing_force_right,text=force_sensor.category_right)
            else:
                suturing_force_page.itemconfigure(suturing_force_page.text_suturing_force_right,text="NO\nFORCE")
            # Update box color
            suturing_force_page.itemconfigure(suturing_force_page.text_suturing_force_right,text=force_sensor.category_right)
            if force_sensor.category_right == "STRONG":
                force_sensor.strong_count_right+=1
                suturing_force_page.itemconfigure(suturing_force_page.box_suturing_force_right,fill="#FF0000")
            elif force_sensor.category_right == "MEDIUM":
                force_sensor.medium_count_right+=1
                suturing_force_page.itemconfigure(suturing_force_page.box_suturing_force_right,fill="#FFF500")
            elif force_sensor.category_right == "SAFE":
                force_sensor.safe_count_right+=1
                suturing_force_page.itemconfigure(suturing_force_page.box_suturing_force_right,fill="#00FF00")
            else:
                force_sensor.noforce_count_right+=1
                suturing_force_page.itemconfigure(suturing_force_page.box_suturing_force_right,fill="#F2F2F2")
        
    def evaluate_force(self, weightValue: float) -> str:
        if weightValue >= const.STRONG_START:
            return "STRONG"
        elif weightValue >= const.MEDIUM_START:
            return "MEDIUM"
        elif weightValue >= const.SAFE_START:
            return "SAFE"
        else:
            return "NO FORCE"