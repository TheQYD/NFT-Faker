#!/Library/Frameworks/Python.framework/Versions/3.9/bin/python3

from PIL import Image
from PIL import ImageChops


if __name__ == '__main__':

  image1 = Image.open(r"image1.png")
  image2 = Image.open(r"image2.jpg")

  image3 = ImageChops.add(image1, image2, scale=1.0, offset=0)

  image3.show()
