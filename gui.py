from turtle import back
import PySimpleGUI as sg
from keylogging import KeyLogger

menubar = [
            sg.Button(button_text="Home", size=(10, 2), enable_events=True, pad=(0, 0), button_color="black on #9cc2ff", border_width=0, expand_x = True, expand_y = False, key="HOMEPAGE"),
            sg.Button(button_text="Key Logging", size=(10, 2), enable_events=True, pad=(0, 0), button_color="black on #9cc2ff", border_width=0, expand_x = True, expand_y = False, key="KEYLOGPAGE"),
            sg.Button(button_text="Practice", size=(10, 2), enable_events=True, pad=(0, 0), button_color="black on #9cc2ff", border_width=0, expand_x = True, expand_y = False, key="PRACTICEPAGE"),
            sg.Button(button_text="Settings", size=(10, 2), enable_events=True, pad=(0, 0), button_color="black on #9cc2ff", border_width=0, expand_x = True, expand_y = False, key="SETTINGSPAGE"),
           ]

# 1
homeLayout = [
    [sg.Text("Home Page", text_color="black", background_color="white", expand_x=True, pad=(0, 0), justification = "center", key="HOMEPAGETEXT")],
    [sg.Frame("WPM Chart", [[sg.Text("chart")]], pad = 20, element_justification="center", expand_x=True, expand_y=True), 
     sg.Frame("Streaks Calendar", [[sg.Text("calendar")]], pad = 20, element_justification="center", expand_x=True, expand_y=True)]
]

# 2
keylogLayout = [
    [sg.Text("Key Log Page", text_color="black", background_color="white", expand_x = True, pad=(0, 0), justification = "center", key="KEYLOGPAGETEXT")],
    [sg.Column(layout=[[sg.Push(), sg.Button("Start Keylogging", pad=20, key="STARTKEYLOG", visible=True, expand_x=True), sg.Push()]], justification="center"),
    sg.Column(layout=[[sg.Push(), sg.Button("Stop Keylogging", pad=20, key="STOPKEYLOG", visible=False, expand_x=True), sg.Push()]], justification="center")]
]

# 3
practiceLayout = [
    [sg.Text("Practice Page", text_color="black", background_color="white", expand_x = True, expand_y = True, pad=(0, 0), justification = "center", key="PRACTICEPAGETEXT")],
]

# 4
settingsLayout = [
    [sg.Text("Settings Page", text_color="black", background_color="white", pad=(0, 0), justification = "center", expand_x=True, key="SETTINGSPAGETEXT")],
    [sg.Text("Account Info", justification="center"),
     sg.VSeparator(),
     sg.Column([[sg.Text("name")],
      [sg.Text("email")],
      [sg.Text("password")]],
               justification="center")
    ]
]

primaryLayout = [
    menubar,
    [sg.HSeparator(pad=(0, 0))],
    [sg.Column(homeLayout, key='HOMEPAGECOL', justification="center", background_color="white", expand_x=True, expand_y=True), 
     sg.Column(keylogLayout, key='KEYLOGPAGECOL', justification="center", visible=False, expand_x=True, expand_y=True),
     sg.Column(practiceLayout, key='PRACTICEPAGECOL', justification="center", visible=False, expand_x=True, expand_y=True),
     sg.Column(settingsLayout, key='SETTINGSPAGECOL', justification="center", visible=False, expand_x=True, expand_y=True)]
]

loginLayout = [
    [sg.VPush(background_color="white")],
    [sg.Push(background_color="white"), 
     sg.Column([
         [sg.Text("Login", text_color="black", font="Helvetica 20 bold", background_color = "white", expand_x=True, expand_y=True, justification="center", pad=((0, 0), (0,40)))],
         [sg.In(pad=10, focus=True)],
         [sg.In(password_char="*", pad=10)],
         [sg.Button("LOGIN", border_width=0, expand_x=True, pad=10, key="LOGINBUTTON")]
     ], background_color="white"),
     sg.Push(background_color="white")],
    [sg.VPush(background_color="white")]
]


#  Full layout 
layout = [
    [sg.Column(primaryLayout, key="PRIMARYLAYOUT", expand_x=True, expand_y=True, visible=False),
    sg.Column(loginLayout, key="LOGINLAYOUT", background_color="white", expand_x=True, expand_y=True, justification="center")]
]

window = sg.Window(title = "FastLogger", layout = layout, size=(850,500), resizable=True, margins=(0, 0), background_color="#FFFFFF")

# Create an event loop
layout = "HOMEPAGE" # starting page
while True:
    event, values = window.read()
    if event == "Exit" or event == sg.WIN_CLOSED:
        break
    
    if event == "LOGINBUTTON":
        window["LOGINLAYOUT"].update(visible = False)
        window["PRIMARYLAYOUT"].update(visible = True)
        
    if event in ("HOMEPAGE", "KEYLOGPAGE", "PRACTICEPAGE", "SETTINGSPAGE"):
        window[f"{layout}COL"].update(visible=False)
        layout = event
        window[f"{layout}COL"].update(visible=True)
        
    if event == "STARTKEYLOG":
        keylogger = KeyLogger()
        keylogger.start()
        window["STARTKEYLOG"].update(visible = False)
        window["STOPKEYLOG"].update(visible = True)
        
    if event == "STOPKEYLOG":
        keylogger.stop()
        window["STARTKEYLOG"].update(visible = True)
        window["STOPKEYLOG"].update(visible = False)
        del keylogger

window.close()