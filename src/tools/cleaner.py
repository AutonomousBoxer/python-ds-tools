import pandas as pd
import os


def clean_excel_file(file_path):
    # Load the Excel file
    df = pd.read_excel(file_path, header=3)

    # Drop the empty rows and columns
    df = df.dropna(how='all')  # Drops the rows where all cells are NaN
    df = df.dropna(how='all', axis=1)  # Drops the columns where all cells are NaN

    # Create a new file path with '_cleaned' appended to the original file name
    base, extension = os.path.splitext(file_path)
    cleaned_file_path = f"{base}_cleaned{extension}"

    # Save the cleaned DataFrame back to the same Excel file
    df.to_excel(file_path, index=False)


# Specify the directory where your Excel files are
directory = r'' # e.g. r'C:\Users\JohnDoe\Documents\ExcelFiles


for filename in os.listdir(directory):
    if filename.endswith(".xlsx") or filename.endswith(".xls"):
        file_path = os.path.join(directory, filename)
        clean_excel_file(file_path)