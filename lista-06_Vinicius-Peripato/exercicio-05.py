# -*- coding: utf-8 -*-
"""
Created on Fri May  8 12:36:12 2020

@author: perip
"""

import numpy as np
import matplotlib.pyplot as plt

estados = np.array(('AC', 'AL', 'AP', 'AM', 'BA', 'CE', 'DF', 'ES', 'GO', 'MA', 'MT', 'MS', 'MG', 'PA', 'PB', 'PR', 'PE', 'PI', 'RJ', 'RN', 'RS', 'RO', 'RR', 'SC', 'SP', 'SE', 'TO'))
#n_focos = np.array((65521, 8326, 17823, 210421, 157347, 72016, 3760, 11089, 182300, 365697, 706313, 254592, 182620, 603590, 23000, 44547, 18094, 233426, 12620, 13098, 35023, 245042, 163234, 19859, 54970, 2953, 330081))
n_focos = np.array((1.62, 0.21, 0.44, 5.21, 3.90, 1.78, 0.09, 0.27, 4.52, 9.06, 17.49, 6.31, 4.52, 14.95, 0.57, 1.10, 0.45, 5.78, 0.31, 0.32, 0.87, 6.07, 4.04, 0.49, 1.36, 0.07, 8.18))

explode = np.repeat(0.1, len(estados))

plt.pie(n_focos, labels=estados, autopct='%1.0f%%', explode=explode, pctdistance=0.9, labeldistance=1)
plt.title("Proporção de focos de incêndio\nno Brasil (2019) - 4.037.362 focos", fontsize=24)
plt.show()