import os
import cv2
import csv

def analyze_images_in_directory(directory):
    results = []
    for root, dirs, files in os.walk(directory):
        for file in files:
            if file.lower().endswith(('.png', '.jpg', '.jpeg', '.bmp', '.tiff', '.gif', '.webp')):
                file_path = os.path.join(root, file)
                image = cv2.imread(file_path)

                # Image size in MB with rounding to 1 decimal place
                file_size = round(os.path.getsize(file_path) / (1024), 2)

                # Image dimensions and format
                height, width = image.shape[:2]
                format = file.split('.')[-1].upper()

                results.append({
                    'File': str(file_path).replace('C:\\Users\\Vadym\\Documents\\GitHub\\web_project\\assets\\img\\', ''),
                    'Size_KB': file_size,
                    'Width': width,
                    'Height': height,
                    'Format': format
                })
    return results

# Function to print image data in a more beautiful way
def print_beautiful_data(data):
    for item in data:
        print("File:", item['File'])
        print("Size:", item['Size_KB'], "KB")
        print("Dimensions:", item['Width'], "x", item['Height'], "pixels")
        print("Format:", item['Format'])
        print("-" * 30)  # Separator for each entry


def save_data_to_csv(data, filename):
    # Field names for the CSV
    fieldnames = ['File', 'Size_KB', 'Width', 'Height', 'Format']

    with open(filename, 'w', newline='', encoding='utf-8') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

        # Writing the headers
        writer.writeheader()

        # Writing the data
        for row in data:
            writer.writerow(row)

# Example usage
image_data = analyze_images_in_directory('C:\\Users\\Vadym\\Documents\\GitHub\\web_project\\assets\\img')
csv_filename = 'webp_sized_image_data.csv' 
save_data_to_csv(image_data, csv_filename)
