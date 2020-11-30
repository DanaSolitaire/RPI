from PIL import Image as I
import check2_helper as c




im = I.new('RGB', (512,512), 'white')
first = I.open('inc4.jpg')
first = c.make_square(first).resize((256,256))
im.paste(first, (0,0))
second = I.open('inc5.jpg')
second = c.make_square(second).resize((256,256))
im.paste(second, (256,256))
third = I.open('inc1.jpg')
third = c.make_square(third).resize((256,256))
im.paste(third, (0,256))
fourth = I.open('inc2.jpg')
fourth = c.make_square(fourth).resize((256,256))
im.paste(fourth, (256,0))

im.show()