import os

# Set the path to your image folder
folder_path = r"image/folder/path"

if not os.path.isdir(folder_path):
    print(f"The path {folder_path} does not exist. Please check and try again.")
    exit()


allowed_extensions = ['.jpg', '.jpeg', '.png', '.gif', '.bmp', '.tiff']
image_files = [
    f for f in os.listdir(folder_path)
    if os.path.isfile(os.path.join(folder_path, f)) and os.path.splitext(f)[1].lower() in allowed_extensions
]

image_files.sort()

# Rename files to temporary names if conflicts exist
for i, image in enumerate(image_files, 1):
    extension = os.path.splitext(image)[1]
    new_name = f"{i}{extension}"
    
    old_path = os.path.join(folder_path, image)
    new_path = os.path.join(folder_path, new_name)
    

    if os.path.exists(new_path):
        temp_name = f"temp_{i}{extension}"
        temp_path = os.path.join(folder_path, temp_name)
        os.rename(new_path, temp_path) 
        print(f"Renamed conflicting file: {new_name} --> {temp_name}")
    
    os.rename(old_path, new_path)
    print(f"Renamed: {image} --> {new_name}")


temp_files = [
    f for f in os.listdir(folder_path)
    if f.startswith("temp_")
]

for temp_file in temp_files:
    temp_index = temp_file.split("_")[1].split(".")[0]
    temp_extension = os.path.splitext(temp_file)[1]
    final_name = f"{temp_index}{temp_extension}"
    
    temp_path = os.path.join(folder_path, temp_file)
    final_path = os.path.join(folder_path, final_name)
    
    os.rename(temp_path, final_path)
    print(f"Corrected temporary file: {temp_file} --> {final_name}")

print("Renaming completed!")
