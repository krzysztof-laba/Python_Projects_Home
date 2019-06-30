from tkinter import *
from tkinter import ttk
from Selenium.Blood_Wars.CheckButtons import CheckButtons


class MainWindowBW(object):

    def __init__(self, win_root):
        self.win_root = win_root  # Parameter from instance of the class Tkinter. Create main window.

        # MAIN WINDOW. Settings:
        self.window_name = "Blood Wars"  # Title of the main window.
        self.window_width = 700  # Width of the main window.
        self.window_height = 700  # Height of the main window.
        self.window_pos_x = +1150  # Position 'x' of the main window.
        self.window_pos_y = +400  # Position 'y' of the main window.

        # CHECK BUTTONS. Positions and name [y_position: description]:
        self.check_button_text = {1: "Time sleep before expeditions (min.):",
                                  2: "Dress up the expedition's equipment.",
                                  3: "Give back the expedition's equipment.",
                                  4: "Log off the browser.",
                                  5: "Close the browser.",
                                  6: "Shutdown the PC."}

        # CHECK BUTTONS. Initial values {button selection, initial value}:
        self.sel_list = {"selected_1": 0, "selected_2": 1, "selected_3": 1,
                         "selected_4": 1, "selected_5": 1, "selected_6": 0}
        self.sel_name_list = []  # List with initial values for check buttons.
        for sel_name, init in self.sel_list.items():
            # Set initial value and name for default settings of the check button.
            self.sel_name = IntVar(self.win_root, value=init, name=sel_name)  # Set up init value for instance.
            self.sel_name_list.append(self.sel_name)  # Add to the list initial button's value.

        # COMBOBOX LABELS. Name and set up items {name: [items, items_1, etc]}:
        self.combobox_label_items = {"The set number after the expeditions:":
                                         ["Set 4", "Set 5", "Set 13", "Set 15"],
                                     "The set number after the expeditions 1:":
                                         ["Set 24", "Set 25", "Set 23", "Set 35"],
                                     "The set number after the expeditions 2:":
                                         ["Set 24", "Set 25", "Set 23", "Set 35"],
                                     "The set number after the expeditions 3:":
                                         ["Set 24", "Set 25", "Set 23", "Set 35"],
                                     "The set number after the expeditions 4:":
                                         ["Set 24", "Set 25", "Set 23", "Set 35"]}

        # COMBOBOX BUTTONS. initial items value {label name: default_set_up}:
        self.combobox_init_items_value = {"The set number after the expeditions:": "Set 5",
                                          "The set number after the expeditions 1:": "Set 24",
                                          "The set number after the expeditions 2:": "Set 25",
                                          "The set number after the expeditions 3:": "Set 35",
                                          "The set number after the expeditions 4:": "Set 23"}






        # SPIN BOXES.
        self.spin_boxes_name = {1: DISABLED, 2: NORMAL, 3: DISABLED,
                                4: DISABLED, 5: DISABLED, 6: DISABLED}

        self.spin_list = {"enable_1": DISABLED, "enable_2": NORMAL, "enable_3": DISABLED,
                          "enable_4": NORMAL, "enable_5": DISABLED, "enable_6": DISABLED}
        # self.spin_name_list = []
        self.spin_name_list = [DISABLED, NORMAL, DISABLED, NORMAL, DISABLED, NORMAL]
        # for spin_name, init in self.spin_list.items():
        #     print(spin_name, init.capitalize())
        #     self.spin_name = IntVar(self.win_root, value=init, name=spin_name)
        #     self.spin_name_list.append(self.spin_name)
        # print(self.spin_name_list)
        # print(self.spin_name_list[0])



    def run_window_bw(self):
        self.main_window_settings()  # Run main window.
        self.check_buttons()  # Run check buttons in main window.
        self.combobox_buttons()  # Run combobox buttons in main window.
        self.spinbox()  # Run spin boxes in main Window.

    def main_window_settings(self):
        # Window geometry and position:
        self.win_root.geometry("{0}x{1}+{2}+{3}".format(self.window_width, self.window_height,
                                                        self.window_pos_x, self.window_pos_y))
        self.win_root.title(self.window_name)  # Title (header) of the main window.

    def check_buttons(self):
        # Check buttons - basic settings (text, variable - state button, color, position-offset, etc):
        for pos, txt in self.check_button_text.items():
            if pos == 1 or pos == 6:  # Unselected check buttons.
                # Checkbutton: text, init value, foreground color, margin x and y.
                checkbutton = Checkbutton(self.win_root, text=txt, variable=self.sel_name_list[pos-1], onvalue=1,
                                          offvalue=0, fg="black", padx=0, pady=10, command=self.spinbox_enabled)
                checkbutton.grid(row=pos, sticky=W)  # Position in a grid.

            else:  # Selected check buttons.
                # Checkbutton: text, init value, foreground color, margin x and y.
                checkbutton = Checkbutton(self.win_root, text=txt, variable=self.sel_name_list[pos-1], onvalue=1,
                                          offvalue=0, fg="black", padx=0, pady=10, command=self.spinbox_enabled)
                checkbutton.grid(row=pos, sticky=W)  # Position in a grid.

    def combobox_buttons(self):
        combobox_pos = len(self.check_button_text) + 1  # Combobox position under the check buttons.
        for label, item in self.combobox_label_items.items():
            label_of_combobox = Label(self.win_root, text=label)  # Label/name for check button.
            label_of_combobox.grid(row=combobox_pos, column=0, sticky=W, padx=0, pady=10)  # Label position.
            combobox = ttk.Combobox(self.win_root, value=item, width=10)
            combobox.set(self.combobox_init_items_value[label])  # Initial set up for combobox.
            combobox.grid(row=combobox_pos, column=1, sticky=W, padx=0, pady=10)  # Combobox position.
            combobox_pos += 1

    def spinbox(self):
        for pos, init_val in self.spin_boxes_name.items():
            spinbox = Spinbox(self.win_root, from_=0, to=600, width=5, state=self.spin_name_list[pos-1])
            spinbox.grid(row=pos, column=1, sticky=W, padx=0, pady=10)

    def spinbox_enabled(self):
        if self.sel_name_list[0].get() == 1:
            print("Enable")
        else:
            print("Disable")
