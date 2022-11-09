
from V_input import *


# Les paramètres de Notre Algorithme génétic
# type_classement =1

# Le nombre des itérations
n_it = 30
 
# La taille de la population
tdp = 100

# Probabilité de selection 
psel =0.2

# Probabilités de croisement
pcr1 = 0.2
pcr2 = 0.5
# Le point de croisement
ptcr = 0.5

# La probabilité de mutaion 
pmu = 0.1

psel=int( psel * tdp)
pcr1=int( pcr1 * tdp)
pcr2=int( pcr2 * tdp)
ptcr=int( ptcr * n_tch)
pmu=int( pmu * tdp)

#Les poids de la fonction pondérée 
W1= 1
W2= 1
W3= 1