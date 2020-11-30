from PIL import Image as I

def make_square(image):
        w,h = image.size
        if w > h:
                image1 = image.crop((0, 0, w ,w - h))  
                return image1
        elif w < h:
                image1 = image.crop((0,0, h-w,h))
                return image1
        else:
                return image
        