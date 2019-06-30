from tkinter import *
from tkinter import ttk


class ComboboxButtons(object):

    """
    Combo box buttons set up:
    1. Choose number of equipment when expeditions finished.
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

    def run_combobox_buttons(self):
        combobox_pos = len(self.check_button_text) + 1  # Combobox position under the check buttons.
        for label, item in self.combobox_label_items.items():
            label_of_combobox = Label(self.win_root, text=label)  # Label/name for check button.
            label_of_combobox.grid(row=combobox_pos, column=0, sticky=W, padx=0, pady=10)  # Label position.
            combobox = ttk.Combobox(self.win_root, value=item, width=10)
            combobox.set(self.combobox_init_items_value[label])  # Initial set up for combobox.
            combobox.grid(row=combobox_pos, column=1, sticky=W, padx=0, pady=10)  # Combobox position.
            combobox_pos += 1
