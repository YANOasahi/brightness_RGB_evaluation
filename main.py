from PIL import Image
import numpy as np
import os
import glob

def analyze_image(image_path):
    # Import image
    img = Image.open(image_path).convert("RGB")  # Use RGB mode
    np_img = np.array(img)  # Convert to numpy array
    
    # Brightness evaluation
    grayscale = np.dot(np_img[..., :3], [0.2989, 0.5870, 0.1140])  # Use NTSC method
    brightness = np.mean(grayscale)
    
    # Average RGB evaluation
    avg_color = np.mean(np_img, axis=(0, 1))

    return brightness, avg_color

# Image folder to import
image_folder = "/mnt/d/Users/asahi/Pictures/film_pic/role17"  # Change to your image directory
image_paths = glob.glob(os.path.join(image_folder, "*.jpg"))  # Get jpg images

# Main part
results = []  # List to store evaluation results
brightness_values = []
avg_colors = []

for img_path in image_paths:
    brightness, avg_color = analyze_image(img_path)
    results.append((os.path.basename(img_path), brightness, avg_color))
    brightness_values.append(brightness)
    avg_colors.append(avg_color)


print("**********  Results of each image  **********")

# Print results for each image
for filename, brightness, avg_color in results:
    print(f"{filename}: brightness: {brightness:.4f}, average RGB: {avg_color}")

print("**********  Overall average  **********")

# Compute and print the average of all images
if results:
    avg_brightness = np.mean(brightness_values)
    avg_rgb = np.mean(avg_colors, axis=0)
    print(f"Brightness: {avg_brightness:.4f}")
    print(f"Average RGB: {avg_rgb}")
else:
    print("No images found in the specified folder.")