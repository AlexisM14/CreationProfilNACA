# Ce script permet ....

import numpy as np
import matplotlib.pyplot as plt


def main():
    print("Ce script vous permet d'obtenir le tracé et les coordonnées d'un profil 4 chiffres symétrique NACA00XX. ")

    nombre_profil = int(input("Veuillez saisir les deux derniers chiffres (XX de NACA00XX) du profil. "))

    corde = float(input("Quelle est la longueur de la corde (en mètre) du profil que vous souhaitez étudier. "))

    nbre_points = int(input("Combien de points voulez-vous étudier sur ce profil ? "))

    print("Quel est le type de distribution de points le long de la corde : linéaire ou non-uniforme. ")
    distribution = input("Veuillez entrer 'l' pour linéaire et 'nu' pour non-uniforme. ")

    print(f"Vous voulez étudier le profil NACA00{nombre_profil}, dont la corde mesure {corde} [m]. ")
    print(f"Le calcul se fera en suivant la distribution {distribution}, sur {nbre_points} points. ")

    if distribution == 'l':
        xc = np.linspace(0, 1, nbre_points)
        x_up = xc * corde
        x_down = x_up.copy()
    else:
        theta = np.linspace(0, np.pi, nbre_points)
        xc = .5 * (1 - np.cos(theta))
        x_up = xc * corde
        x_down = x_up.copy()

    t = nombre_profil/100

    yt = 5 * t * (0.2969 * np.sqrt(xc) - 0.1260 * xc - 0.3516 * xc ** 2 + 0.2843 * xc ** 3 - 0.1036 * xc ** 4)
    y_up = yt * corde
    y_down = -yt * corde

    epaisseur = y_up - y_down
    idx_epaisseur_max = np.argmax(epaisseur)
    epaisseur_max = epaisseur[idx_epaisseur_max]
    position_epaisseur_max = x_up[idx_epaisseur_max]
    print(" ")
    print(f"L'épaisseur maximale vaut {epaisseur_max} [m] et est atteinte à {position_epaisseur_max} [m] du bord d'attaque")
    print(" ")

    plt.plot(x_up, y_up, label='Extrados', color='r')
    plt.plot(x_down, y_down, label='Intrados', color='b')
    plt.title(f"Profil du NACA00{nombre_profil}")
    plt.xlabel('x [m]')
    plt.ylabel('y [m]')
    plt.legend()
    plt.grid()
    plt.show()

    print("Merci d'avoir utilisé ce script. Voulez-vous étudier un autre profil ? ")
    choix_relancer = input("Entrez 'oui' ou 'non'. ")
    if choix_relancer == 'oui':
        main()
        return
    else:
        print("À bientôt !")


main()
