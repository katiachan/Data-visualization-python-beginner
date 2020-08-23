# -*- coding: utf-8 -*-
"""Pendule graphe 2

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1aUGnq0tik1NzkS2DTOlbxodLdOguhjZr
"""

import matplotlib.pyplot as plt

k = [5.89, 21.25, 31.05, 59.83,	64.22,	103.4,	138.2,	166.8,	192.9,	234.1,	259.8]
f1 = [0.346,	0.341,	0.346,	0.338,	0.346,	0.345,	0.342,	0.345,	0.346,	0.343,	0.348]
f2 = [0.349,	0.356,	0.368,	0.381,	0.419,	0.424,	0.452,	0.482,	0.51,	0.554,	0.591]
y = [0.343,	0.347,	0.3,	0.343]
z = [0.411,	0.448,	0.432,	0.531]
k2 = [90,	127,	180,	215]

plt.plot(k,f1)
plt.plot(k,f2)
plt.scatter(k2, y)
plt.scatter(k2, z)
plt.xlabel("K (10^(-3))")
plt.ylabel("F^2 (s^(-2))")
plt.legend(["F1^2", "F2^2", "F1^2 *", "F2^2 *"])
plt.grid(True)
plt.show()

