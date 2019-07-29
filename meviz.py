

#castlevania
import numpy as np
from skimage import io
from PIL import Image




def normalizer(img_array, max_val):
	return img_array*255/max_val

direc = '/media/fabricio/SANDISK/ts1-projections/'
savedir = '/media/fabricio/SANDISK/ts1-projections/combined/'

try:
	tif_stack_e1 = io.imread(direc+'/Al.tif')
	tif_stack_e2 = io.imread(direc+'/Co.tif')
	tif_stack_e3 = io.imread(direc+'/Mn.tif')
except:
	print("no valid directory")

#makes sure all 3 tiff stacks are of the same depth
depth1 = tif_stack_e1.shape[0]
depth2 = tif_stack_e2.shape[0]
depth3 = tif_stack_e3.shape[0]

if (depth1 ==depth2) and (depth2 == depth3):
	depth = depth1
else:
	print('tiff stacks do not have the same depth')

max_1 = tif_stack_e1.max()
max_2 = tif_stack_e2.max()
max_3 = tif_stack_e3.max()
max_val = max_1

if max_2 > max_1:
	max_val = max_2
if max_3 > max_val:
	max_val = max_3

width = tif_stack_e1.shape[1]
height = tif_stack_e1.shape[2]

for i in range(depth):
	rgbArray = np.zeros((width,height,3), 'uint8')

	red = normalizer(tif_stack_e1[i], max_val)*400
	green = normalizer(tif_stack_e2[i], max_val)*1
	blue = normalizer(tif_stack_e3[i], max_val)*2
	print(tif_stack_e1[i].max(),tif_stack_e2[i].max(),tif_stack_e3[i].max())

	rgbArray[:,:,0] = red
	rgbArray[:,:,1] = green
	rgbArray[:,:,2] = blue

	img = Image.fromarray(rgbArray)
	# img.show()
	# savedir = '/home/fabricio/Desktop/combined/'
	img.save(savedir+'AlCoMn_combined_{}.jpeg'.format(i))






# for i in range(3):

	#remove NAN 

	#get min of each stack
	#get max of each stack
	#get avg of each stack

	#if max of one set greater than the smallest max by more than 5x, thorw warning
		#maybe normalize to all elemns


	#convert to rgba
		#set one stack = to red channel
		#set one stack = to green channel
		#set one stack = to blue channel




# r, g, and b are 512x512 float arrays with values >= 0 and < 1.
# import numpy as np
# rgbArray = np.zeros((512,512,3), 'uint8')
# rgbArray[..., 0] = r*256
# rgbArray[..., 1] = g*256
# rgbArray[..., 2] = b*256
# img = Image.fromarray(rgbArray)
# img.save('myimg.jpeg')
