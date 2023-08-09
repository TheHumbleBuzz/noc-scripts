import os

folder_path = ['H:/Desktop/is']

def rename_files(folder_path):
    for filename in os.listdir(folder_path):
        if filename.endswith('.jpg'):
            new_filename = filename[:-8] + filename[-4:]
            os.rename(os.path.join(folder_path, filename), os.path.join(folder_path, new_filename))