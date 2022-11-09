
import os
from re import X
from config_ag import *
from V_input import *
import random, copy, os
from function import *
import plotly.express as px
import pandas as pd


class Tache:
    def __init__(self, lstpt, num=0,lscout=0,ress="h"):
        self.num = num
        self.lstpt = lstpt
        self.lscout = lscout
        # ressources
        self.ress=ress
        self.indress=0
        self.pt = 0
        self.cj = 0
        self.cout=0
        self.cf_t=0

    def update(self):
            ind=list_ress.index(self.ress)
            self.pt = self.lstpt[ind]
            self.indress=ind
            self.cout = self.lscout[ind]
            self.cf_t= list_cf_t[self.num]

class Cromosome:
    def __init__(self):
        self.tabcj = []
        self.n_tch = n_tch
        self.lstch = []
        self.l = []
        self.l2 = []
        self.somcj = 0
        self.cout = 0
        self.fat=0
        self.fo = 0

        self.get_new_cromosome()

    def list_fo(self):
        l=[]
        l.append(self.somcj)
        l.append(self.cout)
        l.append(self.fat)
        # l.append(self.fo)
        return l

    def get_list_r(self):
        l = []
        for t in self.lstch:
            l.append(t.ress)
        return l

    def get_list_t(self):
        self.l = []
        for t in self.lstch:
            self.l.append(t.num)
        return self.l
    
    def get_list_t2(self):
        self.get_list_t()
        self.l2 = []
        i=0
        for t in self.lstch:
            self.l2.append([self.l[i],t.ress])
            i=i+1
        return self.l2

    def update(self):
        for t in self.lstch:
            t.update

        self.tabcj = []
        self.somcj = self.calc_somcj()
        self.cout = self.calc_cout()
        self.fat =self.calc_fatigue()

        # La fonction Somme pondérée se calcule dans la population nous aurons besoin de max et min des fonctions objectif 
        self.fo = 0

    def get_new_cromosome(self):
        self.lstch = []
        for ind_tache in range(n_tch):
            lstpt=[]
            for pt in list_pt:
                lstpt.append(pt[ind_tache])
            lscout=[]
            for cout in list_cout:
                lscout.append(cout[ind_tache])
            ress=random.choice(list_ress)
            tache = Tache(lstpt,ind_tache,lscout=lscout,ress=ress)
            tache.num = ind_tache 
            self.lstch.append(tache)
        random.shuffle(self.lstch)
        self.update

    def correction_crom(self):
        l = self.get_list_t()
        for seqq in sec_in:
            for seq in sec_in:
                val = seq[0]
                prec = seq[1]
                a=l.index(val)
                b=l.index(prec)
                if a < b:
                    v=l[a]
                    l[a]=l[b]
                    l[b]=v
        
        ltcsm=self.lstch
        ltcsm2=[]
        for i in l:
            for tch in ltcsm:
                if tch.num==i:
                    ltcsm2.append(tch)
        self.lstch=ltcsm2
        self.update

    def repetition(self):
        l = self.get_list_t()
        if len(l) == len(set(l)):
            return True
        else:
            return False
            
    def contrainte_prec(self):
        l = self.get_list_t()
        # print(l)
        bien = True
        for seq in sec_in:
            val = seq[0]
            prec = seq[1]
            a=l.index(val)
            b=l.index(prec)
            if a < b:
                bien = False
        return bien
    
    def tout_contrainte(self):
        a = self.repetition()
        b = self.contrainte_prec()
        # a = True
        # d = False
        # e = False
        tout = a and b
        return tout

    def calc_cj_tach(self):
        ds=[]
        for i in range(2):
            ds.append(0)
        for tache in self.lstch:
            tache.update()
            indress=tache.indress
            if indress !=2 :
                cj=ds[indress]+tache.pt
                ds[indress]=cj
            else:
                ma=max(ds)
                ma=ma+tache.pt
                for i in range(2):
                    ds[i]=ma
                cj=ma
            tache.cj = cj
            self.tabcj.append(cj)
            
    def calc_somcj(self):
        self.calc_cj_tach()
        s = 0
        for tache in self.lstch:
            s = s + tache.cj
        return s

    def calc_cout(self):
        s = 0
        for tache in self.lstch:
            s = s + tache.cout
        return s    

    def calc_fatigue(self):
        self.calc_cj_tach()
        somfat = 0
        temp_fx_tch=0
        
        for tache in self.lstch:
            cj=tache.cj 
            pt=tache.pt
            num=tache.num
            if tache.ress in['h' ,'hr'] :
                temp_dn_tch = cj - pt
                delta=temp_dn_tch-temp_fx_tch
                val_fat=pt*list_cf_t[num]
                val_rop=delta*cr_op
                somfat = somfat + val_fat - val_rop
                temp_fx_tch=cj 

        d_tch=self.lstch[-1]

        if d_tch.ress not in ['h' ,'hr'] :
            temp_dn_tch = cj - pt
            delta=temp_dn_tch-temp_fx_tch
            val_rop=delta*cr_op
            somfat = somfat - val_rop
        return somfat

    def print_crom(self):
        print( " Somme Cj : ", self.somcj, " / Somme coût : ", self.cout," /Solution : ", self.get_list_t2())
        # " FOp : ", round(self.fo,2), , "Niveau fatigue: ",self.fat

    def planning(self, itération=''):
        self.update()
        plt=[]
        for tache in self.lstch:
            v_cj=tache.cj
            v_pt=tache.pt
            v_num=tache.num
            v_ress=tache.ress
            Tâches="Tâche: "+str(v_num+1)
            Début=v_cj-v_pt
            Fin =v_cj
            color22=str(v_num)
            
            if v_ress =="hr":
                Ressource="h"
                plt.append(dict(Tâches=Tâches, Début=Début, Fin= Fin, Ressource=Ressource, Aj=Début,Pt=v_pt,Cj=Fin,Time=v_pt))
                
                Ressource="r"
                plt.append(dict(Tâches=Tâches, Début=Début, Fin= Fin, Ressource=Ressource, Aj=Début,Pt=v_pt,Cj=Fin,Time=v_pt))
            else:
            # if 1:    
                Ressource=v_ress
                plt.append(dict(Tâches=Tâches , Début=Début, Fin= Fin, Ressource=Ressource, Aj=Début,Pt=v_pt,Cj=Fin,Time=v_pt))


        df = pd.DataFrame(plt)
        fo='  '
        fo+=" La somme Cj : "+str(self.somcj) 
        fo+="  / Le coût : "+str(round(self.cout,2)) 
        # fo+="  / La fatigue accumélée : "+str(round(self.fat,2)) 
        # fo+="  La moyenne pondérée: "+str(self.fo)
        print(df)

        title="***   ***              Le planning d'ordonnancement d'une solution de la population "+itération+"  -  "+fo+"  -    ***   *** "
        fig = px.bar(df,base = "Aj",x = "Time",y = "Ressource", text="Tâches",color = "Tâches", orientation = 'h', title=title)
        fig.update_yaxes(autorange="reversed")
        fig.show()         

class population:
    def __init__(self):
        self.get_initial_population()
       
    def get_initial_population(self):
        self.tab_crom = []
        for ind_crom in range(tdp):
            crom = Cromosome()
            crom.update()
            self.tab_crom.append(crom)
            crom = copy.deepcopy(crom)
        self.update()
        
    def update(self):
        for crom in self.tab_crom:
            crom.update()
        # self.calc_mp()

    def calc_mp(self):
        lcj=[]
        lcou=[]
        lfat=[]
        for crom in self.tab_crom:
            lcj.append(crom.somcj)
            lcou.append(crom.cout)
            lfat.append(crom.calc_fatigue)

        maxcj=max(lcj)
        mincj=min(lcj)

        maxcout=max(lcou)
        mincout=min(lcou)

        maxf=max(lfat)
        minf=min(lfat)

        for crom in self.tab_crom:
            if maxcj-mincj !=0:
                xcj=(crom.somcj-mincj)/(maxcj-mincj)
            else:
                xcj=0
            if maxcout-mincout !=0 :
                xcout=(crom.cout-mincout)/(maxcout-mincout)
            else:
                xcout=0
            if maxf-minf !=0 :
                xf=(crom.fat-minf)/(maxf-minf)
            else:
                xf=0
            # crom.fo=W1*xcj+W2*xcout
            crom.fo=W1*xcj+W2*xcout+W3*xf

    def print_fo(self):
        l = []
        for crom in self.tab_crom:
            l.append(crom.list_fo())
        return l

    def print_croms_pop(self):
        ind = 0
        for crom in self.tab_crom:
            print(ind, " fmp : ", round(crom.fo,2), " Somme cj : ", crom.somcj, " /Somme coût : ", crom.cout, " /Solution : ", crom.get_list_t2())
            # "Niveau fatigue: ",self.fat,
            ind += 1
    def print_front(self,itération='ff'):
        
        l_fo=[]
        for rec in self.tab_crom:
            l=rec.list_fo()
            l_fo.append(l)
        clas_self=index_nds(l_fo)
        print(clas_self)
        i=0
        f="f"
        lf =[]
        lx =[]
        ly =[]
        lz =[]
        lnum =[]
        plt=[]
        for j in clas_self[0]:

            if f != clas_self[1][i]:
                f=clas_self[1][i]
                print('-------    front : ',f,"  : -----")
            print('               crm [ ',j,' ] : ',l_fo[j])
            i+=1
            lf.append(f)
            lx.append(l_fo[j][0])
            ly.append(l_fo[j][1])
            lz.append(l_fo[j][1])
            lnum.append(j)
        j=0
        max_x=max(lx)
        max_y=max(ly)
        max_z=max(lz)
        min_x=min(lx)
        min_y=min(ly)
        min_z=min(lz)
        for i in lf:
            x=(lx[j]-min_x)/(max_x-min_x)
            y=(ly[j]-min_y)/(max_y-min_y)
            z=(lz[j]-min_z)/(max_z-min_z)
            
            num=str(lnum[j]+1)
            plt.append(dict(front=str(i), x=x, y= y,z=z,text=num))
            j=j+1

        
        
        df = pd.DataFrame(plt)
        title="                         Les fronts de Pareto de la population "+itération+ ":"
        fig = px.scatter(df, x="x", y="y", color="front",title=title)
        fig = px.line(df, x="x", y="y", color="front",markers=True,title=title)

        
        fig.show()

        # l=[]
        # for i in clas_self[0]:
        #     val=self.tab_crom[i]
        #     l.append(val)
        # self.tab_crom=copy.deepcopy(l)
        # return self
        pass


    def print_front3d(self,text='ff'):
        
        l_fo=[]
        for rec in self.tab_crom:
            l=rec.list_fo()
            l_fo.append(l)
        clas_self=index_nds(l_fo)
        print(clas_self)
        i=0
        f="f"
        lf =[]
        lx =[]
        ly =[]
        lz =[]
        lnum =[]
        plt=[]
        for j in clas_self[0]:

            if f != clas_self[1][i]:
                f=clas_self[1][i]
                print('-------    front : ',f,"  : -----")
            print('               crm [ ',j,' ] : ',l_fo[j])
            i+=1
            lf.append(f)
            lx.append(l_fo[j][0])
            ly.append(l_fo[j][1])
            lz.append(l_fo[j][1])
            lnum.append(j)
        j=0
        max_x=max(lx)
        max_y=max(ly)
        max_z=max(lz)
        min_x=min(lx)
        min_y=min(ly)
        min_z=min(lz)
        for i in lf:
            x=(lx[j]-min_x)/(max_x-min_x)
            y=(ly[j]-min_y)/(max_y-min_y)
            z=(lz[j]-min_z)/(max_z-min_z)
            
            num=str(lnum[j]+1)
            plt.append(dict(front=str(i), x=x, y= y,z=z,text=num))
            j=j+1

        
        
        df = pd.DataFrame(plt)
        # fig = px.scatter(df, x="x", y="y", color="front")
        fig = px.scatter_3d(df, x="x", y="y", z="z", color="front",text="text")
        
        # fig = px.line(df, x="x", y="y", color="front",markers=True,text="text")

        
        fig.show()

        # l=[]
        # for i in clas_self[0]:
        #     val=self.tab_crom[i]
        #     l.append(val)
        # self.tab_crom=copy.deepcopy(l)
        # return self
        pass



    