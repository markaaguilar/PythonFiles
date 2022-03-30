import sys
import os
from PIL import Image

ds_store_file_location = 'Pokedex/.DS_store'
if os.path.isfile(ds_store_file_location):
    os.remove(ds_store_file_location)

# grab the first and second argument
image_folder = sys.argv[1]
output_folder = sys.argv[2]

# check if new/ exist, if not create
if not os.path.exists(output_folder):
	os.makedirs(output_folder)

for filename in os.listdir(image_folder):
	img = Image.open(f'{image_folder}{filename}')
	clean_name = os.path.splitext(filename)[0]
	img.save(f'{output_folder}{clean_name}.png', 'png')
	print('all done!')

#  loop through Pokedex
# covert images to png
# save to the new folder
