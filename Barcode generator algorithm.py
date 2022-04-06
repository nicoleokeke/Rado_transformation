import matplotlib.pyplot as plt
import cv2
import os
import imagehash
import numpy as np
from skimage.data import shepp_logan_phantom
from skimage.transform import radon, rescale
images = []
def load_images_from_folder(folder):
    folder = '//folder directory '
    
    for zero in os.listdir(folder):
        img = cv2.imread(os.path.join(folder, zero,cv2.cvtCOLOR_BGR2GRAY))
        gray = np.sqrt((img*img).sum(-1))
        if img is not None:
            images.append(img)
            return images
        
        print (images)
    arr = np.array(images)
    print (arr)
    p1 = radon(images, theta1=0)
    p2 = radon(images, theta2= 45)
    p3 = radon(images, theta3= 90)
    p4 = radon(images, theta4= 135)
    i1 = np.mean(p1)
    i2 = np.mean(p2)
    i3 = np.mean(p3)
    i4 = np.mean(p4)
def threshold():
  barcode_gen = c1+c2+c3+c4
     
  for images in zero:
    c1 = i1 > np.all(p1)
    
    if i1 > np.all(p1):
     return 1
    else:
     return 0
    return c1
    
    for images in zero:
        c2 = i2 > np.all(p2)
    if i2 > np.all(p2):
     return 1
    else:
     return 0
    return c2
    
    for images in zero:
        c3 = i3 > np.all(p3)
    if i3 > np.all(p3):
     return 1
    else:
     return 0
    return c3
    
    for images in zero:
        c4= i4 > np.all(p4)
    if i4 > np.all(p4):
     return 1
    else:
     return 0
    return c4
   
    
    print (barcode_gen)
    
    
    for images in zero:
        for i in range (0, 10):
         hamming_thresh = 0.0
    def hamming (img[i], img[i++]):
        assert len(img[i]) == len(img[i++])
        image1hash = imagehash.whash(img[i])
        image2hash = imagehash.whash(img[i++])
        
        similarities = image1hash - image2hash
        print (similarities)
   
    return similarities
i++
else:
    print(no similarity)
def unvectorized_hitrate(iamges, true_labels)
        pred_images = []
        for images in zero:
            if pred_images.append(np.argmax(row)):
                
                num_correct = 0 
                for i in range (len(pred_images)):
                    if pred_images[i] == true_images[i]:
                        num_coreect += 1
                        
                        return num_correct / len(true_labels)
                    %%timeit
                    unvectorized_hitrate(images, hamming_thresh)