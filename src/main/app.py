import wx
import keyboard
from src.tools.color_picker import create_color_picker
from src.tools.icon_creator import DnDFrame
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

        # Create a button for the icon creator tool
        self.icon_creator_button = wx.Button(self, label="Icon Creator")
        self.icon_creator_button.Bind(wx.EVT_BUTTON, self.on_icon_creator)

        # Create a button for closing the window
        self.close_button = wx.Button(self, label="Close")
        self.close_button.Bind(wx.EVT_BUTTON, self.on_close)

        # Create a horizontal sizer for the color picker and icon creator buttons
        tool_sizer = wx.BoxSizer(wx.HORIZONTAL)
        tool_sizer.Add(self.color_picker_button, 1, wx.EXPAND)
        tool_sizer.Add(self.icon_creator_button, 1, wx.EXPAND)

        # Create a vertical sizer for the main layout
        main_sizer = wx.BoxSizer(wx.VERTICAL)
        main_sizer.Add(tool_sizer, 1, wx.EXPAND)  # Add the tool sizer to the main sizer
        main_sizer.Add(self.close_button, 1, wx.EXPAND)  # Add the close button to the main sizer

        self.SetSizer(main_sizer)

    def on_color_picker(self, event):
        self.Hide()
        create_color_picker(self, colors)
        self.update_button_text()

    def on_icon_creator(self, event):
        self.Hide()
        icon_creator_frame = DnDFrame(self)
        icon_creator_frame.Show(True)
        self.update_button_text()

    def update_button_text(self):
        self.color_picker_button.SetLabel(self.color_picker_button.GetLabel())
        self.close_button.SetLabel(self.close_button.GetLabel())

    def on_close(self, event):
        self.Hide()
        self.update_button_text()

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
