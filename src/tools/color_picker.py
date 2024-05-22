# import tkinter as tk
# from src.utils.window import move_window
#
#
# # Copy the color code with or without the '#' character based on the state of the Checkbutton
# # Destroy the color window
# # Hide the color window from the taskbar
# def copy_to_clipboard_close_color_window(root, color, include_hash):
#     root.clipboard_clear()
#
#     if include_hash.get():
#         root.clipboard_append(color)
#     else:
#         root.clipboard_append(color[1:])
#
#     root.destroy()
#
#
# # Create a Checkbutton to toggle the '#' character
# # Create a list to store all buttons
# # Create a button for each color
# # Create a label to display the color sample
# # Create the button with a specified width and height
# # Add the button to the list
# # Create a callback function to update the text of all buttons and the toggle button
# def create_color_picker(root, colors):
#     dialog = tk.Toplevel(root)
#     move_window(dialog, 955, 540)
#     include_hash = tk.BooleanVar(value=False)
#     buttons = []
#
#     for i, (color_name, color_code) in enumerate(colors.items()):
#         frame = tk.Frame(dialog, bg='grey')
#         frame.grid(row=i // 5 + 1, column=i % 5, padx=10, pady=10)
#
#         color_sample = tk.Label(frame, bg=color_code, width=5, height=2)
#         color_sample.pack(fill='both', expand=True)
#
#         button = tk.Button(frame, text=color_code, bg='grey', width=20, height=2,
#                            command=lambda c=color_code, cs=color_sample: copy_to_clipboard_close_color_window(dialog, c, include_hash))
#         button.pack(fill='both', expand=True)
#
#         buttons.append((button, color_code))
#
#     # Call the callback function when the state of the Checkbutton changes
#     # Create the Checkbutton after the callback function is defined
#     # Call the callback function to update the text of the checkbutton
#     def update_button_text(*args):
#         for update_button, update_color_code in buttons:
#             button_text = update_color_code if include_hash.get() else update_color_code[1:]
#             update_button.config(text=button_text)
#         checkbutton.config(
#             text="Exclude '#'" if include_hash.get() else "Include '#'")
#
#     include_hash.trace('w', update_button_text)
#
#     checkbutton = tk.Button(dialog, bg='grey', command=lambda: include_hash.set(not include_hash.get()))
#     checkbutton.grid(row=6, column=0, sticky='ew', columnspan=5, padx=10, pady=10)
#
#     update_button_text()
#
#     root.grid_propagate(False)
#     root.grid_rowconfigure(0, weight=1, minsize=10)
#     root.grid_columnconfigure(0, weight=1, minsize=10)
#
#     return root


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
