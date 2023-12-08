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
                img_path = os.path.join(dirpath, filename)
                if ' ' in img_path:
                    logging.error(f'File or path name contains spaces: {img_path}')
                    continue
                hr_image_paths.append(img_path)

    for dirpath, _, filenames in os.walk(lr_folder):
        for filename in filenames:
            if filename.endswith('.png'):
                img_path = os.path.join(dirpath, filename)
                if ' ' in img_path:
                    logging.error(f'File or path name contains spaces: {img_path}')
                    continue
                lr_image_paths.append(img_path)

    if not hr_image_paths or not lr_image_paths:
        logging.error("No images found in the provided folders.")
        return

    with open(output_file, 'w') as txt_file:
        for hr_image_path, lr_image_path in zip(hr_image_paths, lr_image_paths):
            try:
                hr_img = Image.open(hr_image_path)
                lr_img = Image.open(lr_image_path)

                if hr_img.mode == 'RGBA' or lr_img.mode == 'RGBA':
                    logging.error(f'Unsupported mode. Images should not be RGBA. Detected modes: HR: {hr_img.mode}, LR: {lr_img.mode}')
                    continue

                if hr_img.mode == 'RGB' or lr_img.mode == 'RGB':
                    n_channel = 3
                elif hr_img.mode == 'L' or lr_img.mode == 'L':
                    n_channel = 1
                else:
                    logging.error(f'Unsupported mode. Images should be RGB or L. Detected modes: HR: {hr_img.mode}, LR: {lr_img.mode}')
                    continue

                img_name_gt = os.path.basename(hr_image_path)
                img_name_lq = os.path.basename(lr_image_path)

                txt_file.write(f'{img_name_gt}, {img_name_lq}, {n_channel}\n')
                logging.info(f"Processed {img_name_gt} and {img_name_lq}")
            except Exception as e:
                logging.error(f'Error processing {hr_image_path} and {lr_image_path}: {str(e)}')

if __name__ == "__main__":
    generate_meta_info_div2k('PATH/TO/HR', 'PATH/TO/LR', 'output.txt') # Ensure your files are in perfect matching order
