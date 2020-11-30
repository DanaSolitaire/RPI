import wikimedia as w
import check2_helper as ch
from PIL import Image as i

location = input('Where => ')

images = w.find_images(location,4)


if len(images) == 4:
    im = i.new('RGB', (512,512), 'blue')
    
    first = images[0]
    first = ch.make_square(first).resize((256,256))
    im.paste(first,(0,0))
    
    sec = images[1]
    sec = ch.make_square(sec).resize((256,256))
    im.paste(sec,(256,0))
    
    thr = images[2]
    thr = ch.make_square(thr).resize((256,256))
    im.paste(thr,(0,256))
    
    four = images[3]
    four = ch.make_square(four).resize((256,256))
    im.paste(four,(256,256))
    
    im.show()      