import pyautogui
from screeninfo import get_monitors
import wx


# Get the display where the cursor is currently located
# Get the geometry of the display
# Calculate the center of the display
# Adjust the x and y coordinates so the window is centered on the display
# Set the window's position and size
# If the cursor is not on any display, do nothing
def move_window(frame, width, height):
    display = wx.Display.GetFromPoint(wx.GetMousePosition())
    if display != wx.NOT_FOUND:
        display_rect = wx.Display(display).GetGeometry()

        center_x = display_rect.x + display_rect.width // 2
        center_y = display_rect.y + display_rect.height // 2

        x = center_x - width // 2
        y = center_y - height // 2

        frame.SetPosition(wx.Point(x, y))
        frame.SetSize(wx.Size(width, height))
    else:
        pass


# Get the position of the cursor
# Iterate over all connected monitors
# Check if the cursor is inside the current monitor
# Calculate the center of the monitor
# If no monitor was found (which should not happen), return None
def get_cursor_monitor_center():
    mouse_x, mouse_y = pyautogui.position()

    for monitor in get_monitors():
        if monitor.x <= mouse_x < monitor.x + monitor.width and monitor.y <= mouse_y < monitor.y + monitor.height:
            center_x = monitor.x + monitor.width // 2
            center_y = monitor.y + monitor.height // 2
            return monitor, center_x, center_y

    return None, None, None
