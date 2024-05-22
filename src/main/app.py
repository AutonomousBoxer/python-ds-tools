# import keyboard
# import tkinter as tk
# from src.tools.color_picker import create_color_picker
# from src.utils.window import move_window
#
# # Define the colors and their names
# colors = {
#     "Crown Beige": "#d7cdbe",
#     "Momentum Orange": "#ff980f",
#     "Dark Gray": "#151d24",
#     "Medium Gray": "#5d646a",
#     "Light Graphite": "#878c90",
#     "Crystal Silver": "#a9adb0",
#     "Blue Violet": "#23226a",
#     "Teal Blue": "#00bec8",
#     "Purple": "#7c1682",
#     "Sea Green": "#18ae76",
#     "Yellow Green": "#d2e65a",
#     "Pacific Blue": "#2985c0",
#     "Violet": "#bf2a95",
#     "Green": "#2b9936",
#     "Yellow": "#ffc400",
#     "Red": "#cd1816"
# }
#
# # Create the main application window
# root = tk.Tk()
# root.title("Tools")
#
# # Create a button for the color picker tool
# color_picker_button = tk.Button(root, text="Color Picker", bg='grey', width=20,
#                                 command=lambda: [create_color_picker(root, colors), root.withdraw()])
# color_picker_button.grid(row=0, column=0, sticky='nsew', padx=5, pady=10)
#
# # Create a button for closing the window
# close_button = tk.Button(root, text="Close", bg='grey', width=20,
#                          command=root.withdraw)
# close_button.grid(row=0, column=1, sticky='nsew', padx=5, pady=10)
#
# # Configure the grid to distribute extra space among the columns
# root.grid_columnconfigure(0, weight=1, minsize=5)
# root.grid_columnconfigure(1, weight=1, minsize=5)
#
#
# # Get the center of the monitor where the cursor is currently located
# # Get the current position of the window
# # Only hide the window if it's not on the same monitor as the cursor
# def toggle_window():
#     if root.state() == 'withdrawn':
#         root.deiconify()
#         move_window(root, 450, 50)
#     elif root.state() == 'normal':
#         move_window(root, 450, 50)
#     else:
#         root.iconify()
#         root.withdraw()
#
#     root.after(100, move_window(root, 450, 50))
#
#
# # Register a hotkey that will deiconify or iconify the root window when pressed
# keyboard.add_hotkey('ctrl+shift+a', toggle_window)
#
# # Hide the main application window when the script is run
# root.withdraw()
# root.mainloop()


import wx
import keyboard
from src.tools.color_picker import create_color_picker
from src.utils.window import move_window

# Define the colors and their names
colors = {
    "Crown Beige": "#d7cdbe",
    "Momentum Orange": "#ff980f",
    "Dark Gray": "#151d24",
    "Medium Gray": "#5d646a",
    "Light Graphite": "#878c90",
    "Crystal Silver": "#a9adb0",
    "Blue Violet": "#23226a",
    "Teal Blue": "#00bec8",
    "Purple": "#7c1682",
    "Sea Green": "#18ae76",
    "Yellow Green": "#d2e65a",
    "Pacific Blue": "#2985c0",
    "Violet": "#bf2a95",
    "Green": "#2b9936",
    "Yellow": "#ffc400",
    "Red": "#cd1816"
}


class MainFrame(wx.Frame):
    def __init__(self, parent):
        wx.Frame.__init__(self, parent, title="Tools")

        # Create a button for the color picker tool
        self.color_picker_button = wx.Button(self, label="Color Picker")
        self.color_picker_button.Bind(wx.EVT_BUTTON, self.on_color_picker)

        # Create a button for closing the window
        self.close_button = wx.Button(self, label="Close")
        self.close_button.Bind(wx.EVT_BUTTON, self.on_close)

        # Configure the grid to distribute extra space among the columns
        sizer = wx.BoxSizer(wx.HORIZONTAL)
        sizer.Add(self.color_picker_button, 1, wx.EXPAND)
        sizer.Add(self.close_button, 1, wx.EXPAND)
        self.SetSizer(sizer)

    def on_color_picker(self, event):
        self.Hide()
        create_color_picker(self, colors)
        self.update_button_text()

    def on_close(self, event):
        self.Hide()
        self.update_button_text()

    def update_button_text(self):
        self.color_picker_button.SetLabel("Color Picker")
        self.close_button.SetLabel("Hide App")


class MyApp(wx.App):
    def OnInit(self):
        self.frame = MainFrame(None)
        self.frame.Hide()
        keyboard.add_hotkey('ctrl+shift+a', self.toggle_frame)
        return True

    def toggle_frame(self):
        if self.frame.IsShown():
            self.frame.Hide()
        else:
            self.frame.Show()
            move_window(self.frame, 450, 100)  # Move the window to the center of the screen where the cursor is located
        self.frame.update_button_text()


app = MyApp()
app.MainLoop()
