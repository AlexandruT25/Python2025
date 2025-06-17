#download_images.py
import os
import requests

# List of image URLs
image_urls = [
    "https://www1.bcaimage.com/GetDoc.aspx?DocType=VehicleImage&docId=557680166&width=310",
"https://www1.bcaimage.com/GetDoc.aspx?DocType=VehicleImage&docId=557680166&width=310",
"https://www1.bcaimage.com/GetDoc.aspx?DocType=VehicleImage&docId=557680169&width=96",
"https://www1.bcaimage.com/GetDoc.aspx?DocType=VehicleImage&docId=557680170&width=96",
"https://www1.bcaimage.com/GetDoc.aspx?DocType=VehicleImage&docId=557680172&width=96",
"https://www1.bcaimage.com/GetDoc.aspx?DocType=VehicleImage&docId=557680174&width=96",
"https://www1.bcaimage.com/GetDoc.aspx?DocType=VehicleImage&docId=557680166",
"https://www1.bcaimage.com/GetDoc.aspx?DocType=VehicleImage&docId=557680166&width=200",
"https://www1.bcaimage.com/GetDoc.aspx?DocType=VehicleImage&docId=557680169&width=200",
"https://www1.bcaimage.com/GetDoc.aspx?DocType=VehicleImage&docId=557680170&width=200",
"https://www1.bcaimage.com/GetDoc.aspx?DocType=VehicleImage&docId=557680172&width=200",
"https://www1.bcaimage.com/GetDoc.aspx?DocType=VehicleImage&docId=557680174&width=200",
"https://www1.bcaimage.com/GetDoc.aspx?DocType=VehicleImage&docId=557680176&width=200",
"https://www1.bcaimage.com/GetDoc.aspx?DocType=VehicleImage&docId=557680177&width=200",
"https://www1.bcaimage.com/GetDoc.aspx?DocType=VehicleImage&docId=557680179&width=200",
"https://www1.bcaimage.com/GetDoc.aspx?DocType=VehicleImage&docId=557680180&width=200",
"https://www1.bcaimage.com/GetDoc.aspx?DocType=VehicleImage&docId=557680182&width=200",
"https://www1.bcaimage.com/GetDoc.aspx?DocType=VehicleImage&docId=557680183&width=200",
"https://www1.bcaimage.com/GetDoc.aspx?DocType=VehicleImage&docId=557680184&width=200"
]

# Create a directory to save the images
if not os.path.exists("downloaded_images"):
    os.makedirs("downloaded_images")

# Function to download the images
def download_image(url, folder):
    try:
        # Send a GET request to the image URL
        response = requests.get(url)
        # Get the image name from the URL
        image_name = url.split("=")[-1] + ".jpg"
        # Create a path for saving the image
        image_path = os.path.join(folder, image_name)
        # Write the image content to a file
        with open(image_path, "wb") as file:
            file.write(response.content)
        print(f"Downloaded {image_name}")
    except Exception as e:
        print(f"Failed to download {url}: {e}")

# Loop through all image URLs and download them
for url in image_urls:
    download_image(url, "downloaded_images")
