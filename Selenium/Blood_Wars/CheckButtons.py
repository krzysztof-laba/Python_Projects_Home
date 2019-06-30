from tkinter import *


class CheckButtons(object):

    """
    Check buttons are needed to select what the program should to do:
    1. Time sleep before run the program.
    2. If dress up or not expeditions's equipment before run the expeditions.
    3. If give back expedition's equipment after expeditions.
    4. Log off from web page Blood Wars.
    5. Close or not web browser after running program.
    6. Shut down or not the PC.
    """

    def __init__(self, win_root):
        self.win_root = win_root  # Parameter from instance of the class Tkinter. Create main window.

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

    def run_check_buttons(self):
        # Check buttons - basic settings (text, variable - state button, color, position-offset, etc):
        for pos, txt in self.check_button_text.items():
            if pos == 1 or pos == 6:  # Unselected check buttons.
                # Checkbutton: text, init value, foreground color, margin x and y.
                checkbutton = Checkbutton(self.win_root, text=txt, variable=self.sel_name_list[pos-1], onvalue=1,
                                          offvalue=0, fg="black", padx=0, pady=10, command=self.spinbox_visibility)
                checkbutton.grid(row=pos, sticky=W)  # Position in a grid.

            else:  # Selected check buttons.
                # Checkbutton: text, init value, foreground color, margin x and y.
                checkbutton = Checkbutton(self.win_root, text=txt, variable=self.sel_name_list[pos-1], onvalue=1,
                                          offvalue=0, fg="black", padx=0, pady=10, command=self.spinbox_visibility)
                checkbutton.grid(row=pos, sticky=W)  # Position in a grid.

    def spinbox_visibility(self):
        print("\n>>> Check Box values:")
        lista = []
        for item in self.check_button_text.keys():
            i = item - 1
            if self.sel_name_list[i].get() == 1:
                # print("Enable: {0}".format(self.check_button_text[item]))
                lista.append(NORMAL)
            elif self.sel_name_list[i].get() == 0:
                # print("Disable: {0}".format(self.check_button_text[item]))
                lista.append(DISABLED)
        # print("Lista =", lista)
        print(lista)
        return lista
