import matplotlib.pyplot as plt
import matplotlib.image as mpimg
from PIL import Image
import numpy as np

ghost = np.array(Image.open('../src/ghost.png'))
theo = np.array(Image.open('theo.png'))

def resizeColor(image):
    image2= np.empty([image.shape[0],image.shape[1],3],dtype=int)
    for i in range(0,image.shape[0],1):
        for j in range (0,image.shape[1],1):
            image2[i][j][0] = image[i][j][0]
            image2[i][j][1] = image[i][j][1]
            image2[i][j][2] = image[i][j][2]
    return image2

def test(image,hauteur):
    height = image.shape[0]//hauteur
    ratio = (image.shape[0]//hauteur)
    largeur = int(image.shape[1]//ratio)
    width = image.shape[1]//largeur
    im = np.empty([hauteur,largeur,3], dtype=int)
    for i in range(0,hauteur,1):
        for j in range (0,largeur,1):
            avg = [0,0,0]
            for k in range(height*i,height*(i+1),1):
                for l in range(width*j,width*(j+1),1):
                    # print('k,l',k,',',l)
                    avg[0] += image[k][l][0]
                    avg[1] += image[k][l][1]
                    avg[2] += image[k][l][2]
            avg[0]=avg[0]//(height*width)
            avg[1]=avg[1]//(height*width)
            avg[2]=avg[2]//(height*width)
            im[i][j] = avg
    return im

image = test(ghost,50)
print(image)
plt.imshow(image)
plt.show()


