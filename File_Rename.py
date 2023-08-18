# This script cam out of nessesity. I had hundreds of staff photos.
# The name of each file started with the lastname of the staff member and ended with their employee number
# I needed a way to take out the name and leave the numbers
# I stumbled my way to this solution
# It will take out everything except the last 4-5 numbers

import os
import shutil

folders = ['C:/Users/Username/Photos']

for folder in folders:
    for filename in os.listdir(folder):
        file_path = os.path.join(folder, filename)
        try:
            if filename.endswith(".jpg"):
                 new_filename = filename[-5-4:]
                 os.rename(os.path.join(folder, filename), os.path.join(folder, new_filename))
            elif os.path.isdir(file_path):
                shutil.rmtree(file_path)
        except Exception as e:
            print(f'Failed to delete {file_path}. Reason: {e}')
