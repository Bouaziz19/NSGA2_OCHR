import plotly.express as px
import plotly.express as px
df = px.data.iris()
fig = px.scatter(df, x="sepal_width", y="sepal_length", color="species",)
fig.show()


    # def lis_list(self, list_2, list_1):
    #     l = []
    #     for x in list_2:
    #         if x not in list_1:
    #             l.append(x)
    #     return l   
  
        # l=[]
        # for i in clas_self[0]:
        #     val=self.tab_crom[i]
        #     l.append(val)
        # self.tab_crom=copy.deepcopy(l)
        # return self
        # pass
# def correction_reg_crom(self):
#         random.shuffle(self.lstch)
#         self.update
# def correction_crom_mut(self):
#         ltcsm=self.lstch

#         rind1=randint(0,n_tch-1)
#         rind2 =randint(0,n_tch-1)

#         a=ltcsm[rind1]
#         ltcsm[rind1]=ltcsm[rind2]
#         ltcsm[rind2]=a

#         self.lstch=ltcsm
#         self.update


# def get_new_population_corr(pop):
#     pop=classementnds_corr(pop)
#     N_pop=selection(pop)
#     N_pop=croisement_corr(pop,N_pop)
#     N_pop=regroup_pq(pop,N_pop)
#     N_pop=classementnds(N_pop)
#     N_pop=selection2(N_pop)
#     return N_pop
    
# def classementnds_corr(pop):
#     l_fo=[]
#     for crom in pop.tab_crom:
#         l=crom.list_fo()
#         l_fo.append(l)
#     clas_pop=index_nds(l_fo)
#     l=[]
#     for i in clas_pop[0]:
#         val=pop.tab_crom[i]
#         l.append(val)
#     pop.tab_crom=copy.deepcopy(l)
#     # pop.print_crom()
#     return pop

# def croisement_corr(pop,N_pop):
#     tab_crom=pop.tab_crom
#     x_rg1_tab = tab_crom[0:pcr1]
#     x_rg2_tab = tab_crom[pcr1:pcr2 ]
#     tp=tdp-psel
#     po=population()
#     tab=po.tab_crom
#     # tp2=1+int((tdp-psel)/2)
#     # j=0
#     for i in range(tp):
#         c1 = copy.deepcopy( random.choice(x_rg1_tab))
#         c2 = copy.deepcopy( random.choice(x_rg2_tab))
#         fin=False  
#         while fin==False :
#             l1=c1.lstch
#             l2=c2.lstch
#             l1,l2=mix2list(l1,l2)
#             c1.lstch=l1
#             fin=c1.tout_contrainte()
#             if fin==False:
#                 c1 = copy.deepcopy( random.choice(x_rg1_tab))
#                 c2 = copy.deepcopy( random.choice(x_rg2_tab))
#                 l1=c1.lstch
#                 l2=c2.lstch
#                 l1,l2=mix2list(l1,l2)
#                 c1.lstch=l1
#         tab.append(c1)
#         while fin==False :
#             l1=c1.lstch
#             l2=c2.lstch
#             l1,l2=mix2list(l1,l2)
#             c2.lstch=l2
#             fin=c2.tout_contrainte()
#             if fin==False:
#                 c1 = copy.deepcopy( random.choice(x_rg1_tab))
#                 c2 = copy.deepcopy( random.choice(x_rg2_tab))
#                 l1=c1.lstch
#                 l2=c2.lstch
#                 l1,l2=mix2list(l1,l2)
#                 c2.lstch=l2
#         tab.append(c2)
#         # if j<tp:
#         #     N_pop.tab_crom.append(c1)
#         #     j+=1
#         # if j<tp:
#         #     N_pop.tab_crom.append(c2)
#         #     j+=1
#         po=classementnds_corr(po)
#         demi=int(len(po.tab_crom)*0.5)
#         N_pop.tab_crom=tab[:demi]
#     N_pop.update()
#     return N_pop

# def mutation_corr(N_pop):
#     l=list(range(tdp))
#     for i in range(pmu):
#         print(i)
#         #Indice de cromosome séléctionné pour la mutation 
#         icsm = random.choice(l)
#         print(icsm)
#         fin=False  
#         while fin==False :
            
#             # icsm !=0  pour garder la meilleure solution 
#             if icsm !=0 :
#                 csm=N_pop.tab_crom[icsm]
#                 ltcsm=csm.lstch

#                 rind1=randint(0,n_tch-1)
#                 rind2 =randint(0,n_tch-1)

#                 a=ltcsm[rind1]
#                 ltcsm[rind1]=ltcsm[rind2]
#                 ltcsm[rind2]=a

#                 csm.lstch=ltcsm
#                 print("salwa")
#             fin=csm.tout_contrainte()
            

#         N_pop.tab_crom[icsm]=csm
#     return N_pop

# def classement_normal(pop):
#     for i in range(tdp - 1):
#         for j in range(tdp - 1):
#             if pop.tab_crom[j].fo > pop.tab_crom[j + 1].fo:
#                 plus = pop.tab_crom[j]
#                 pop.tab_crom[j] = pop.tab_crom[j + 1]
#                 pop.tab_crom[j + 1] = plus
#     return pop

    # def get_new_population(self):
    #     N_pop = self.selection()
    #     x_tab = self.croisement()
    #     N_pop = N_pop + x_tab[:int(0.5 * len(x_tab))]
    #     self.tab_crom = N_pop
    #     self.tab_crom = self.mutation(N_pop)
    #     self.classementnds()
    #     return self