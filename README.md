# Objectif du code 
Ce script a pour objectif de dessiner la courbe d'un profil dit 4 chiffres symétriques NACA00XX et d'en donner le tableau des coordonnées, il calcule aussi son épaisseur maximale et sa position. 

L'utilisateur a l'opportunité de donner les 2 chiffres 'XX' du profil, la longueur de la corde, le nombre de points avec lequel il souhaite discrétiser le profil et la méthode avec laquelle il veut répartir les points sur le profil : linéaire ou non-uniforme.

Enfin l'utilisateur a la possibilité d'enregistrer les coordonnées sous la forme d'un fichier .txt : 'coordonnees_profil_NACA00XX.txt' et la courbe du profil sous la forme d'une image .png : 'profil_NACA00XX.png'. Ces fichiers seront enregistrés dans le même dossier que celui depuis lequel est lancé ce script.

Du code LaTex a été utilisé pour créer ce README, ainsi il est meilleur de le lire directement sur GitHub, les formules mathématiques apparaîtront.

# Comment utiliser le code
Pour utiliser ce script, il suffit de :
- Télécharger le script
- Installer les librairies numpy et matplotlib
- Lancer le script
- Suivre les instructions données dans la console

Attention, une fois que la courbe du profil est affichée, le script se met en pause, il faut alors fermer la fenêtre de la courbe pour qu'il reprenne.

# Stratégie adoptée pour la structure du code
Le code a été réalisé dans un premier temps en supposant que l'utilisateur donnerait tout le temps des réponses appropriées. Ainsi les entrées telles que : les deux derniers chiffres du profil, la longueur de la corde, le nombre de points de discrétisation, la méthode de répartition des points ont toujours le bon type et respectent les choix proposés.
Par la suite, des vérifications de réponses ont été ajoutées afin d'assurer le bon fonctionnement du script.

## Calcul de l'épaisseur maximale et de sa position
L'épaisseur maximale du profil est calculée d'après la formule : $t=corde \times \frac{XX}{100}$ (t = corde*XX/100). D'un autre côté, on recherche l'index du maximum de la liste des coordonnées y, la position de l'épaisseur maximale se situe dans la liste des coordonnées x autour de cet index.

## Calcul des répartitions des coordonnées x
Pour répartir les coordonnées x, l'utilisateur à deux choix : linéaire ou non-uniforme.

### Répartition linéaire
Dans ce cas, on répartit uniformément les coordonnées x entre 0 et la longueur de la corde (entrée par l'utilisateur), en autant de points que le veut l'utilisateur.

### Répartition non-uniforme
Dans ce cas, on utilise la transformée de Glauert pour définir la distribution des points le long de la corde : $x_c = \frac{1}{2}(1-cos(\theta))$

Où $\theta$ est uniformément répartie, en autant de point que le veut l'utilisateur, de 0 à $\pi$ afin de couvrir les valeurs de $x_c$ de 0 à 1.

## Tracé de la courbe du profil
La courbe du profil est tracé en utilisant matplotlib.pyplot. L'intrados et l'extrados sont tracés séparément.

## Fonctions de vérification
Afin de s'assurer que le code fonctionne correctement, plusieurs fonctions de verifications ont été implémentées.

### Fonction verifier_binaire
Cette fonction prend en entrée deux choix : choix1 et choix2. Tant que l'utilisateur n'a pas entré une réponse correspondant à l'un de ces choix, la fonction continue de demander à l'utilisateur de répondre correctement.

Cette fonction est utilisée dans le script lorsque l'utilisateur doit choisir entre 'oui' et 'non' ou encore 'linéaire' et 'non-uniforme'.

### Fonction verifier_int
Cette fonction sert à vérifier qu'une chaîne de caractère contient seulement un entier.
On peut choisir de vérifier que l'entier est positif. Le principe de la fonction est de vérifier que chaque terme de la chaîne de caractère appartient à la liste contenant tous les chiffres, et le signe "-" dans le cas négatif. La fonction vérifie aussi que le signe "-" se trouve uniquement sur le premier terme.

### Fonction verifier_float
Fonctionne de la même manière que verifier_int seulement, on vérifie aussi que la virgule n'apparaît qu'une fois dans la chaîne de caractère.

### Fonctions demander_profil, demander_corde, demander_nbre_points et demander_distribution
Ces fonctions fonctionnent toutes de la même manière : tant que la réponse entrée n'est pas convenable, on demande à l'utilisateur de saisir sa réponse à nouveau.
Finalement, on affiche à l'utilisateur son entrée et on lui demande de confirmer qu'il s'agit de ce qu'il veut étudier.
Les réponses convenables sont : 
- un entier positif de deux chiffres pour <i>demander_profil</i>
- un flottant positif pour <i>demander_corde</i>
- un entier positif pour <i>demander_nbre_points</i>
- 'l' ou 'nu' pour <i>demander_distribution</i>

## Procédure principale : main
Le programme principal fonctionne de la manière suivante :
- On présente le script
- On demande le numéro du profil, la longueur de la corde, le nombre de points de discrétisation, la distribution
- On affiche les informations entrées à l'utilisateur et on lui propose de modifier ses choix ou de continuer :
  - Modifier : on lance <i>main</i> de nouveau
  - Continuer :
    - On calcule les coordonnées <i>x_up</i>, <i>x_down</i>, <i>y_up</i> et <i>y_down</i> selon la distribution choisie
    - On calcule l'épaisseur maximale et sa position le long de la corde
    - On trace les courbes intrados et extrados
    - On propose à l'utilisateur d'enregistrer la courbe dans le fichier 'profil_NACA00XX.png'
    - On affiche la courbe
    - On affiche les coordonnées du profil
    - On propose à l'utilisateur d'enregistrer les coordonnées du profil dans le fichier 'coordonnees_profil_NACA00XX.txt'
    - On propose à l'utilisateur d'étudier un nouveau profil :
        - oui : on lance <i>main</i> de nouveau
        - non : le script est fini

La procédure nettoyer_ecran est utilisée afin d'enlever les informations de la console, il s'agit d'une procédure qui affiche assez de lignes pour faire remonter les lignes précédentes de manière à les faire "disparaître".

# Références
Certaines fonctions et procédures ont été reprises de projets précédents :
- [MGA802 - Jeu du pendu](https://github.com/AlexisM14/JeuDuPendu) : nettoyer_ecran
- [MGA802 - Chiffrement César](https://github.com/MartinGrG/VeniVidiVici) : verifier_int
