import os
import shutil

# Set the path to your downloads folder
downloads_folder = 'H:/Downloads'
windowstemp_folder = 'C:/Windows/Temp'

# Loop through all files and subdirectories in the downloads folder
for filename in os.listdir(downloads_folder):
    file_path = os.path.join(downloads_folder, filename)

    # Check if the file is a file or directory
    if os.path.isfile(file_path):
        # Delete the file
        os.remove(file_path)
    elif os.path.isdir(file_path):
        # Delete the directory and all its contents
        shutil.rmtree(file_path)