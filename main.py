import os # importation du module os

def dessine_grille(tab):
    """
    affiche l'état de la partie (position joueur / map / etc)

    prend en argument tab qui représente le grille 3 * 3
    """
    os.system('cls')  
    print("   1   2   3")  
    for i in range(3):
        ligne = f"{i+1} "  
        for j in range(3):
            ligne += f"{tab[i][j]}" 
            if j < 2:
                ligne += "|" 
        print(ligne)  
        if i < 2:
            print("  ---+---+---")  

def jouer_tour(tab, joueur):
    """
    permet à un joueur de jouer son tour en choisissant une ligne et une colonne
    pour placer son symbole dans la grille.

    prend en argument la grille 3 * 3 et le symbole du joueur (son tour par la même occasion)    
    """
    lignes = int(input(f"{joueur[1]}: Lignes ? ")) - 1 
    colonne = int(input(f"{joueur[1]}: Colonnes ? ")) - 1
    if verif_tour(tab, lignes, colonne):
        tab[lignes][colonne] = joueur
    else:
        dessine_grille(tab)
        print("Case déjà occupée ou coordonnées invalides. Réessayez.")
        return jouer_tour(tab, joueur)
        
def verif_tour(tab, cord_x, cord_y):
    """
    vérifie si le joueur ne donne pas des coordonnées hors map ou encore
    que la cse soit vide

    prend en argument la grille 3 * 3 et les coordonnées

    retourne True si la case est vide et que les coordonnées sont bonne sinon il retourne False
    """
    return 0 <= cord_x < 3 and 0 <= cord_y < 3 and tab[cord_x][cord_y] == "   "

def condition_fin_partie(tab, joueur):
    """
    vérifie si un joueur a gagné la partie de n'importe quelle manière

    prend en argument la grille 3 * 3 et le symbole du joueur (son tour par la même occasion) 

    retourne True si un joueur gagne sinon False   
    """
    return condition_fin_partie_diag(tab, joueur) or condition_fin_partie_li_et_col(tab, joueur)

def condition_fin_partie_diag(tab, joueur):
    """
    vérifie si un joueur a gagné la partie via les diagonales

    prend en argument la grille 3 * 3 et le symbole du joueur (son tour par la même occasion) 

    retourne True si un joueur via les diagonales gagne sinon False   
    """
    if (tab[0][0] == joueur and tab[1][1] == joueur and tab[2][2] == joueur) or \
       (tab[0][2] == joueur and tab[1][1] == joueur and tab[2][0] == joueur):
        return True
    return False

def condition_fin_partie_li_et_col(tab, joueur):
    """
    vérifie si un joueur a gagné la partie via les lignes ou les colonnes

    prend en argument la grille 3 * 3 et le symbole du joueur (son tour par la même occasion) 

    retourne True si un joueur gagne vai les lignes ou les colonnes sinon False   
    """
    for i in range(3):
        if (tab[i][0] == joueur and tab[i][1] == joueur and tab[i][2] == joueur) or \
           (tab[0][i] == joueur and tab[1][i] == joueur and tab[2][i] == joueur):
            return True
    return False

def condition_fin_partie_null(tab):
    """
    vérifie que tab ne contient pas de case vide

    prend en argument la grille 3 * 3 

    retourne True si c'est match null sinon False   
    """
    for i in range(3):
        for j in range(3):
            if tab[i][j] == "   ":
                return False
    return True

def rejouer():
    """
    permet de rejouer en relancant le programme ou de quitter le programme  
    """
    restart = input("Rejouer [Y/N]: ").strip().upper()
    if restart == "Y":
        return main()  
    elif restart == "N":
        os._exit(0)  
    else:
        os.system('cls')
        return rejouer()

def main():
    """
    fonction principale qui initialise la grille, démarre le jeu et gère les tours des joueurs
    
    le jeu s'exécute jusqu'à ce qu'il y ait un gagnant ou une égalité. après la fin du jeu,
    le joueur peut choisir de rejouer
    """
    # initialisations des variables du jeu
    joueur_1 = " X " 
    joueur_2 = " O "
    grille = [["   " for _ in range(3)] for _ in range(3)]
    les_joueurs = [joueur_1, joueur_2]
    tour = 1

    # boucle du jeu 
    dessine_grille(grille)
    while not condition_fin_partie(grille, les_joueurs[tour]) and not condition_fin_partie_null(grille):
        tour = 1 - tour 
        jouer_tour(grille, les_joueurs[tour])
        dessine_grille(grille)
        
    # menu fin de partie
    if condition_fin_partie(grille, les_joueurs[tour]):
        print(f"{les_joueurs[tour]} ont gagné !!")
    else:
        print("égalité !!")
    
    # option pour rejouer
    rejouer()


main() # lancement du jeu 