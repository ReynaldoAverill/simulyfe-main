import tkinter as tk
import threading
import time

def start_stopwatch_test():
    root = tk.Tk() 
    app = Application(window=root)
    app.mainloop()

class Application(tk.Canvas):

    def __init__(self, window=None):
        super().__init__(window)
        self.window = window
        self.update_time = ''
        self.running = False
        
        self.passed = 0
        self.started = False

        self.hours = 0
        self.minutes = 0
        self.seconds = 0
        self.miliseconds = 0
        self.pack()
        self.create_widgets()

    def create_widgets(self):
        self.stopwatch_label = tk.Text(self, text='00:00:00:00', font=('Arial', 80))
        self.stopwatch_label.pack()
        self.start_button = tk.Button(self, text='start', height=5, width=7, font=('Arial', 20), command=self.start)
        self.start_button.pack(side=tk.LEFT)
        self.pause_button = tk.Button(self, text='pause', height=5, width=7, font=('Arial', 20), command=self.pause)
        self.pause_button.pack(side=tk.LEFT)
        self.reset_button = tk.Button(self, text='reset', height=5, width=7, font=('Arial', 20), command=self.reset)
        self.reset_button.pack(side=tk.LEFT)
        self.quit_button = tk.Button(self, text='quit', height=5, width=7, font=('Arial', 20), command=self.window.quit)
        self.quit_button.pack(side=tk.LEFT)
        self.window.title('Stopwatch (Class)')

    def start(self):
        if not self.running:
            self.running = True
            threading.Thread(target=self.update_time_stopwatch).start()
            self.start_button.config(state='disabled')
            # self.stopwatch_label.after(1000)
            # self.update()

    def pause(self):
        if self.running:
            # self.stopwatch_label.after_cancel(self.update_time)
            self.running = False
            self.start_button.config(state='active')

    def reset(self):
        if self.running:
            # self.stopwatch_label.after_cancel(self.update_time)
            self.running = False
        self.start_button.config(state='active')
        self.passed = 0
        self.stopwatch_label.config(text=self.format_time_string(self.passed))
        # self.hours, self.minutes, self.seconds = 0, 0, 0
        # self.stopwatch_label.config(text='00:00:00')
    
    def format_time_string(self, time_passed):
        seconds = time_passed % 60
        minutes = time_passed // 60
        hours   = minutes // 60
        return f"{int(hours):02d}:{int(minutes):02d}:{int(seconds):02d}:{int((self.passed)%1*100):02d}"

    def update_time_stopwatch(self):
        start = time.time()
        if self.running:
            until_now = self.passed
        else:
            until_now = 0
        while self.running:
            self.passed = time.time() - start + until_now
            self.stopwatch_label.config(text=self.format_time_string(self.passed))

    def update(self):
        # self.miliseconds += 1
        # if self.miliseconds == 100:
        self.seconds += 1
            # self.miliseconds = 0
        if self.seconds == 60:
            self.minutes += 1
            self.seconds = 0
        if self.minutes == 60:
            self.hours += 1
            self.minutes = 0
        hours_string = f'{self.hours}' if self.hours > 9 else f'0{self.hours}'
        minutes_string = f'{self.minutes}' if self.minutes > 9 else f'0{self.minutes}'
        seconds_string = f'{self.seconds}' if self.seconds > 9 else f'0{self.seconds}'
        miliseconds_string = f'{self.miliseconds}' if self.miliseconds > 9 else f'0{self.miliseconds}'
        self.stopwatch_label.config(text=hours_string + ':' + minutes_string + ':' + seconds_string)
        # self.stopwatch_label.config(text=hours_string + ':' + minutes_string + ':' + seconds_string + ':' + miliseconds_string)
        self.update_time = self.stopwatch_label.after(1000, self.update)