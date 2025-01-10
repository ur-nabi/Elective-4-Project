import os
import shutil

# Define the directory to organize
directory = r'C:\Users\Downloads'  # Update this path to your target directory

# Define the file type categories and their corresponding extensions
file_types = {
    'Images': ['.jpg', '.jpeg', '.png', '.gif', '.bmp'],
    'Documents': ['.pdf', '.docx', '.txt', '.xlsx', '.pptx'],
    'Videos': ['.mp4', '.mov', '.avi', '.mkv'],
    'Music': ['.mp3', '.wav', '.aac'],
    'Archives': ['.zip', '.rar', '.tar', '.gz']
}

# Create subdirectories if they don't exist
for folder in file_types.keys():
    folder_path = os.path.join(directory, folder)
    if not os.path.exists(folder_path):
        os.makedirs(folder_path)

skipped_files = []

for filename in os.listdir(directory):
    file_path = os.path.join(directory, filename)
    if os.path.isfile(file_path):  # Ensure it's a file
        file_extension = os.path.splitext(filename)[1].lower()
        for folder, extensions in file_types.items():
            if file_extension in extensions:
                try:
                    shutil.move(file_path, os.path.join(directory, folder, filename))
                    print(f"Moved: {filename} -> {folder}")
                except PermissionError:
                    print(f"Skipping '{filename}' - File in use.")
                    skipped_files.append(filename)
                break

if skipped_files:
    print("\nFiles that could not be moved:")
    for file in skipped_files:
        print(f" - {file}")
