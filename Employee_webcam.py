import cv2
import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk

class WebcamApp:
    def __init__(self, window, window_title):
        self.window = window
        self.window.title(window_title)
        
        self.vid = cv2.VideoCapture(0)
        
        self.canvas = tk.Canvas(window, width=self.vid.get(cv2.CAP_PROP_FRAME_WIDTH), height=self.vid.get(cv2.CAP_PROP_FRAME_HEIGHT))
        self.canvas.pack()
        
        self.btn_play = tk.Button(window, text="Play", width=10, command=self.play)
        self.btn_play.pack(pady=10)
        
        self.btn_start_recording = tk.Button(window, text="Start Recording", width=15, command=self.start_recording)
        self.btn_start_recording.pack(pady=10)
        
        self.btn_stop_recording = tk.Button(window, text="Stop Recording", width=15, command=self.stop_recording, state=tk.DISABLED)
        self.btn_stop_recording.pack(pady=10)
        
        self.btn_take_screenshot = tk.Button(window, text="Take Screenshot", width=15, command=self.take_screenshot)
        self.btn_take_screenshot.pack(pady=10)
        
        self.is_playing = False
        self.is_recording = False
        self.out = None
        
        self.update()
        self.window.mainloop()
        
    def play(self):
        self.is_playing = not self.is_playing

    def start_recording(self):
        fourcc = cv2.VideoWriter_fourcc(*'XVID')
        self.out = cv2.VideoWriter('output.avi', fourcc, 20.0, (int(self.vid.get(3)), int(self.vid.get(4))))
        self.is_recording = True
        self.btn_start_recording.config(state=tk.DISABLED)
        self.btn_stop_recording.config(state=tk.NORMAL)

    def stop_recording(self):
        self.is_recording = False
        self.out.release()
        messagebox.showinfo("Recording Stopped", "Video saved as 'output.avi'")
        self.btn_start_recording.config(state=tk.NORMAL)
        self.btn_stop_recording.config(state=tk.DISABLED)

    def take_screenshot(self):
        ret, frame = self.vid.read()
        if ret:
            cv2.imwrite('screenshot.png', cv2.cvtColor(frame, cv2.COLOR_BGR2RGB))
            messagebox.showinfo("Screenshot Taken", "Screenshot saved as 'screenshot.png'")

    def update(self):
        if self.is_playing:
            ret, frame = self.vid.read()
            if ret:
                self.photo = ImageTk.PhotoImage(image=Image.fromarray(cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)))
                self.canvas.create_image(0, 0, image=self.photo, anchor=tk.NW)
        if self.is_recording:
            ret, frame = self.vid.read()
            if ret:
                self.out.write(frame)
        self.window.after(10, self.update)

    def __del__(self):
        if self.vid.isOpened():
            self.vid.release()
        if self.out is not None:
            self.out.release()

# Create a window and pass it to the WebcamApp class
root = tk.Tk()
app = WebcamApp(root, "Webcam App")


# This code creates a GUI with buttons to play the webcam, start recording, stop recording, and take a screenshot. Clicking the "Play" button will start displaying the webcam feed. Clicking the "Start Recording" button will start recording the webcam feed and save it as `output.avi` in the current directory. Clicking the "Stop Recording" button will stop the recording. Clicking the "Take Screenshot" button will capture a screenshot and save it as `screenshot.png` in the current directory.
