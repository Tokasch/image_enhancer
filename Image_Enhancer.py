from PIL import Image, ImageEnhance, ImageFilter
import os

path = "./Tests/Bilder"
pathout = "./Tests/Bearbeitet"

for filename in os.listdir(path):
    if filename.endswith(".jpg") or filename.endswith(".png"):
        img = Image.open(f"{path}/{filename}").rotate(-90)
        edit = img.filter(ImageFilter.SHARPEN)
        factor = 1.5
        enhancer = ImageEnhance.Contrast(edit)
        edit = enhancer.enhance(factor)
        clean_name = os.path.splitext(filename)[0]
        edit.save(f"{pathout}/{clean_name}_edited.jpg")