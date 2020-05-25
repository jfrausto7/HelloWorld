"""This script is just to get a feel for the pytesseract OCR
module and its capabilities."""
# imports
import pytesseract
from PIL import Image

print(pytesseract.image_to_string(Image.open("/Users/frausto/Downloads/62459ab7-98ca-4237-a139-89e4473e301e_fs.png")))

