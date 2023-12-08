import logging
import os
from PIL import Image

def generate_meta_info_div2k():
    """Generate meta info for DIV2K dataset."""

    # Set up logging to print to console
    logging.basicConfig(level=logging.INFO)

    gt_folder = 'PATH/TO/HR'
    meta_info_txt = 'hfa2k_metainfo.txt'

    img_list = []
    for dirpath, dirnames, filenames in os.walk(gt_folder):
        for filename in filenames:
            img_path = os.path.normpath(os.path.join(dirpath, filename))
            if ' ' in img_path:
                logging.error(f'File or path name contains spaces: {img_path}')
                continue
            img_list.append(img_path)

    if not img_list:
        logging.error('No images found')
        return

    with open(meta_info_txt, 'w') as f:
        for idx, img_path in enumerate(img_list):
            try:
                img = Image.open(img_path)  # lazy load
                mode = img.mode
                if mode == 'RGBA':
                    logging.error(f'Unsupported mode. Images should not be RGBA. Detected image mode: {mode}')
                    continue

                if mode == 'RGB':
                    n_channel = 3
                elif mode == 'L':
                    n_channel = 1
                else:
                    logging.error(f'Unsupported mode. Images should be RGB or L. Detected image mode: {mode}')
                    continue
            except Exception as e:
                logging.error(f'Error processing {img_path}: {str(e)}')
if __name__ == '__main__':
    generate_meta_info_div2k()
