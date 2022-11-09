import os
os.system('cls')
from config_ag import *
from V_input import *
from function import *
from function_base import *

def AG():
    pop = gen_po0()
    pop=verification(pop)
    pop=classementnds(pop)
    print("Un Cromosome de la population initiale:")
    pop.tab_crom[1].print_crom()
    pop.tab_crom[1].planning("initiale: ")
    print("*****************************************")
    print("                                         ")
    # pop.print_front("initiale")
    # pop.print_front3d("initiale")
    #l=plot_l_ins(pop)

    for i in range(n_it):
        pop = get_new_population(pop)
        # l=plot_l_add(i,l,pop)  
    # plot_fo(l)
    print("Un Cromosome de la population finale:")
    pop.tab_crom[0].print_crom()
    pop.tab_crom[0].planning( "finale: ")
    print("*****************************************")
    print("                                         ")
    # pop.print_front("finale") 
    # pop.print_front3d("finale")

AG()


