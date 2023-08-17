#This Script will delete the folder listed
#if you put \ at the end, it will remove anything inside the folder and not the folder itself
Remove-Item -Path "$env:userprofile\Downloads\*" -Recurse -Force
Remove-Item -Path "$env:windir\temp\*" -Recurse -Force
Remove-Item -Path "\\networklocation*" -Recurse -Force
