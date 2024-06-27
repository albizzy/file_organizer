# file_organizer/organizer.py

import os
import shutil
import argparse

def scan_directory(src_dir):
    file_types = {
        'images': ['.jpg', '.jpeg', '.png', '.gif', '.bmp'],
        'documents': ['.pdf', '.docx', '.doc', '.txt', '.xlsx', '.pptx'],
        'scripts': ['.py', '.js', '.sh', '.bat', '.ps1'],
        'archives': ['.zip', '.tar', '.gz', '.rar'],
        'videos': ['.mp4', '.avi', '.mov', '.mkv'],
        'audio': ['.mp3', '.wav', '.aac']
    }
    
    available_types = {key: False for key in file_types.keys()}
    
    for file in os.listdir(src_dir):
        if os.path.isfile(os.path.join(src_dir, file)):
            for folder, exts in file_types.items():
                if any(file.lower().endswith(ext) for ext in exts):
                    available_types[folder] = True
    
    return available_types, file_types

def organize_files(src_dir):
    available_types, file_types = scan_directory(src_dir)

    # Create only the necessary folders
    for folder, needed in available_types.items():
        if needed:
            folder_path = os.path.join(src_dir, folder)
            os.makedirs(folder_path, exist_ok=True)

    # Move files to corresponding folders
    for file in os.listdir(src_dir):
        file_path = os.path.join(src_dir, file)
        if os.path.isfile(file_path):  # Ensure it's a file
            moved = False
            for folder, exts in file_types.items():
                if any(file.lower().endswith(ext) for ext in exts):
                    shutil.move(file_path, os.path.join(src_dir, folder, file))
                    moved = True
                    break
            if not moved:
                others_path = os.path.join(src_dir, 'others')
                os.makedirs(others_path, exist_ok=True)
                shutil.move(file_path, os.path.join(others_path, file))

    print("Files organized successfully.")

def main():
    parser = argparse.ArgumentParser(description='Organize files in a directory based on their extensions.')
    parser.add_argument('src_dir', type=str, help='The source directory to organize')
    args = parser.parse_args()
    
    organize_files(args.src_dir)

if __name__ == "__main__":
    main()