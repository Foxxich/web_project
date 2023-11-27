import os
from PIL import Image

def downsize_images_by_factor(directory, scale_factor):
    for root, dirs, files in os.walk(directory):
        for file in files:
            if file.lower().endswith(('.png', '.jpg', '.jpeg', '.bmp')):
                image_path = os.path.join(root, file)

                with Image.open(image_path) as img:
                    # Calculate the new size by scaling down
                    new_size = (int(img.width / scale_factor), int(img.height / scale_factor))

                    # Resize the image
                    img_resized = img.resize(new_size, Image.ANTIALIAS)

                    # Save the resized image over the original file
                    img_resized.save(image_path)

                print(f"Resized and saved '{image_path}'")

# Example usage
directory = 'C:\\Users\\Vadym\\Documents\\GitHub\\web_project\\assets\\img'
scale_factor = 1.5  # Images will be resized to 1/1.5 of their original size
downsize_images_by_factor(directory, scale_factor)
