#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Nov  3 11:50:18 2020

@author: enrico
"""

import matplotlib.pyplot as plt
from math import sqrt
from skimage import io
from skimage.feature import blob_log, blob_dog, blob_doh
#tutte le lib che servono

true_blob_im = io.imread('gray_blob.tif')#mi serve alla fine
#carico l'immagine come ndarray grigio
blob_im = io.imread('gray_blob.tif', as_gray=True)
inverse_blob = 1 - blob_im
#qui scambio i colori, per avere un'immagine nera con blob chiari

#non devo far altro che chiamare le funzioni, danno come risultato un ndarray
im_log = blob_log(inverse_blob, min_sigma=0.4, max_sigma=50, num_sigma=5, threshold=.5,
             overlap=1, log_scale=False, exclude_border=False)
im_log[:, 2] = im_log [:, 2] * sqrt(2)

im_dog = blob_dog(inverse_blob, min_sigma=0.3, max_sigma=50, sigma_ratio=1.6, threshold=.1,
                  overlap=.5, exclude_border=False)
im_dog[:, 2] = im_dog[:, 2] * sqrt(2)

im_doh = blob_doh(inverse_blob, min_sigma=0.1, max_sigma=60, num_sigma=5, threshold=0.001,
             overlap=.1, log_scale=False)


#questo l'ho copiato dalla pagina della libreria e modificato un pochino
#purtroppo questa parte non mi è chiara sintatticamente e da solo non riesco a fare qualcosa di simile
blobs_list = [im_log, im_dog, im_doh]
titles = ['Laplacian of Gaussian', 'Difference of Gaussian',
          'Determinant of Hessian']
sequence = zip(blobs_list, titles)

fig, axes = plt.subplots(1, 3, figsize=(9, 3), sharex=True, sharey=True)
ax = axes.ravel()

for idx, (blobs, title) in enumerate(sequence):
    ax[idx].set_title(title)
    ax[idx].imshow(true_blob_im)
    for blob in blobs:
        y, x, r = blob
        c = plt.Circle((x, y), r, color='red', linewidth=1, fill=False)
        ax[idx].add_patch(c)
    ax[idx].set_axis_off()

plt.tight_layout()
plt.show()