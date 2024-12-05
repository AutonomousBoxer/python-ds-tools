import os
import wx
from src.utils.file_type_converter import convert_file_type


class DnDFrame(wx.Frame):
    def __init__(self, parent=None):
        wx.Frame.__init__(self, parent, title="Icon Creator")

        # Set the window size and disable resizing
        self.output_location = None
        self.input_path = None
        self.output_name = None
        self.SetSize(500, 160)
        self.SetMinSize(self.GetSize())
        self.SetMaxSize(self.GetSize())

        # Create text boxes and buttons for selecting the file to convert, the new file name, and the save location
        self.input_text = wx.TextCtrl(self, size=(300, 30), style=wx.TE_MULTILINE)
        self.input_button = wx.Button(self, label="Select Input File", size=(125, 30))
        self.input_button.Bind(wx.EVT_BUTTON, self.on_select_file)

        self.generate_name_text = wx.TextCtrl(self, size=(300, 30), style=wx.TE_MULTILINE)
        self.generate_name_button = wx.Button(self, label="Generate FileName", size=(125, 30))
        self.generate_name_button.Bind(wx.EVT_BUTTON, self.generate_output_name)

        self.output_location_text = wx.TextCtrl(self, size=(300, 30), style=wx.TE_MULTILINE)
        self.output_location_button = wx.Button(self, label="Select Save Location", size=(125, 30))
        self.output_location_button.Bind(wx.EVT_BUTTON, self.on_select_location)

        # Create a button for converting the file
        self.convert_button = wx.Button(self, label="Convert", size=(-1, 30))
        self.convert_button.Bind(wx.EVT_BUTTON, self.on_convert)

        # Create a sizer to manage the layout of window sub-components
        sizer = wx.BoxSizer(wx.VERTICAL)

        # Create horizontal sizers for each row of textbox and button
        input_sizer = wx.BoxSizer(wx.HORIZONTAL)
        generate_name_sizer = wx.BoxSizer(wx.HORIZONTAL)
        output_location_sizer = wx.BoxSizer(wx.HORIZONTAL)

        # Add the textboxes and buttons to their respective sizers
        input_sizer.Add(self.input_text, proportion=1, flag=wx.EXPAND)
        input_sizer.Add(self.input_button)

        generate_name_sizer.Add(self.generate_name_text, proportion=1, flag=wx.EXPAND)
        generate_name_sizer.Add(self.generate_name_button)

        output_location_sizer.Add(self.output_location_text, proportion=1, flag=wx.EXPAND)
        output_location_sizer.Add(self.output_location_button)

        # Add the horizontal sizers and the convert button to the main vertical sizer
        sizer.Add(input_sizer, flag=wx.EXPAND)
        sizer.Add(generate_name_sizer, flag=wx.EXPAND)
        sizer.Add(output_location_sizer, flag=wx.EXPAND)
        sizer.Add(self.convert_button, flag=wx.EXPAND)

        self.SetSizer(sizer)

    def generate_output_name(self, event):
        # Get the input file name and remove the extension
        input_name = os.path.splitext(os.path.basename(self.input_text.GetValue()))[0]
        if not input_name:
            # Show an error message if the input file name is empty
            wx.MessageBox('Input file must be selected to generate an output name.', 'Error', wx.OK | wx.ICON_ERROR)
            return
        # Append "_icon_conversion" to the input file name
        output_name = input_name + "_icon_conversion"

        # Check if a file with this name already exists in the output location
        i = 1
        final_output_name = output_name
        while os.path.exists(os.path.join(self.output_location_text.GetValue(), final_output_name + '.ico')):
            # If it does, append "(n)" to the end of the file name
            final_output_name = output_name + "({})".format(i)
            i += 1

        # Set the output name text box value to the generated name
        self.generate_name_text.SetValue(final_output_name)

    def on_select_file(self, event):
        # Open a file dialog for the user to select a file
        with wx.FileDialog(self, "Open", wildcard="Image files (*.jpg;*.png)|*.jpg;*.png",
                           style=wx.FD_OPEN | wx.FD_FILE_MUST_EXIST) as fileDialog:
            if fileDialog.ShowModal() == wx.ID_CANCEL:
                return
            self.input_path = fileDialog.GetPath()
            self.input_text.SetValue(self.input_path)

    def on_select_location(self, event):
        # Open a directory dialog for the user to select the save location
        with wx.DirDialog(self, "Select Save Location") as dirDialog:
            if dirDialog.ShowModal() == wx.ID_CANCEL:
                return
            self.output_location = dirDialog.GetPath()
            self.output_location_text.SetValue(self.output_location)

    def on_convert(self, event):
        if not self.input_path and not self.output_location and not self.generate_name_text.GetValue():
            # Show an error message if any of the fields are empty
            wx.MessageBox('Please fill in all fields.', 'Error', wx.OK | wx.ICON_ERROR)
            return

        # Get the new file name from the text box
        self.output_name = self.generate_name_text.GetValue()

        # Construct the output path from the save location and new file name
        output_path = os.path.join(self.output_location, self.output_name + '.ico')

        # Call the convert_to_ico function to convert the selected file
        convert_to_ico(self.input_path, output_path)
        # Show a message box to inform the user that the file has been converted
        wx.MessageBox('The file has been converted to ICO format.', 'Info', wx.OK | wx.ICON_INFORMATION)


def convert_to_ico(image_path, output_path, size=(256,256)):
    convert_file_type(image_path, output_path, 'ICO', size)
