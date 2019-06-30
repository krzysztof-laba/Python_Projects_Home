from tkinter import *


class SpinboxBox(object):

    def __init__(self, win_root):
        self.win_root = win_root  # Parameter from instance of the class Tkinter. Create main window.

        # SPIN BOXES.
        self.spin_boxes_name = {1: NORMAL, 2: DISABLED, 3: DISABLED,
                                4: DISABLED, 5: DISABLED, 6: DISABLED}

        # self.spin_list = {"enable_1": DISABLED, "enable_2": DISABLED, "enable_3": DISABLED,
        #                   "enable_4": DISABLED, "enable_5": DISABLED, "enable_6": DISABLED}

        # self.spin_name_list = [DISABLED, DISABLED, DISABLED, DISABLED, DISABLED, DISABLED]
        # for spin_name, init in self.spin_list.items():
        #     print(spin_name, init.capitalize())
        #     self.spin_name = IntVar(self.win_root, value=init, name=spin_name)
        #     self.spin_name_list.append(self.spin_name)
        # print(self.spin_name_list)
        # print(self.spin_name_list[0])

    def run_spinbox(self):
        for pos, init_val in self.spin_boxes_name.items():
            spinbox = Spinbox(self.win_root, from_=0, to=600, width=5, state=init_val)
            spinbox.grid(row=pos, column=1, sticky=W, padx=0, pady=10)
