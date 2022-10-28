import os
from pathlib import Path
import PySimpleGUI as sg
from datetime import datetime

class KeyLogDisplay:
    def __init__(self) -> None:
        self.date = datetime.now().date()
        
    def getLayout(self):
        return []