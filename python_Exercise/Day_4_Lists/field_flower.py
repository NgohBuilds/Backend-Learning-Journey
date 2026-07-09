"""Flower_field challenge"""
def from_to_string(iterable):
    return "".join(iterable)
def annotate(garden):
    """Add flower counts to empty squares in a completed Flower Field garden.
    
    Args :
        garden (list of str) : Flower Field garden to complete
    Returns:
        list
    Raises :
        ValueError : annotate() receives mallformed input
    """

    flower_counter = 0
    

    for ind_up, portion in enumerate(garden) :
        portion = portion.split()
        for index, elt in enumerate(portion) :
            if not elt : # Est pas un espace 
                position_droite = index + 1
                if position_droite < len(portion) - 1 : # N'est pas la derniere colonne
                    if portion[index + 1] == "*": # * a droite
                        flower_counter += 1
                position_gauche = index - 1  # Pas sur la premiere colonne 
                if position_gauche > 0 : # est a l'extremite gauche ?
                    if portion [position_gauche] == "*": # * a gauche ?
                        flower_counter += 1
                # La portion de fleur du haut 
                position_up = ind_up - 1
                if position_up > 0 : # une case en haut
                    if garden[ind_up][index] == "*": # En haut est *
                        flower_counter += 1
                    if garden[ind_up][index + 1] == "*": # En haut a droite est *
                        flower_counter += 1
                    if index - 1 > 0:
                        if garden[ind_up][index - 1] == "*":
                            flower_counter += 1

                # La portion de fleur du bas 
                position_down = ind_up + 1
                if position_down < len(garden) - 1: # Y a t'il des portions en bas ?
                    if garden[ind_up + 1][index] == "*": #"Y a * en bas ?"
                        flower_counter += 1
                    if garden[ind_up + 1][index + 1] == "*":  #"Y a * en bas a droite"
                        flower_counter += 1
                    if index - 1 > 0 : # est extremite ?
                        if garden[ind_up + 1][index - 1] == "*":
                            flower_counter += 1
            #Finale
                elt = flower_counter
                flower_counter = 0
   
    return [from_to_string(iterable) for iterable in garden]
