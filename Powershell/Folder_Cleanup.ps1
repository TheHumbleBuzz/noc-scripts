# This Script will delete the folder listed
# If you put \ at the end, it will remove anything inside the folder and not the folder itself

# For Windows directories, you can list them as follows
Remove-Item -Path "$env:windir\temp\*" -Recurse -Force
Remove-Item -Path "$env:userprofile\Downloads\*" -Recurse -Force

# For network locations, just put the full path
Remove-Item -Path "\\networklocation*" -Recurse -Force

# Empty Recycle Bin
Clear-RecycleBin -Force

