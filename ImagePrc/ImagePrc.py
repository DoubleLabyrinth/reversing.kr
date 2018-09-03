#!/usr/bin/env python3

import numpy as np
import matplotlib.pyplot as plt

imgData = np.fromfile('image.raw', dtype = np.uint8)
imgData = imgData.reshape([150, 200, 3])
plt.imshow(imgData, origin = 'lower')
plt.show()
