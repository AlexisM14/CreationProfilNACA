# Ce fichier contient des fonctions nécessaires à la bonne utilisation du fichier main

def nettoyer_ecran():
    """Cette procédure permet de nettoyer la console, afin que rien n'y soit plus affiché"""
    print("")
    print("")
    print("")
    print("")
    print("")
    print("")
    print("")
    print("")
    print("")
    print("")
    print("")
    print("")
    print("")
    print("")
    print("")
    print("")
    print("")
    print("")
    print("")
    print("")
    print("")
    print("")


def verifier_binaire(choix1, choix2):
    """Cette fonction sert à s'assurer que l'utilisateur a entré une réponse parmi 2 choix"""
    # Entrée : des chaînes de caractères
    # Sortie : une chaîne de caractère
    choix = input(" ")
    liste_choix = [choix1, choix2]
    while choix not in liste_choix:
        print(f"La réponse entrée : '{choix}' n'est pas correcte. ")
        choix = input(f"Veuillez choisir entre : {choix1} et {choix2}. ")
    return choix


def verifier_int(chaine, signe='+-'):
    """Cette fonction sert à vérifier qu'une chaîne de caractère contient seulement un entier"""
    # Entrée : chaîne de caractère
    # Sorite : booléen
    if signe == '+':
        liste_int = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    else:
        liste_int = ['-', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    for idx, elem in enumerate(chaine):
        if elem not in liste_int:
            return False
        elif len(chaine) == 1:
            return False
        elif elem == '-' and idx != 0:
            return False
    return True


def verifier_float(chaine, signe='+-'):
    """Cette fonction sert à vérifier qu'une chaîne de caractère contient un entier"""
    # Entrée : chaîne de caractère
    # Sortie : booléen
    nbre_point = 0
    if signe == '+':
        liste_float = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '.']
    else:
        liste_float = ['-', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '.']
    for idx, elem in enumerate(chaine):
        if elem not in liste_float:
            return False
        elif elem == '.':
            nbre_point += 1
            if len(chaine) == 1:
                return False
        elif elem == '-':
            if len(chaine) == 1 or idx != 0:
                return False
        elif len(chaine) < 1:
            return False
    if nbre_point > 1:
        return False
    return True


def demander_profil():
    nombre_profil = input("Veuillez saisir les deux derniers chiffres (XX de NACA00XX) du profil. ")
    affirmation = verifier_int(nombre_profil, '+') and len(nombre_profil) == 2

    while not affirmation:
        nettoyer_ecran()
        print(f"Les caractères entrés ne sont pas corrects : "
              f"'{nombre_profil}' ne peut pas correspondre aux deux derniers chiffres du profil NACA00XX. ")
        nombre_profil = input("Veuillez saisir les deux derniers chiffres (XX de NACA00XX) du profil. ")
        affirmation = verifier_int(nombre_profil, '+') and len(nombre_profil) == 2
    nettoyer_ecran()
    print(f"Entrez 'oui' si vous voulez étudier le profil NACA00{nombre_profil}, sinon entrez 'non'")
    choix = verifier_binaire('oui', 'non')
    if choix == 'non':
        nombre_profil = demander_profil()
    return int(nombre_profil)


def demander_corde():
    corde = input("Quelle est la longueur de la corde (en mètre) du profil que vous souhaitez étudier. ")
    affirmation = verifier_float(corde, '+') and len(corde) >= 1

    while not affirmation:
        nettoyer_ecran()
        print(f"Les caractères entrés : '{corde}' ne correspondent pas une longueur. ")
        corde = input("Quelle est la longueur de la corde (en mètre) du profil que vous souhaitez étudier. ")
        affirmation = verifier_float(corde, '+') and len(corde) >= 1
    nettoyer_ecran()
    print(f"Entrez 'oui' si la corde du profil que vous souhaitez étudier mesure {corde} [m], sinon entrez 'non'")
    choix = verifier_binaire('oui', 'non')
    if choix == 'non':
        corde = demander_corde()
    return float(corde)


def demander_nbre_points():
    nbre_points = input("Combien de points voulez-vous étudier sur ce profil, le long de la corde ? ")
    while not verifier_int(nbre_points, '+'):
        nettoyer_ecran()
        print(f"Le nombre de points entré : '{nbre_points}' n'est pas correct.")
        nbre_points = input("Combien de points voulez-vous étudier sur ce profil ? ")
    nettoyer_ecran()
    print(f"Entrez 'oui' si vous souhaitez étudier mesure {nbre_points} points, sinon entrez 'non'. ")
    choix = verifier_binaire('oui', 'non')
    if choix == 'non':
        nbre_points = demander_nbre_points()
    return int(nbre_points)


def demander_distribution():
    print("Veuillez entrer 'l' pour linéaire et 'nu' pour non-uniforme. ")
    distribution = verifier_binaire('l', 'nu')
    nettoyer_ecran()

    if distribution == 'l':
        distribution = 'linéaire'
    else:
        distribution = 'non-uniforme'

    nettoyer_ecran()
    print(f"Entrez 'oui' si vous souhaitez utiliser la distribution {distribution}, sinon entrez 'non'. ")
    choix = verifier_binaire('oui', 'non')
    if choix == 'non':
        nettoyer_ecran()
        distribution = demander_distribution()
    return distribution
