
#Nombre de tâches
n_tch = 21
#Nombre de ressources
n_ress = 3
#la liste des ressources 
list_ress =['h','r','hr']

#les propriétés de la tâche:

#Données Exemple 

# #le temps opératoire Pt de la tâche selon la ressource choisie en seconde
#             #0   1   2   3   4   5    6   7   8  9
# list_pt_h = [50, 15, 75, 40, 55, 30, 35, 20, 45, 30]
# list_pt_r = [30, 20, 55, 10, 25, 50, 44, 17, 90, 50]
# list_pt_hr = [25, 10, 20, 5, 30, 25, 27, 19, 28, 25]


# list_pt=[list_pt_h,list_pt_r,list_pt_hr]

# # le coût de la tâche selon la ressource choisie 
# list_cout_h = [10, 4, 15, 8, 11, 6, 7, 4, 9, 6]
# list_cout_r = [8, 3, 8.25, 15, 3.75, 7.5, 6.6, 2.55, 13.5, 7.5]
# list_cout_hr = [5, 4.50, 12, 8.75, 6.0, 8.75, 9.45, 350, 9.8, 8.75]

# list_cout=[list_cout_h,list_cout_r,list_cout_hr]

# # les paramètres de fatigues   

# list_cf_t=[2, 3, 8, 8, 8, 8, 8, 4, 8, 8]
# cr_op= 8

# # les conditions de précedence
# sec_in = [
#         [0,1],
#         [2,1],
#         # [3,2],
#         # [4,3],
#         # [5,4],
#         # [6,5],
#         # [7,6],
#         # [8,7],
#         # [9,8],
# ]


#les données de notre USE Case 

#le temps opératoire Pt de la tâche selon la ressource choisie en seconde:
list_pt_h = [50, 15, 75, 40, 55, 30, 35, 20, 45, 30, 35, 50, 30, 45, 28, 30, 75, 46, 27, 71, 44]
list_pt_r = [30, 20, 55, 100, 25, 50, 44, 17, 90, 50, 44, 20, 15, 88, 17, 50, 55, 89, 28, 53, 88]
list_pt_hr = [100000, 100000, 40, 25, 1000000, 25, 27, 1000000, 28, 25, 27, 1000000, 100000, 31, 1000000, 25, 40, 36, 100000, 41, 39]

list_pt=[list_pt_h,list_pt_r,list_pt_hr]

# le coût de la tâche selon la ressource choisie:
list_cout_h = [10, 3, 15, 8, 11, 6, 7, 4, 9, 6, 7, 10, 6, 9, 5.6, 6, 15, 9.2, 5.4, 14.2, 8.8]
list_cout_r = [2.1, 1,4, 3.85, 7, 1.75, 3.5, 3.08, 1.19, 6.3, 3.5, 3.08, 1.4, 1.05, 6.16, 1.19, 3.5, 3.85, 6.23, 1.96, 3.71, 6.16]
list_cout_hr = [270000, 270000, 10.8, 6.75, 270000, 6.75, 7.29, 270000, 7.56, 6.75, 7.29, 270000, 270000, 8.37, 270000, 6.75, 10.8, 9.72, 270000, 11.07, 10.53]

list_cout=[list_cout_h,list_cout_r,list_cout_hr]

# les conditions de précedence
sec_in = [
          [1, 0],
          [2, 1],
          [3, 2],
          [5, 4],
          [6, 5],
          [7, 0],
          [8, 6],
          [8, 7],
          [9, 4],
          [10, 9],
          [12, 11],
          [13, 10],
          [13, 12],
          [14, 11],
          [15, 14],
          [16, 15],
          [17, 16],
          [18, 11],
          [19, 18],
          [19, 20]
]

list_cf_t=[3, 2, 1, 4, 3, 2, 5, 2, 2, 5, 2, 3, 5, 2, 2, 1, 1, 4, 2, 1,4]
cr_op= 3