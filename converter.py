import matplotlib.pyplot as plt
import numpy as np
import cv2
messi = plt.imread('/home/phonegawd/Desktop/2ASCII/messi.jpg')


def imageASCII(messi):
    messi = np.array(messi)
    messi = np.mean(messi, axis=2)
    h, w = messi.shape
    asciiARR = 'N@#W$9876543210?!abc;:+=-,._'[::-1]
    # messi = messi.astype(int)
    messi = cv2.resize(messi, dsize=(w//8, w//8),
                       interpolation=cv2.INTER_NEAREST)
    messi = messi.astype(int)
    h, w = messi.shape
    asciiSize = len(asciiARR) - 1
    messi = messi // (asciiSize)
    messiAscii = [['' for j in range(w)] for i in range(h)]
    txt = ''
    for i in range(h):
        for j in range(w):
            messiAscii[i][j] = asciiARR[messi[i][j]]
        txt += (''.join(messiAscii[i])) + '\n'
    return txt


# print(imageASCII(messi))
# print(messiAscii)
# plt.imshow(messi, cmap='gray')
# plt.show()
