def spiral_matrix(size):
    # Initialise la matrice avec des zéros
    n = size
    matrice = [[0] * n for _ in range(n)]
    
    # Position de départ
    ligne, colonne = 0, 0
    
    # Vecteur de direction (départ : vers la droite)
    dr = [0, 1, 0, -1]
    dc = [1, 0, -1, 0]
    direction = 0 # Indice pour dr et dc
    
    # Remplissage
    for i in range(1, n * n + 1):
        matrice[ligne][colonne] = i
        
        # Calcul de la prochaine case
        next_ligne = ligne + dr[direction]
        next_colonne = colonne + dc[direction]
        
        # Vérification si la case est valide (dans la matrice et vide)
        if (not (0 <= next_ligne < n and 0 <= next_colonne < n) or 
            matrice[next_ligne][next_colonne] != 0):
            # Tourner à droite
            direction = (direction + 1) % 4
            
        # Avancer
        ligne += dr[direction]
        colonne += dc[direction]
        
    return matrice