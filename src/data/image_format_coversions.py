from PIL import Image


def convert_webp_to_jpg(webp_image_path: str, jpg_image_path: str):
    try:
        with Image.open(webp_image_path) as img:
            rgb_image = img.convert('RGB')

            rgb_image.save(jpg_image_path, 'JPEG')
            print(f"Image successfully converted to {jpg_image_path}")

    except Exception as e:
        print(f"An error occurred: {e}")

