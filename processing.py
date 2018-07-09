import os
import time

import numpy
from scipy import misc
from skimage import io, filters
from skimage import transform

train_size = 12

start_time = time.time()

data_files = os.listdir('data')
for i in range(1, train_size):
    file = data_files[i]
    buf = './data/{}'.format(file)
    buf1 = './processed_data/{}'.format(file)
    image = io.imread(buf)
    image = numpy.invert(image)
    #image = filters.gaussian(image, 5)
    misc.imsave(buf1, image)

print("Time taken:", time.time() - start_time)
