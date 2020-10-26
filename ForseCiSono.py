#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Oct 26 11:55:40 2020

@author: enrico
"""
import matplotlib#serve questa libreria
import matplotlib.pyplot as plt
from skimage import io

figure, ax = plt.subplots()
#ho Figure e Axes, questa istanza è vuota ma posso "inserire un elemento"
#creato da me a parte senza passare attraverso i metodi della classe Axes
#ad esempio usando i metodi della classe Rectangle, creo un rettangolo
rect = matplotlib.patches.Rectangle((1, 1), width=15, height=12, color='green')
#ora esiste come oggetto a sé stante, lo inserisco in ax con un helper method
#ax1 = figure.add_axes([1, 0.4, 0.3, 1])
#ax1.add_patch(rect)
im = io.imread('Prova.jpeg')
car =  ax.imshow(im)
ax.add_patch(rect)

#for label in ax.get_xticklabels():
#   label.set_color('orange')