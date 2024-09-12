import os

import cv2


def convert_to_jpg(image_path: str):
    try:
        image = cv2.imread(image_path)
        root, _ = os.path.splitext(image_path)
        cv2.imwrite(f'{root}.jpg', image)
        print(f"Image successfully converted to {root}.jpg.")

    except Exception as e:
        print(f"An error occurred: {e}")

