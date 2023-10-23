from rembg import remove
from PIL import Image
import easygui

input_path = easygui.fileopenbox("Select Image File")
output_path = easygui.filesavebox("Save file to...")

image_file = Image.open(input_path)
output = remove(image_file)
output.save(output_path)