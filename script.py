import os

# Set the path to your image folder
folder_path = r"images/path/folder"

if not os.path.isdir(folder_path):
    print(f"The path {folder_path} does not exist. Please check and try again.")
    exit()

image_files = [f for f in os.listdir(folder_path) if os.path.isfile(os.path.join(folder_path, f))]

allowed_extensions = ['.jpg', '.jpeg', '.png', '.gif', '.bmp', '.tiff']
image_files = [f for f in image_files if os.path.splitext(f)[1].lower() in allowed_extensions]

image_files.sort()

for i, image in enumerate(image_files, 1):
    extension = os.path.splitext(image)[1]
    
    new_name = f"{i}{extension}"
    
    old_path = os.path.join(folder_path, image)
    new_path = os.path.join(folder_path, new_name)
    
    os.rename(old_path, new_path)
    
    print(f"Renamed: {image} -> {new_name}")

print("Renaming completed!")
