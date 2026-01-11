import os
import shutil

def copy_static(src_dir, des_dir): 
    if not os.path.exists(src_dir):
        print("Source directory does not exist.")
        return

    if not os.path.exists(des_dir):
        print("Destination directory does not exist.")
        return

    delete_directory_contents(des_dir)

    list_of_dir = os.listdir(path=src_dir)
    for item in list_of_dir:
        src_path = os.path.join(src_dir, item)
        des_path = os.path.join(des_dir, item)
        if os.path.isdir(src_path):
            os.mkdir(des_path)
            copy_static(src_path, des_path)
        else:
            shutil.copy2(src_path, des_path)        

def delete_directory_contents(directory_path):
    """Delete all files and subdirectories from a directory."""
    try:
        for filename in os.listdir(directory_path):
            file_path = os.path.join(directory_path, filename)
            if os.path.isfile(file_path) or os.path.islink(file_path):
                os.unlink(file_path)
            elif os.path.isdir(file_path):
                shutil.rmtree(file_path)
    except Exception as e:
        print(f"Error: {e}")


