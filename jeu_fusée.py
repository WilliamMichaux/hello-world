def nbr_prs(average_somme):
    
    prix_personne = 0
    personne = 1

    while prix_personne <= average_somme:
    	personne += 1
        prix_personne += (personne-1)
    print personne

nbr_prs(4500)
