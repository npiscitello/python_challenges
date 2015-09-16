# try separating out the pixels - every other, 2 interlaced frames, like in Contact
from PIL import Image

image_path = 'cave.jpg'
im = Image.open(image_path).convert('RGB')

new = Image.new('RGB', (im.size[0]/2,im.size[1]/2), (0,0,0))

for y in range(0, im.size[1]):
	for x in range(0, im.size[0]):
		if (x+y) % 2 == 0:
			new.putpixel((x/2,y/2), im.getpixel((x,y)))

save = 'ch11.png'
new.save(save)

print 'Image output - saved as %s' % save
