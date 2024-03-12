from PIL import Image
import os

# Defining the function to convert images to PDF
def images_to_pdf(directory, output_filename='output.pdf'):
    # Defining accepted image extensions
    accepted_extensions = ('.png', '.jpg', '.jpeg', '.webp', '.bmp', '.gif')
    
    # Gathering files in the current directory with the accepted extensions
    images_list = [file for file in os.listdir(directory) if file.lower().endswith(accepted_extensions)]
    
    # Checking if there are any matching files in the directory
    if not images_list:
        print("No matching files found in the directory.")
        return

    # Sorting the images list to maintain order
    images_list.sort()

    # Opening, converting, and appending images to the image_objects list
    image_objects = []
    for image in images_list:
        img_path = os.path.join(directory, image)
        with Image.open(img_path) as img:
            # Converting images to RGB to ensure compatibility for PDF conversion
            # Ignoring animation frames in GIFs by converting them to a single image
            if img.mode != 'RGB':
                img = img.convert('RGB')
            image_objects.append(img)
    
    # Saving the images as a PDF
    image_objects[0].save(output_filename, save_all=True, append_images=image_objects[1:])

    print(f"PDF file '{output_filename}' has been created with {len(images_list)} images.")

# Calling the function with the current directory
current_directory = '.'  # Current directory
images_to_pdf(current_directory)
