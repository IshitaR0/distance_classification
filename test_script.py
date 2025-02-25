import wandb
import cv2
import os

wandb.init(project='distance_classification_project')

image_path = "Plaksha_Faculty.jpg"
img = cv2.imread(image_path)

if img is None:
    print(f"Failed to load image: {image_path}.")
else:
    print(f"Image loaded successfully: {image_path}.")

image_filenames = [
    "gray_scale_image.png",
    "face_detection_1.png",
    "face_clustering_1.png",
    "hue_and_saturation_clustering_1.png",
    "template_image.png",
    "face_clustering_2.png",
    "hue_and_saturation_clustering_2.png"
]

for img_file in image_filenames:
    if os.path.exists(img_file):
        wandb.log({img_file: wandb.Image(img_file)})
        print(f"Logged {img_file} to WandB.")
    else:
        print(f"Warning: {img_file} not found.")

print("All tests and WandB logging completed successfully.")

wandb.finish()