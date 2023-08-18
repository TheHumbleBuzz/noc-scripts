# This was my first iteration of cleaning up folders. I was only able to do one folder at a time. IF you find a way to list and search multiple folders go for it. 

import os
import shutil

# Set the path to your downloads folder
downloads_folder = 'H:/Downloads'

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
