# Invokation: python3 JPGtoPNG.py source_folder target_folder
# Example: python3 JPGtoPNG.py pokedox new

import sys
import os
from PIL import Image

img_folder = sys.argv[1]
outpur_folder = sys.argv[2]

if(not os.path.exists(outpur_folder)):
    os.makedirs(outpur_folder)

for filename in os.listdir(img_folder):
    clean_name = os.path.splitext(filename)[0]
    img = Image.open(f'{img_folder}/{filename}')
    img.save(f'{outpur_folder}/{clean_name}.png', 'png')


print("All files converted!")
