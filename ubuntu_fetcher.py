import os
import requests
from urllib.parse import urlparse
import uuid

def fetch_image():
    # Prompt user for image URL
    url = input("Enter the image URL: ").strip()

    # Directory for saving images
    save_dir = "Fetched_Images"
    os.makedirs(save_dir, exist_ok=True)

    try:
        # Request image from the web
        response = requests.get(url, timeout=10)
        response.raise_for_status()  # Raise HTTPError for bad responses

        # Try to extract filename from URL
        parsed_url = urlparse(url)
        filename = os.path.basename(parsed_url.path)

        # If no filename, generate one
        if not filename:
            filename = f"image_{uuid.uuid4().hex}.jpg"

        # Save path
        filepath = os.path.join(save_dir, filename)

        # Save in binary mode
        with open(filepath, "wb") as file:
            file.write(response.content)

        print(f"✅ Image successfully fetched and saved as: {filepath}")

    except requests.exceptions.MissingSchema:
        print("❌ Invalid URL format. Please include http:// or https://")
    except requests.exceptions.HTTPError as http_err:
        print(f"❌ HTTP error occurred: {http_err}")
    except requests.exceptions.ConnectionError:
        print("❌ Connection error. Please check your internet connection.")
    except requests.exceptions.Timeout:
        print("❌ Request timed out. Try again later.")
    except Exception as e:
        print(f"❌ An unexpected error occurred: {e}")


if __name__ == "__main__":
    fetch_image()
