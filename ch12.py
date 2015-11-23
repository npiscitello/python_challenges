file_path = 'evil2.gfx'

data = []
images = {}
number = 5
file_handle = open(file_path, 'rb')
gfx = file_handle.read()

for i in range(number):
	images[i]=(open('image'+str(i)+'.jpg', 'wb'))


for j in range(0,len(gfx)):
	data.append(gfx[j])
	images[j%number].write(gfx[j])

file_handle.close()

for i in range(number):
	images[i].close()
