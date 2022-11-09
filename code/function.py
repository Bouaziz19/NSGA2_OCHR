import numpy as np
from nds import ndomsort
import matplotlib.pyplot as plt
from config_ag import *
from V_input import *
from random import randint,shuffle


# Mixage 2 listes pour Le croisement
def mix2list(l1,l2):
    l30=l1[0:ptcr]
    l40=l2[0:ptcr]
    l31=[]
    l41=[]
    for i in range(ptcr):
        l31.append(l30[i].num)
        l41.append(l40[i].num)
    for rec in l2:
        if rec.num not in l31:
            l30.append(rec)
    for rec in l1:
        if rec.num not in l41:
            l40.append(rec)
    rnl=range(len(l1))
    lr1=[]
    lr2=[]
    for i in rnl:
        lr1.append(l1[i].ress)
        lr2.append(l2[i].ress)
    shuffle(lr1)
    shuffle(lr2)
    for i in rnl:
        l40[i].ress=lr1[i]
        l30[i].ress=lr2[i]
    return l30 , l40

# Supprimer les élements redondants 
def supp_red(list_vr):
    list_sr=[]
    for ele in list_vr:
        if ele not in list_sr:
            list_sr.append(ele)
    return list_sr

# Obtenir les indices de tout les cromosomes dans les  fronts 
def get_indexs(list_vr,list_sr):
    ind_in_list_vr=[]
    for i in list_sr:
        indices = []
        ind=0
        for  ele in list_vr:
            if ele == i:
                indices.append(ind)
            ind+=1
        ind_in_list_vr.append(indices)
    return [list_sr,ind_in_list_vr]

# Get index Non-dominated sorting
def index_nds(list_vr):
    if len(list_vr[0])==1:
        for i in range(len(list_vr)):
            list_vr[i].append(0)
    
    l_ind=[]
    l_front=[]
    list_sr=supp_red(list_vr)
    l_sr_ind=get_indexs(list_vr,list_sr)
    fronts = ndomsort.non_domin_sort(list_sr)
    for front in fronts:
        for l_fo in fronts[front]:
            ind=l_sr_ind[0].index(l_fo)
            for ind_crom in l_sr_ind[1][ind]:
                l_ind.append(ind_crom)
                l_front.append(front)
    return [l_ind,l_front]









#Les fonctions plot
    
ylinestyle=["-","-","-",":","-","--","-.",":","-","--","-.",":",]
ylabel=['fo1','fo2','fo3','fo4','fo5','fo6','fo7','fo8','fo9','fo10','fo11',]   
def plot_fo(l):
    for i in range(len(l)-1):
        x=l[0]
        y=l[i+1]
        label=ylabel[i]
        linestyle=ylinestyle[i]
        plt.plot(x,y,label = label,linestyle=linestyle)
    
    plt.legend()
    plt.show()

def plot_l_ins(pop):
    l=[[]]
    sol=pop.tab_crom[0]
    for i in range(len(sol.list_fo())):
        l.append([])
    return l

def plot_l_add(i,l,pop):
    sol=pop.tab_crom[0]
    l1=sol.list_fo()

    l1.insert(0, i)
    j=0
    for rec in l1:
        l[j].append(rec)
        j+=1
    return l

    


