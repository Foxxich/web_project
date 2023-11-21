import os
from PIL import Image

def convert_images_to_webp(directory):
    for root, dirs, files in os.walk(directory):
        for file in files:
            if file.lower().endswith(('.png', '.jpg', '.jpeg', '.bmp')):
                image_path = os.path.join(root, file)
                webp_path = image_path.rsplit('.', 1)[0] + '.webp'

                # Converting the image to WEBP
                with Image.open(image_path) as img:
                    img.save(webp_path, 'WEBP')

                # Remove the original image file
                os.remove(image_path)

                print(f"Converted and removed '{image_path}', saved as '{webp_path}'")

# Example usage
directory = 'C:\\Users\\Vadym\\Documents\\GitHub\\web_project\\assets\\img'  # Replace with your directory path
convert_images_to_webp(directory)
