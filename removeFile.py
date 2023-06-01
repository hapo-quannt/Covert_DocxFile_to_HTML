import os
import glob

def delete_old_file(file_name):
    if os.path.exists(file_name):
        os.remove(file_name)

    image_files = glob.glob('*.png') + glob.glob('*.jpg')
    for image_file in image_files:
        os.remove(image_file)
