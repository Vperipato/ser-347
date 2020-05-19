# -*- coding: utf-8 -*-
"""
Created on Fri May  8 10:45:02 2020

@author: perip
"""

import numpy as np

#Dadas as seguintes séries temporais
s1 = np.array((168, 398, 451, 337, 186, 232, 262, 349, 189, 204, 220, 220, 207, 239, 259, 258, 242, 331, 251, 323, 106, 1055, 170))
s2 = np.array((168, 400, 451, 300, 186, 200, 262, 349, 189, 204, 220, 220, 207, 239, 259, 258, 242, 331, 251, 180, 106, 1055, 200))

#calcular a distância euclidiana entre as séries
dist = np.linalg.norm(s1-s2)
print("Distância euclidiana entre S1 e S2 : ", dist)

#calcular a série temporal com os valores médios entre s1 e s2
medi = ((s1 + s2) / 2)
print("Vals. Média: ", medi)

#calcular a série temporal com os valores máximos de cada instante entre s1 e s2
maxi = np.maximum(s1, s2)
print("Vals. Máx: ", maxi)

#calcular a série temporal com os valores mínimos de cada instante entre s1 e s2
mini = np.minimum(s1, s2)
print("Vals. Min: ", mini)