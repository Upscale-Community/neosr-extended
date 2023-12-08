import os
import logging
from PIL import Image

def generate_meta_info_div2k(hr_folder, lr_folder, output_file):
    logging.basicConfig(level=logging.INFO)

    hr_image_paths = []
    lr_image_paths = []

    for dirpath, _, filenames in os.walk(hr_folder):
        for filename in filenames:
            if filename.endswith('.png'):
                hr_image_paths.append(os.path.join(dirpath, filename))

    for dirpath, _, filenames in os.walk(lr_folder):
        for filename in filenames:
            if filename.endswith('.png'):
                lr_image_paths.append(os.path.join(dirpath, filename))

    if not hr_image_paths or not lr_image_paths:
        raise ValueError("No images found in the provided folders.")

    with open(output_file, 'w') as txt_file:
        for hr_image_path, lr_image_path in zip(hr_image_paths, lr_image_paths):
            img_name_gt = os.path.basename(hr_image_path)
            img_name_lq = os.path.basename(lr_image_path)
            txt_file.write(f'({img_name_gt}), ({img_name_lq})\n')
            logging.info(f"Processed {img_name_gt} and {img_name_lq}")

if __name__ == "__main__":
    generate_meta_info_div2k('PATH/TO/HR', 'PATH/TO/LR', 'output.txt') # Ensure your files are in perfect matching order
