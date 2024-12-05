#### Imports et définition des variables globales
'''
Lis le données d'un fichier
'''
FILENAME = "listes.csv"
#### Fonctions secondaires
def read_data(filename):
    """retourne le contenu du fichier <filename>

    Args:
        filename (str): nom du fichier à lire
    Returns:
        list: le contenu du fichier (1 list par ligne)
    """
    with open(filename, mode='r', encoding='utf-8') as file:
        return [list(map(int, line.strip().split(';'))) for line in file.readlines()]

def get_list_k(data, k):
    '''
    retourne la liste
    '''
    return data[k] if 0 <= k < len(data) else None

def get_first(l):
    '''
    retourne le premier élément
    '''
    return l[0] if l else None

def get_last(l):
    '''
    retourne le dernier élément
    '''
    return l[-1] if l else None

def get_max(l):
    '''
    retourne l'élément le plus grand
    '''
    return max(l) if l else None

def get_min(l):
    '''
    retourne le plus petit élément
    '''
    return min(l) if l else None

def get_sum(l):
    '''
    retourne la somme des éléments
    '''
    return sum(l) if l else None

#### Fonction principale
def main():
    '''
    appelle les fonctions
    '''
    try:
        data = read_data(FILENAME)
        print("Données lues :")
        for i, l in enumerate(data):
            print(f"Ligne {i} : {l}")
        k = 37
        liste_k = get_list_k(data, k)
        if liste_k is not None:
            print(f"\nListe {k} : {liste_k}")
            print(f"Premier élément : {get_first(liste_k)}")
            print(f"Dernier élément : {get_last(liste_k)}")
            print(f"Maximum : {get_max(liste_k)}")
            print(f"Minimum : {get_min(liste_k)}")
            print(f"Somme : {get_sum(liste_k)}")
        else:
            print(f"\nL'indice {k} est hors limites (données disponibles : {len(data)} lignes).")
    except FileNotFoundError:
        print(f"Erreur : le fichier '{FILENAME}' est introuvable.")
    except ValueError as e:
        print(f"Erreur dans le fichier '{FILENAME}' : {e}")

if __name__ == "__main__":
    main()
