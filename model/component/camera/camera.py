import threading
import model.constant as const
from model.base import ObservableModel
import cv2 as cv
import os
from datetime import datetime
from pathlib import Path
import tkinter as tk
from PIL import Image, ImageTk
import threading

import logging
logger = logging.getLogger(__name__)

class Camera(ObservableModel):
    def __init__(self):
        super().__init__()
        self.output_dir = Path(__file__).parent / "recording"
        self.cam = cv.VideoCapture(2)
        if not self.cam.isOpened():
            raise Exception("Error: Camera could not be opened.")
        self.recording = False
        self.is_paused = False
        self.previewing = False
        self.file = None
        self.frame = None
        self.lock = threading.Lock()
        self.create_new_video_writer()

    def create_new_video_writer(self):
        date = datetime.now().strftime("%d-%m-%Y_%H.%M.%S")
        filename = self.output_dir / f"video_{date}.mp4"
        fourcc = cv.VideoWriter_fourcc(*'mp4v')
        self.file = cv.VideoWriter(str(filename), fourcc, 30.0, (640, 480))
        logger.info(f"Recording started... {filename}")
    
    def start_recording(self):
        if not self.recording:
            self.recording = True
            if not self.previewing:
                self.previewing = True
            threading.Thread(target=self._capture_frames, daemon=True).start()

    def _capture_frames(self):
        while self.recording or self.previewing:
            ret, frame = self.cam.read()
            if not ret:
                logger.error("Error: Frame could not be retrieved.")
                break
            with self.lock:
                self.frame = frame
            if self.recording and not self.is_paused:
                self.file.write(frame)

    def pause(self):
        self.is_paused = not self.is_paused
        logger.info("Recording paused." if self.is_paused else "Recording resumed.")

    def reset(self):
        if self.recording:
            self.file.release()
            self.create_new_video_writer()

    def stop(self):
        self.recording = False
        self.previewing = False
        self.cam.release()
        if self.file:
            self.file.release()
        cv.destroyAllWindows()
        logger.info("Recording stopped and resources released.")
