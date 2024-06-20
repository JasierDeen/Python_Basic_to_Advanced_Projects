import os
import requests

def get_extention(image_url):
    extentions = ['.jpg', '.png', '.jpeg' , '.gif', '.svg']

    for extention in extentions:
        if extention in image_url:
            return extention
        
def download_image(image_url, name, folder=None):
    ext = get_extention(image_url)
    if ext:
        if folder:
            image_name = f'{folder}/{name}{ext}'
        else:
            image_name = f'{name}{ext}'
    else:
        raise Exception("Image extension cannot be processed")

    # Check if name already exists
    if os.path.isfile(image_name):
        raise Exception("File name already exists")
    
    # Download the image
    try:
        image_content = requests.get(image_url).content
        with open(image_name, 'wb') as handler:
            handler.write(image_content)
            print(f'Downloaded {image_name} successfully!')
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":

    # Get user input for the download
    input_url = input("Enter a Url: ")
    input_name = input("What would you like to name it?")
    print("Downloading......")

    download_image(input_url, input_name, folder="images")

