from .controller_base import Controller_base
from datetime import datetime
from model.component.camera.camera import Camera
from userinterface.page_anastomosis_camera import Page_anastomosis_camera
from PIL import Image, ImageTk
import cv2 as cv
import tkinter as tk
import model.constant as const
import logging

logger = logging.getLogger(__name__)

class Controller_camera(Controller_base):
    def __init__(self, model, userinterface):
        super().__init__(model,userinterface)
        # self.model.camera.start_recording()
        self.model.camera.add_event_listener("create_new_video_writer",self.create_new_video_writer)
        # self.model.camera.add_event_listener("on_start",self.on_start
        self.model.camera.add_event_listener("reset_recording",self.reset_recording)
        self.model.camera.add_event_listener("capture_frames",self.capture_frames)
        self.model.camera.add_event_listener("change_layout",self.change_layout)
    
    def create_new_video_writer(self, camera: Camera):
        date = datetime.now().strftime("%d-%m-%Y_%H.%M.%S")
        filename = camera.output_dir / f"video_{date}.mp4"
        fourcc = cv.VideoWriter_fourcc(*'mp4v')
        camera.file = cv.VideoWriter(str(filename), fourcc, const.FPS, (const.FRAME_WIDTH, const.FRAME_HEIGHT))
        logger.info(f"Recording started... {filename}")
    
    def capture_frames(self,camera : Camera):
        while camera.recording or camera.previewing:
            ret, frame = camera.cam.read()
            if not ret:
                logger.error("Error: Frame could not be retrieved.")
                break
            with camera.lock:
                camera.frame = frame
            if camera.recording and not camera.is_paused:
                camera.file.write(frame)

    # def on_start(self, camera: Camera):
    #     self.create_new_video_writer()
    #     camera.start_recording()

    # def on_pause(self):
    #     self.model.camera.pause()

    def reset_recording(self, camera: Camera):
        if camera.file:
            camera.file.release()
            logger.info("Recording reset")
        else:
            logger.error("No camera file exist")
        self.change_layout
        # self.create_new_video_writer()

    def stop_camera(self, camera: Camera):
        camera.cam.release()
        if camera.file:
            camera.file.release()
        cv.destroyAllWindows()
        logger.info("Recording stopped and resources released.")

    def change_layout(self, camera: Camera):
        camera_page: Page_anastomosis_camera = self.userinterface.current_page
        if camera.connected:
            camera_page.itemconfigure(camera_page.text_camera_connectionstatus,text="CONNECTED",fill="#00FF00")
        else:
            camera_page.itemconfigure(camera_page.text_camera_connectionstatus,text="DISCONNECTED",fill="#FF0000")
        if camera.recording and not camera.is_paused:
            camera_page.itemconfigure(camera_page.text_camera_recordingstatus,text="RECORDING",fill="#00FF00")
        elif camera.recording and camera.is_paused:
            camera_page.itemconfigure(camera_page.text_camera_recordingstatus,text="PAUSED",fill="#FFF500")
        else:
            camera_page.itemconfigure(camera_page.text_camera_recordingstatus,text="NOT RECORDING",fill="#FF0000")

    def on_preview(self):
        self.model.camera.previewing = not self.model.camera.previewing
        if self.model.camera.previewing:
            pass
            # self.update_preview()
        else:
            pass
            # self.view.canvas.delete("all")
            # self.view.canvas.create_rectangle(0, 0, 640, 480, fill="gray")

    def update_preview(self):
        pass
        # if self.model.camera.previewing:
        #     frame = self.model.camera.frame
        #     if frame is not None:
        #         frame_rgb = cv.cvtColor(frame, cv.COLOR_BGR2RGB)
        #         img = Image.fromarray(frame_rgb)
        #         imgtk = ImageTk.PhotoImage(image=img)
        #         self.userinterface.current_page.imgtk = imgtk
        #         self.view.canvas.create_image(0, 0, anchor=tk.NW, image=imgtk)
        #         # self.view.update_preview(frame)
        #         self.root.after(10, self.update_preview)
    

