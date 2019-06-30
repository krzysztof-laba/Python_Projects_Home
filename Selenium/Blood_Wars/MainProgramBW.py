from tkinter import *
from Selenium.Blood_Wars.MainWindowBW import MainWindowBW
from AbstractClasses.Colors import Colors
from Selenium.Blood_Wars.Buttons import Buttons
from Selenium.Blood_Wars.CheckButtons import CheckButtons


window = Tk()
bw_window = MainWindowBW(window)
bw_window.run_window_bw()
window.mainloop()


lista = ['normal', 'normal', 'normal', 'normal', 'normal', 'disabled']
if Buttons(window).press_start() is True:
    print(Colors.fg.green, "*** BLOOD WARS MAIN PROGRAM ***\n", Colors.reset)
print(CheckButtons(window).run_check_buttons())