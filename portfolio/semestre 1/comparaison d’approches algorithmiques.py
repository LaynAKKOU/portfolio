##############
# SAE S01.02 #
##############

#question 1
def create_network(tab):
    if tab==[]:
        return "tableau vide"
    dico={}
    i=0
    while i<len(tab)/2:
        if tab[2*i] in list(dico):
            dico[tab[2*i]]+=[tab[2*i+1]]
        else:
            dico[tab[2*i]]=[tab[2*i+1]]
        if tab[2*i+1] in list(dico):
            dico[tab[2*i+1]]+=[tab[2*i]]
        else:
            dico[tab[2*i+1]]=[tab[2*i]]
        i+=1
    return dico
#question 3

def get_people(reseau):
    if reseau=={}:
        return "reseau vide"
    personne=[]
    tab= list(reseau)
    i=0
    while i< len(tab):
        if tab[i] not in personne:
            personne.append(tab[i])
        i+=1 
    return personne
#question 4

def are_friend(reseau,personne1,personne2):
    """reseau: dict, un dictionnaire dont les clés sont les prénoms des personnes et les valeurs des tableaux contenant la liste des amis de la personne.
       personne1: int, prénom d'une personne appartenant au reseau.
       personne2: int, prénom d'une personne appartenant au reseau.
       Cette fonction  retourne True si personne1 et personne2 sont amies, et False sinon."""
    if personne2 in reseau[personne1] and personne1 in reseau[personne2]:
        return True
    return False




#question 5

def all_his_friends(reseau,personne,groupe):
    """
       reseau: dict, un dictionnaire dont les clés sont les prénoms des personnes et les valeurs des tableaux contenant la liste des amis de la personne.
       personne: int, prénom d'une personne appartenant au reseau.
       groupe: list, tableau de personnes.
       cette fonction retourne True si la personne est amie avec toutes les personnes du groupe, et False sinon."""
    for i in range(len(groupe)):
        if not (groupe[i] in reseau[personne]):
            return False
    return True

#question 6

def is_a_communaute(reseau,groupe):
    """
       reseau: dict, un dictionnaire dont les clés sont les prénoms des personnes et les valeurs des tableaux contenant la liste des amis de la personne.
       groupe: list, tableau de personnes.
       Cette fonction retourne True si ce groupe est une communauté, et False sinon."""
    for i in range(len(groupe)):
        for a in range(len(groupe)):
            if not (groupe[i] in reseau[groupe[a]]) and groupe[i]!=groupe[a]:
                return False
    return True

#question 7

def find_community (reseau, groupe) :
    """
        reseau: dict, un dictionnaire dont les clés sont les prénoms des personnes et les valeurs des tableaux contenant la liste des amis de la personne.
        groupe: list, tableau de personnes.
        Cette fonction retourne la communauté maximale (au sens où il n'existe personne qui puisse être ajoutée dans cette communauté) du réseau"""
    com=[groupe[0]]
    for i in range (len(groupe)):
        nb_com=len(com)-1
        nb=0
        for a in range(len (com)):
            if groupe[i] in com[a] and groupe [i]!=com[a]:
                nb+=0
        if nb==nb_com:
            com.append(groupe[i])
    return com

#question 8 

def order_by_decreasing_popularity(reseau,groupe):
    """
       reseau: dict, un dictionnaire dont les clés sont les prénoms des personnes et les valeurs des tableaux contenant la liste des amis de la personne.
       groupe: list, tableau de personnes.
       Cette fonction trie le groupe de personnes selon la popularité (nombre d'amis) décroissante."""
    nb_amis=[]
    for i in range(len(groupe)):
        nb_amis.append(len(reseau[groupe[i]]))
    n = len(nb_amis)
    for i in range(n):
        for j in range(0, n-i-1):
            if nb_amis[j] < nb_amis[j+1] :
                nb_amis[j], nb_amis[j+1] = nb_amis[j+1], nb_amis[j]
                groupe[j], groupe[j+1] = groupe[j+1], groupe[j]
    return groupe

#question 9

def find_community_by_decreasing_popularity(reseau):
    """
       reseau: dict, un dictionnaire dont les clés sont les prénoms des personnes et les valeurs des tableaux contenant la liste des amis de la personne.
       Cette fonction doit trier l'ensemble des personnes du réseau selon l'ordre décroissant de popularité puis retourner la communauté trouvée en appliquant l'heuristique de construction de communauté maximale expliquée plus haut.
    """
    if reseau=={}:
        return []
    groupe=list(reseau)
    long_group=len(groupe)
    tab=[]
    for personne in range(long_group):
        for i in range(long_group-personne-1,0,-1):
            if len(reseau[groupe[i]]) > len(reseau[groupe[i-1]]):
                tab=groupe[i]
                groupe[i]=groupe[i-1]
                groupe[i-1]=tab
    commu=[groupe[0]]
    for personne in groupe:
        amis=0
        for i in commu:
            if personne in reseau[i] and personne not in commu:
                amis+=1
        if amis== len(commu):
            commu.append(personne)
    return commu


#question 10

def find_community_from_person(reseau,personne):
    """
       reseau: dict, un dictionnaire dont les clés sont les prénoms des personnes et les valeurs des tableaux contenant la liste des amis de la personne.
       personne: int, prénom d'une personne appartenant au reseau.
       cette fonction retourne une communauté maximale contenant cette personne selon l'heuristique suivant:on choisit une personne du réseau,on crée une communauté contenant juste cette personne,
       on considère les amis de cette personne par ordre de popularité décroissante. Pour chacune de ces personnes, si celle-ci est amie avec tous les membres de la communauté déjà créée, alors on l'ajoute à la communauté.
       """
    communaute=[personne]
    gens=list(reseau)
    for i in range(len(reseau[personne])+2):
        cpt=0
        for a in range(len(communaute)):
            if gens[i] in reseau[gens[a]]:
                cpt+=1
        if cpt==len(communaute):
            communaute.append(gens[i])
    return communaute


#question 12

def find_max_community(reseau):
    """
       reseau:dict, un dictionnaire dont les clés sont les prénoms des personnes et les valeurs des tableaux contenant la liste des amis de la personne.
       La fonction doit retourner la plus grande communauté trouvée."""
    personnes=list(reseau)
    plus_grande_commu=[]
    for i in range(len(personnes)):
        commu=find_community_from_person(reseau,personnes[i])
        if len(commu) > len(plus_grande_commu):
            plus_grande_commu= commu
    return plus_grande_commu
