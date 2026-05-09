import os
import shutil
extension = input("Enter the file extension to search for (e.g., .txt): ").lower()

folder_extensions = {
    "Images": [".jpg", ".jpeg", ".png", ".gif", ".bmp"],
    "Documents": [".pdf", ".docx", ".txt", ".xlsx"],
    "Videos": [".mp4", ".avi", ".mkv"],
    "Audio": [".mp3", ".wav", ".flac"],
    "Compressed": [".zip", ".rar", ".7z"],
    "Others": []
}

folder_path = input("Enter the folder path: ")
if not os.path.exists(folder_path):
    print("The specified folder path does not exist.")
    exit()
for file in folder_extensions.keys():
    if not os.path.exists(os.path.join(folder_path, file)):
        os.mkdir(os.path.join(folder_path, file))
for item in os.listdir(folder_path):
    item_path = os.path.join(folder_path, item)
    if os.path.isfile(item_path):
        file_extension = os.path.splitext(item)[1].lower()
        moved = False
        for folder, extensions in folder_extensions.items():
            if file_extension in extensions:
                destination = os.path.join(folder_path, folder, item)
                shutil.move(item_path, destination)
                moved = True
                break
        if not moved:
            destination = os.path.join(folder_path, "Others", item)
            shutil.move(item_path, destination)
print("Files have been organized successfully.")
    

