#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Oct 22 16:56:26 2020

@author: enrico
"""
#import os
import matplotlib.pyplot as plt
from math import sqrt
from skimage import io
from skimage.feature import blob_log, blob_dog, blob_doh
import numpy as np
#from skimage.color import rgb2gray
#tutte le lib che servono

#carico l'immagine come ndarray grigio
#per evitare crash ho isolato una zona piccola
#l'idea è fare un loop su tutta l'immagine divisa in settori
blob_im = io.imread('gray_blob.tif', as_gray=True)[:600, :600]
#io.imshow(blob_im)

#non devo far altro che chiamare le funzioni, danno come risultato un ndarray
#per log e dog bisogna modificare il raggio secondo la teoria
#ma non capisco la sintassi
im_log = blob_log(blob_im, min_sigma=.5, threshold=.1, overlap=.7)
im_log[:, 2] = im_log [:, 2] * sqrt(2)

im_dog = blob_dog(blob_im, min_sigma=.1, threshold=.1, overlap=.2)
im_dog[:, 2] = im_dog[:, 2] * sqrt(2)

im_doh = blob_doh(blob_im, min_sigma=0.1)

#da questo punto in poi l'esempio mi diventa non chiaro
#faccio di testa mia
#ho una Figure con 0 Axes
fig, axes = plt.subplots(1, 3, figsize=(9, 3), sharex=True, sharey=True)
ax = axes.imshow(blob_im)