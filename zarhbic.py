"""Module zarhbic.
Un célèbre druide Breton du « Penn ar bed », nommé Zarhbic, vous remarquerez l'orthographe
« rh » comme un enseignant d'info du 21ième siècle, a une drôle façon de faire les calculs
arithmétiques même dans son état normal.

Exemple:

Calcul n°1 : 3 5 + donne 8
Calcul n 2 : 4 7 + 3 * donne 33
Calcul n 3 : 3 4 7 + * donne 33
Calcul n 4 : 10 4 + 2 - donne 12
Calcul n 5 : 2 10 4 + - donne -12
"""


def lecture_fichier(nom_fichier):
    """Lit un fichier et renvoie une liste de ses lignes."""
    with open(nom_fichier, encoding="utf-8", mode="r") as file:
        liste_expression = []
        for line in file:
            liste_expression.append(line)
    return liste_expression
        

def evaluer_zarhbic(expression):
    """Évalue une expression Zarhbic et renvoie le résultat."""
    pile_evaluation = []
    symboles = expression.split()

    for symbole in symboles:
        if est_operande(symbole):
            pile_evaluation.append(int(symbole))
        elif est_operateur(symbole):
            evaluer_operation(symbole, pile_evaluation)
        else:
            raise ValueError("Erreur : symbole non reconnu dans l'expression.")

    if len(pile_evaluation) != 1:
        raise ValueError("Erreur : l'expression n'est pas valide.")

    return pile_evaluation[0]

def est_operande(symbole):
    """Vérifie si un symbole est un opérande (un nombre)."""
    return symbole.isdigit() or (symbole[0] == '-' and symbole[1:].isdigit())

def est_operateur(symbole):
    """Vérifie si un symbole est un opérateur (+, -, *, /)."""
    operateurs = ['+', '-', '*', '/']
    return symbole in operateurs 

def evaluer_operation(operateur, pile_operation):
    """Évalue une opération et met à jour la pile avec le résultat."""
    if len(pile_operation) < 2:
        raise ValueError(f"Erreur : pas assez d'opérandes pour l'opérateur {operateur}.")

    operand2 = pile_operation.pop()
    operand1 = pile_operation.pop()

    if operateur == '+':
        pile_operation.append(operand1 + operand2)
    elif operateur == '-':
        pile_operation.append(operand1 - operand2)
    elif operateur == '*':
        pile_operation.append(operand1 * operand2)
    elif operateur == '/':
        pile_operation.append(operand1 / operand2)

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
