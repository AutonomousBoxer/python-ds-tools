import wx
from src.utils.window import move_window


def copy_to_clipboard_close_color_window(frame, color, include_hash):
    if wx.TheClipboard.Open():
        wx.TheClipboard.SetData(wx.TextDataObject(color[1:] if include_hash else color))
        wx.TheClipboard.Close()
    frame.Close()


def create_color_picker(parent, colors):
    frame = wx.Frame(parent, title="Color Picker", size=(1000, 450))
    frame.SetBackgroundColour(wx.WHITE)
    move_window(frame, 1000, 450)
    include_hash = False
    buttons = []

    grid_sizer = wx.GridSizer(rows=4, cols=5, vgap=10, hgap=10)
    box_sizer = wx.BoxSizer(wx.VERTICAL)

    for color_name, color_code in colors.items():
        button_sizer = wx.BoxSizer(wx.VERTICAL)
        color_sample = wx.Panel(frame, size=(50, 40))
        color_sample.SetBackgroundColour(color_code)
        button = wx.Button(frame, label=color_code, size=(200, 40))

        button.Bind(wx.EVT_BUTTON, lambda event, c=color_code: copy_to_clipboard_close_color_window(frame, c, include_hash))

        button_sizer.Add(color_sample, 0, wx.EXPAND)
        button_sizer.Add(button, 0, wx.EXPAND)
        grid_sizer.Add(button_sizer, 0, wx.EXPAND)

        buttons.append((button, color_code))

    def update_button_text():
        nonlocal include_hash
        include_hash = not include_hash
        for update_button, update_color_code in buttons:
            update_button.SetLabel(update_color_code if not include_hash else update_color_code[1:])
        checkbutton.SetLabel("Exclude '#'" if not include_hash else "Include '#'")

    checkbutton = wx.Button(frame, size=(200, 40))
    checkbutton.Bind(wx.EVT_BUTTON, lambda event: update_button_text())

    box_sizer.Add(grid_sizer, 1, wx.EXPAND)
    box_sizer.Add(checkbutton, 0, wx.EXPAND)

    update_button_text()

    frame.SetSizer(box_sizer)
    frame.Show()

    return frame
