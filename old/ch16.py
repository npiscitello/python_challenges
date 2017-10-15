from PIL import Image

slice_width = 5
pattern = [(255,0,255),(255,0,255),(255,0,255),(255,0,255),(255,0,255)]
src_path = 'mozart.gif'
out_path = 'ch16.png'
	# open and convert the source image
src = Image.open(src_path).convert('RGB')
out = Image.new(src.mode,src.size)
	# use these if we wanted to continue using a palette...
#out.putpalette(src.palette)
src_pixels = list(src.getdata())
pixel_slice = []
pink_locations = []
data_list = []

	# iterate down the image rows
for y in range(src.size[1]):
		# iterate across each row
	for x in range(src.size[0]-slice_width):
		first_pixel = (y * src.size[0]) + x
		pixel_slice = src_pixels[first_pixel:first_pixel + slice_width]
			# test if we're at a pink thing
		if pixel_slice == pattern:
			# store the (x,y) pink thing location
			pink_locations.append((x,y))
			break
	pixel_slice = src_pixels[y*src.size[0]:((y+1)*src.size[0])]
	for i in range(x):
		pixel_slice.append(pixel_slice[i])
	for i in range(x,len(pixel_slice)):
		data_list.append(pixel_slice[i])
			
	# save the output file
out.putdata(data_list)
out.save(out_path)
