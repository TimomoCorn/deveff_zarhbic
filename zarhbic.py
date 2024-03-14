def lecture_fichier(nom_fichier):
    """Lit un fichier et renvoie une liste de ses lignes."""
    with open(nom_fichier, 'r') as file:
        liste_expression = []
        for line in file:
            liste_expression.append(line)
    return liste_expression
        

def evaluer_zarhbic(expression):
    """Évalue une expression Zarhbic et renvoie le résultat."""
    pile = []
    symboles = expression.split()

    for symbole in symboles:
        if est_operande(symbole):
            pile.append(int(symbole))
        elif est_operateur(symbole):
            evaluer_operation(symbole, pile)
        else:
            raise ValueError("Erreur : symbole non reconnu dans l'expression.")

    if len(pile) != 1:
        raise ValueError("Erreur : l'expression n'est pas valide.")

    return pile[0]

def est_operande(symbole):
    """Vérifie si un symbole est un opérande (un nombre)."""
    return symbole.isdigit() or (symbole[0] == '-' and symbole[1:].isdigit())

def est_operateur(symbole):
    """Vérifie si un symbole est un opérateur (+, -, *, /)."""
    operateurs = ['+', '-', '*', '/']
    return symbole in operateurs 

def evaluer_operation(operateur, pile):
    """Évalue une opération et met à jour la pile avec le résultat."""
    if len(pile) < 2:
        raise ValueError("Erreur : pas assez d'opérandes pour l'opérateur {}.".format(operateur))

    operand2 = pile.pop()
    operand1 = pile.pop()

    if operateur == '+':
        pile.append(operand1 + operand2)
    elif operateur == '-':
        pile.append(operand1 - operand2)
    elif operateur == '*':
        pile.append(operand1 * operand2)
    elif operateur == '/':
        pile.append(operand1 / operand2)

def affichage_calcul(expression):
    """Affiche une expression Zarhbic."""
    print(f"L'expression Zarhbic est {expression}")

def affichage_resultat(resultat):
    """Affiche le résultat d'une expression Zarhbic."""
    print(f"L'expression Zarhbic vaut {resultat}")

# Exemple d'utilisation
        
if __name__ == '__main__':
    expressions = lecture_fichier('./import_zarhbic.txt')

    for expression in expressions:
        resultat = evaluer_zarhbic(expression)
        
        affichage_calcul(expression)
        affichage_resultat(resultat)
