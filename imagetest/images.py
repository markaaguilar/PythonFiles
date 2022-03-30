from PIL import Image, ImageFilter

# im = Image.open("space.jpg")
# rgb_im = im.convert('RGB')
# rgb_im.save('spaces.jpg')


img = Image.open('./space.jpg')
new_img = img.resize((1920ß, 640 ))
new_img.save('space2.jpg')



