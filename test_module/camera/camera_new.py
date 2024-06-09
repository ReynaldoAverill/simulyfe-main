import cv2 as cv
import os
from datetime import datetime
from pathlib import Path
import tkinter as tk
from PIL import Image, ImageTk
import threading

class Model:
    def __init__(self, output_dir):
        self.output_dir = output_dir
        self.cam = cv.VideoCapture(2)
        if not self.cam.isOpened():
            raise Exception("Error: Camera could not be opened.")
        self.recording = False
        self.is_paused = False
        self.previewing = False
        self.file = None
        self.frame = None
        self.lock = threading.Lock()
        # self.create_new_video_writer()

    def create_new_video_writer(self):
        date = datetime.now().strftime("%d-%m-%Y_%H.%M.%S")
        filename = self.output_dir / f"video_{date}.mp4"
        fourcc = cv.VideoWriter_fourcc(*'mp4v')
        self.file = cv.VideoWriter(str(filename), fourcc, 30.0, (640, 480))
        print(f"Recording started... {filename}")

    def start_recording(self):
        if not self.recording:
            self.recording = True
            self.create_new_video_writer()
            if not self.previewing:
                self.previewing = True
            threading.Thread(target=self._capture_frames, daemon=True).start()

    def _capture_frames(self):
        while self.recording or self.previewing:
            ret, frame = self.cam.read()
            if not ret:
                print("Error: Frame could not be retrieved.")
                break
            with self.lock:
                self.frame = frame
            if self.recording and not self.is_paused:
                self.file.write(frame)

    def pause(self):
        self.is_paused = not self.is_paused
        print("Recording paused." if self.is_paused else "Recording resumed.")

    def reset(self):
        if self.recording:
            self.file.release()
            self.recording = False
        print("Reset recording")
            # self.create_new_video_writer()

    def stop(self):
        self.recording = False
        self.previewing = False
        self.cam.release()
        if self.file:
            self.file.release()
        cv.destroyAllWindows()
        print("Recording stopped and resources released.")

class View:
    def __init__(self, root):
        self.root = root
        self.canvas = tk.Canvas(root, width=640, height=480)
        self.canvas.pack()

        self.start_button = tk.Button(root, text="Start")
        self.start_button.pack(side=tk.LEFT)

        self.pause_button = tk.Button(root, text="Pause")
        self.pause_button.pack(side=tk.LEFT)

        self.reset_button = tk.Button(root, text="Reset")
        self.reset_button.pack(side=tk.LEFT)

        self.preview_button = tk.Button(root, text="Preview Camera")
        self.preview_button.pack(side=tk.LEFT)

    # def update_preview(self, frame):
    #     if frame is not None:
    #         frame_rgb = cv.cvtColor(frame, cv.COLOR_BGR2RGB)
    #         img = Image.fromarray(frame_rgb)
    #         imgtk = ImageTk.PhotoImage(image=img)
    #         self.canvas.imgtk = imgtk
    #         self.canvas.create_image(0, 0, anchor=tk.NW, image=imgtk)

class Controller:
    def __init__(self, root, model, view):
        self.root = root
        self.model = model
        self.view = view

        # self.model.start_recording()
        self.update_preview()

        self.root.bind('<Key>', self.on_key)

        self.view.start_button.config(command=self.on_start)
        self.view.pause_button.config(command=self.on_pause)
        self.view.reset_button.config(command=self.on_reset)
        self.view.preview_button.config(command=self.on_preview)

    def on_start(self):
        self.model.start_recording()

    def on_pause(self):
        self.model.pause()

    def on_reset(self):
        self.model.reset()

    def on_preview(self):
        self.model.previewing = not self.model.previewing
        if self.model.previewing:
            self.update_preview()
        else:
            self.view.canvas.delete("all")
            self.view.canvas.create_rectangle(0, 0, 640, 480, fill="gray")

    def on_key(self, event):
        if event.char == 'q':
            self.model.stop()
            self.root.quit()
        elif event.char == 'p':
            self.model.pause()
        elif event.char == 'r':
            self.model.reset()

        self.update_preview()

    def update_preview(self):
        if self.model.previewing:
            frame = self.model.frame
            if frame is not None:
                frame_rgb = cv.cvtColor(frame, cv.COLOR_BGR2RGB)
                img = Image.fromarray(frame_rgb)
                imgtk = ImageTk.PhotoImage(image=img)
                self.view.canvas.imgtk = imgtk
                self.view.canvas.create_image(0, 0, anchor=tk.NW, image=imgtk)
                # self.view.update_preview(frame)
                self.root.after(10, self.update_preview)

def start_app(output_dir):
    root = tk.Tk()
    root.title("Camera Recorder")

    model = Model(output_dir)
    view = View(root)
    controller = Controller(root, model, view)

    root.mainloop()

if __name__ == "__main__":
    output_dir = Path(__file__).parent / "recording"
    try:
        start_app(output_dir)
    except Exception as e:
        print(f"An error occurred: {e}")
