from tkinter import *
from AbstractClasses.Colors import Colors


class Buttons(object):

    """
    Buttons are needed to start or stop the program:
    1. After main settings START running the expeditions in Blood Wars.
    2. Do not run the main program - quit window with settings.
    """

    def __init__(self, win_root):
        self.win_root = win_root  # Parameter from instance of the class Tkinter. Create main window.
        self.start_posx = 0.7
        self.start_posy = 0.18
        self.stop_posy = self.start_posy + 0.3

    def run_buttons(self):
        # Start button:
        start_button = Button(self.win_root, text="START", fg="dark green", width=15, height=7,
                              activebackground="green", activeforeground="light green", font="22",
                              bd=5, command=self.press_start)
        start_button.place(relx=self.start_posx, rely=self.start_posy, anchor=CENTER)

        # Start button:
        stop_button = Button(self.win_root, text="STOP", fg="dark red", width=15, height=7,
                             activebackground="dark red", activeforeground="red", font="22",
                              bd=5, command=self.press_stop)
        stop_button.place(relx=self.start_posx, rely=self.stop_posy, anchor=CENTER)

    def press_start(self):
        self.win_root.quit()
        return True

    @staticmethod
    def press_stop():
        print(Colors.fg.red, "*** PROGRAM STOPPED ***", Colors.reset)
        quit()
