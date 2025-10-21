import os
import shutil

def copy_readme_to_docs():
    """
    Copies the README.md file to a /docs subfolder.
    If the /docs folder doesn't exist, it will be created.
    """
    # Define source and destination paths
    source_file = '../README.md'
    destination_folder = '../docs'
    destination_file = os.path.join(destination_folder, 'README.md')

    # Check if the source file exists
    if not os.path.exists(source_file):
        print(f"Error: Source file '{source_file}' not found.")
        return

    # Create the destination folder if it doesn't exist
    try:
        os.makedirs(destination_folder, exist_ok=True)
        print(f"Directory '{destination_folder}' created or already exists.")
    except OSError as e:
        print(f"Error creating directory '{destination_folder}': {e}")
        return

    # Copy the file
    try:
        shutil.copy2(source_file, destination_file)
        print(f"Successfully copied '{source_file}' to '{destination_file}'")
    except IOError as e:
        print(f"Error copying file: {e}")

if __name__ == '__main__':
    copy_readme_to_docs()
