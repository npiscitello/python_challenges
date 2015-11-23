from PIL import Image
import math

src_image_path = 'wire.png'
out_image_path = 'ch14.png'
src = Image.open(src_image_path)
square_dim = int(math.sqrt(src.size[0]))
out = Image.new('RGB', (square_dim,square_dim))
	# the number of pixels to place, the number of times this number has been
	# used to move, the direction to move (0 = x-, 1 = y+, 2 = x+, 3 = y-),
	# and the current movement counter
meta = [square_dim,1,0,0]
coord = [square_dim,0]

for i in range(0, square_dim * square_dim):
		# if at the end of the current count, add one to the use var,
		# change direction, and reset counter
	if meta[3] == meta[0]:
		meta[1] += 1
		meta[2] += 1
		meta[3] = 0
		# if the current count limit is expired, decrement it and reset
		# use var
	if meta[1] > 1:
		meta[0] -= 1
		meta[1] = 0
		# ensure direction is cyclical
	if meta[2] > 3:
		meta[2] = 0
		# change coordinates
	if meta[2] == 0:
		coord[0] -= 1
	elif meta[2] == 1:
		coord[1] += 1
	elif meta[2] == 2:
		coord[0] += 1
	elif meta[2] == 3:
		coord[1] -= 1
	meta[3] += 1
	out.putpixel((coord[0],coord[1]),(src.getpixel((i,0))))

out.save(out_image_path)

print 'image output - saved as %s' % out_image_path
