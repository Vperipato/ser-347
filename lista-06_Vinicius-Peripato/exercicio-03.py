# -*- coding: utf-8 -*-
"""
Created on Fri May  8 11:52:10 2020

@author: perip
"""

import numpy as np
import matplotlib.pyplot as plt

#Construa um gráfico de barras horizontal com os dados da distribuição da população masculina.
grupos = np.array(('0-4', '5-9', '10-14', '15-19', '20-24', '25-29', '30-34', '35-39', '40-44', '45-49', '50-54', '55-59', '60-64', '65-69', '70-74', '75-79', '80-84', '85-89', '90-94', '95-99', '100+'))
masculino = np.array((7016987, 7624144, 8725413, 8558868, 8630229, 8460995, 7717658, 6766664, 6320568, 5692014, 4834995, 3902344, 3041035, 2224065, 1667372, 1090517, 668623, 310759, 114964, 31529, 7247))
feminino = np.array((6779171, 7345231, 8441348, 8432004, 8614963, 8643419, 8026854, 7121915, 6688796, 6141338, 5305407, 4373877, 3468085, 2616745, 2074264, 1472930, 998349, 508724, 211594, 66806, 16989))


plt.figure(figsize=(6,5))
plt.barh(grupos, masculino, color='lightblue')
plt.xlabel("População", fontsize=16)
plt.ylabel("Grupos de idade", fontsize=16)
plt.title("Distribuição da população masculina (2010)", fontsize=24)
ax = plt.gca()
ax.get_xaxis().set_major_formatter(plt.FuncFormatter(lambda x, loc: "{:,}".format(int(x))))
plt.show()


