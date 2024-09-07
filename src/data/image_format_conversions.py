import cv2


def convert_webp_to_jpg(webp_image_path: str, jpg_image_path: str):
    try:
        webp_image = cv2.imread(webp_image_path)
        cv2.imwrite(jpg_image_path, webp_image)
        print(f"Image successfully converted to {jpg_image_path}")

    except Exception as e:
        print(f"An error occurred: {e}")

