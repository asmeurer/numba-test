from matplotlib import pyplot as plt

from skimage import data
from skimage.feature import corner_harris, corner_subpix, corner_peaks
from skimage.transform import warp, AffineTransform
from skimage.draw import ellipse

from numba import jit, autojit, typeof
import time

import sys

arg1 = sys.argv[1]

if int(arg1):
    print "using autojit"

autojit = autojit if int(arg1) else lambda: (lambda x: x)
jit = jit if int(arg1) else lambda x: (lambda x: x)

print autojit

print "generating checkerboard"
t = time.time()
tform = AffineTransform(scale=(1.3, 1.1), rotation=1, shear=0.7,
                            translation=(210, 50))
image = warp(data.checkerboard(), tform.inverse, output_shape=(5000, 5000))
# rr, cc = ellipse(310, 175, 100, 100)
#
# image[rr, cc] = 1
print "took", time.time() - t

print "generating squares"

@jit('void()')
def generate_squares_niave():
    for i in range(0, 5*50, 50):
        for j in range(180 + i, 230 + i):
            for k in range(10 + i, 60 + i):
                image[j, k] = 1
        for j in range(230 + i, 280 + i):
            for k in range(60 + i, 110 + i):
                image[j, k] = 1


def generate_squares():
    for i in range(0, 5*50, 50):
        image[180 + i:230 + i, 10 + i:60 + i] = 1
        image[230 + i:280 + i, 60 + i:110 + i] = 1

t = time.time()

if int(arg1) > 1:
    generate_squares()
else:
    generate_squares_niave()

print "took", time.time() - t

print "finding corners"
t = time.time()
coords = corner_peaks(corner_harris(image), min_distance=5)
print "took", time.time() - t

print "getting subpix"
t = time.time()

coords_subpix = corner_subpix(image, coords, 13, 0.99)

print "took", time.time() - t

print "plotting"
plt.gray()
plt.imshow(image, interpolation='nearest')
plt.plot(coords[:, 1], coords[:, 0], '.b', markersize=3)
plt.plot(coords_subpix[:, 1], coords_subpix[:, 0], '+r', markersize=15)
plt.axis((0, 500, 500, 0))
plt.show()
