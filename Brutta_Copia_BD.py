#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Oct 22 16:56:26 2020

@author: enrico
"""
#import os
#import matplotlib
import matplotlib.pyplot as plt
from math import sqrt
from skimage import io
from skimage.feature import blob_log, blob_dog, blob_doh
#import numpy as np
#from skimage.color import rgb2gray
#tutte le lib che servono

true_blob_im = io.imread('gray_blob.tif')#mi serve alla fine
#carico l'immagine come ndarray grigio
#per evitare crash ho isolato una zona piccola
#l'idea è fare un loop su tutta l'immagine divisa in settori
blob_im = io.imread('gray_blob.tif', as_gray=True)
inverse_blob = 1 - blob_im
#io.imshow(inverse_blob)

#non devo far altro che chiamare le funzioni, danno come risultato un ndarray
#per log e dog bisogna modificare il raggio secondo la teoria
#ma non capisco la sintassi
im_log = blob_log(inverse_blob, min_sigma=0.4, max_sigma=50, num_sigma=5, threshold=.5,
             overlap=1, log_scale=False, exclude_border=False)
im_log[:, 2] = im_log [:, 2] * sqrt(2)

im_dog = blob_dog(inverse_blob, min_sigma=0.3, max_sigma=50, sigma_ratio=1.6, threshold=.1,
                  overlap=.5, exclude_border=False)
im_dog[:, 2] = im_dog[:, 2] * sqrt(2)

im_doh = blob_doh(inverse_blob, min_sigma=0.1, max_sigma=60, num_sigma=5, threshold=0.001,
             overlap=.1, log_scale=False)
#da questo punto in poi l'esempio mi diventa non chiaro
#faccio di testa mia, ma esce qualcosa di non bello visivamente
#ho una Figure con 0 Axes
figure, ax = plt.subplots()
blob = ax.imshow(true_blob_im)



#metodo blob_log
for elem in im_log:
    y_blob = elem[0]
    x_blob = elem[1]
    r_blob = elem[2]
    cerchio_log = plt.Circle((x_blob, y_blob), r_blob, color='red', linewidth=10, fill=False)
    ax.add_patch(cerchio_log)
 
#metodo blod_dog
for elem in im_dog:
    y_blob = elem[0]
    x_blob = elem[1]
    r_blob = elem[2]
    cerchio_dog = plt.Circle((x_blob, y_blob), r_blob, color='blue', linewidth=1, fill=False)
    ax.add_patch(cerchio_dog)
    
    
#questo segna in basso a destra un blob grande che in realtà non c'è
#indipendentemente dai parametri continua a dire che esiste
#non mi spiego il motivo    
#metodo blob_doh
for elem in im_doh:
    y_blob = elem[0]
    x_blob = elem[1]
    r_blob = elem[2]
    cerchio_doh = plt.Circle((x_blob, y_blob), r_blob, color='black', linewidth=1, fill=False)
    ax.add_patch(cerchio_doh)
    
plt.show()