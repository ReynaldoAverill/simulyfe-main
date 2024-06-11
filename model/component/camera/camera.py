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
        self.cam = cv.VideoCapture(const.CAM_PORT)
        self.connected = self.cam.isOpened()
        if not self.connected:
            logger.error("Error: Camera could not be opened.")
        else:
            logger.info("camera successfully activated")

    def start_recording(self):
        if not self.recording:
            self.recording = True
            self.trigger_event("create_new_video_writer")
            if not self.previewing:
                self.previewing = True
            threading.Thread(target=lambda: self.trigger_event("capture_frames"), daemon=True).start()
            self.trigger_event("change_layout")
        else:
            logger.error("recording not started")

    def pause(self):
        self.is_paused = not self.is_paused
        logger.info("Recording paused." if self.is_paused else "Recording resumed.")
        self.trigger_event("change_layout")

    def reset(self):
        if self.recording:
            self.trigger_event("reset_recording")
            self.recording = False
        self.trigger_event("change_layout")

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
