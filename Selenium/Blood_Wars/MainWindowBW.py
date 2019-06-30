from Selenium.Blood_Wars.CheckButtons import CheckButtons
from Selenium.Blood_Wars.ComboboxButtons import ComboboxButtons
from Selenium.Blood_Wars.SpinboxBox import SpinboxBox
from Selenium.Blood_Wars.Buttons import Buttons


class MainWindowBW(object):

    def __init__(self, win_root):
        self.win_root = win_root  # Parameter from instance of the class Tkinter. Create main window.

        # MAIN WINDOW. Settings:
        self.window_name = "Blood Wars"  # Title of the main window.
        self.window_width = 700  # Width of the main window.
        self.window_height = 700  # Height of the main window.
        self.window_pos_x = +1150  # Position 'x' of the main window.
        self.window_pos_y = +400  # Position 'y' of the main window.

    def run_window_bw(self):
        self.run_main_window_settings()  # Run all main window with every elements on it.

        checkbutton = CheckButtons(self.win_root)
        checkbutton.run_check_buttons()  # Run check buttons.

        # print(checkbutton.spinbox_visibility())
        # for i in checkbutton.spinbox_visibility():
        #     print(i)

        comboxbut = ComboboxButtons(self.win_root)
        comboxbut.run_combobox_buttons()  # Run combobox buttons.

        spinbox = SpinboxBox(self.win_root)
        spinbox.run_spinbox()  # Runs spin box buttons.

        buttons = Buttons(self.win_root)
        buttons.run_buttons()

    def run_main_window_settings(self):
        # Window geometry and position:
        self.win_root.geometry("{0}x{1}+{2}+{3}".format(self.window_width, self.window_height,
                                                        self.window_pos_x, self.window_pos_y))
        self.win_root.title(self.window_name)  # Title (header) of the main window.
