import os
from PIL import Image


def convert_file_type(image_path, output_path, new_format, size):
    img = Image.open(image_path)
    img.thumbnail(size)
    img.save(output_path, format=new_format.upper())
