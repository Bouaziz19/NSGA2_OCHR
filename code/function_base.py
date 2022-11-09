from ast import Pass
import numpy as np
from nds import ndomsort
import matplotlib.pyplot as plt
from config_ag import *
from V_input import *
from model import *

# Génération de la population initiale
def gen_po0():
    po=population()
    return po

def get_new_population(pop):
    # pop=verification(pop)
    # pop.print_front()
    pop=classementnds(pop)
    N_pop=selection(pop)
    N_pop=croisement(pop,N_pop)
    N_pop=mutation(N_pop)
    N_pop=verification(N_pop)
    N_pop=regroup_pq(pop,N_pop)
    N_pop=classementnds(N_pop)
    N_pop=selection2(N_pop)
    return N_pop

def classementnds(pop):
    pop=verification(pop)
    l_fo=[]
    for crom in pop.tab_crom:
        l=crom.list_fo()
        l_fo.append(l)
    clas_pop=index_nds(l_fo)
    l=[]
    for i in clas_pop[0]:
        val=pop.tab_crom[i]
        l.append(val)
    pass

    pop.tab_crom=copy.deepcopy(l)
    # pop.print_crom()
    return pop

def selection(pop):
    N_pop=population()
    tab_crom=pop.tab_crom
    N_pop.tab_crom=[]
    for crom in tab_crom[0:psel]:
        N_pop.tab_crom.append(crom)
    return N_pop

def croisement(pop,N_pop):
    tab_crom=pop.tab_crom
    x_rg1_tab = tab_crom[0:pcr1]
    x_rg2_tab = tab_crom[pcr1:pcr2]
    tp=tdp-psel
    tp2=1+int((tdp-psel)/2)
    j=0
    for i in range(tp2):
        c1 = copy.deepcopy( random.choice(x_rg1_tab))
        c2 = copy.deepcopy( random.choice(x_rg2_tab))
        l1=c1.lstch
        l2=c2.lstch
        l1,l2=mix2list(l1,l2)
        c1.lstch=l1
        c2.lstch=l2
        if j<tp:
            N_pop.tab_crom.append(c1)
            j+=1
        if j<tp:
            N_pop.tab_crom.append(c2)
            j+=1
    N_pop.update()
    return N_pop

def mutation(N_pop):
    l=list(range(tdp))
    for i in range(pmu):
        #Indice de cromosome séléctionné pour la mutation 
        icsm = random.choice(l)
        # icsm !=0  pour garder la meilleure solution 
        if icsm !=0 :
            csm=N_pop.tab_crom[icsm]
            ltcsm=csm.lstch

            rind1=randint(0,n_tch-1)
            rind2 =randint(0,n_tch-1)

            a=ltcsm[rind1]
            ltcsm[rind1]=ltcsm[rind2]
            ltcsm[rind2]=a

            csm.lstch=ltcsm
            N_pop.tab_crom[icsm]=csm
    return N_pop

def verification(N_pop):
    for i in range(tdp):
        fin=False  
        while fin==False :
            fin=N_pop.tab_crom[i].tout_contrainte()
            if fin==False:
                # N_pop.tab_crom[i].correction_reg_crom()
                N_pop.tab_crom[i].correction_crom()

                
            else:
                # print(N_pop.tab_crom[i].get_list_t())
                pass
            # fin=N_pop.tab_crom[i].tout_contrainte()
                #N_pop.tab_crom[i].correction_crom_mut()
        fin=False  
   
    # N_pop.update()
    return N_pop

def regroup_pq(pop,N_pop):
    for crom in pop.tab_crom:
        N_pop.tab_crom.append(crom)
    N_pop.update()
    return N_pop

def selection2(N_pop):
    N_pop.tab_crom=N_pop.tab_crom[0:tdp]
    N_pop.update()
    return N_pop
















