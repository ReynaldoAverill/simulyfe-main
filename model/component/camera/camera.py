import threading
import model.constant as const
from model.base import ObservableModel
import cv2 as cv
import os
from datetime import datetime
from pathlib import Path
import tkinter as tk
# from PIL import Image, ImageTk
import threading

import logging
logger = logging.getLogger(__name__)

class Camera(ObservableModel):
    def __init__(self):
        super().__init__()
        self.output_dir = self.get_output_dir()
        self.cam: cv.VideoCapture = None
        self.connected = False
        self.recording = False
        self.is_paused = False
        self.previewing = False
        self.file: cv.VideoWriter   = None
        self.frame = None
        self.lock = threading.Lock()
        self.activate()
        # self.create_new_video_writer()

    def activate(self):
        if not self.connected:
            self.cam = cv.VideoCapture(const.CAM_PORT)
            self.connected = self.cam.isOpened()
            if not self.connected:
                logger.error("Error: Camera could not be opened.")
            else:
                logger.info("camera successfully activated")
        else:
            logger.info("camera is already connected")

    def start_recording(self):
        if self.connected:
            if not self.recording:
                self.recording = True
                self.trigger_event("create_new_video_writer")
                if not self.previewing:
                    self.previewing = True
                threading.Thread(target=lambda: self.trigger_event("capture_frames"), daemon=True).start()
                self.trigger_event("update_connection_status")
            else:
                logger.error("recording is already started")
        else: 
            logger.error("recording not started because camera is not connected")

    def pause(self):
        if self.connected:
            self.is_paused = not self.is_paused
            logger.info("Recording paused." if self.is_paused else "Recording resumed.")
            self.trigger_event("update_connection_status")
        else:
            logger.error("recording not paused because camera is not connected")

    def reset(self):
        if self.connected:
            if self.recording:
                self.trigger_event("reset_recording")
                self.recording = False
                self.is_paused = False
            self.trigger_event("update_connection_status")
        else:
            logger.error("recording not reset because camera is not connected")

    def stop(self):
        self.recording = False
        self.previewing = False
        self.cam.release()
        if self.file:
            self.file.release()
        cv.destroyAllWindows()
        logger.info("Recording stopped and resources released.")
    
    def get_output_dir(self):
        if const.EXTERNAL:
            return Path(const.EXTERNAL_PATH)
        else:
            return Path(__file__).parent / "recording"
