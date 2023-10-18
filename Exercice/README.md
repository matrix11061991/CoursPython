## Exercice 1: Les listes
  On vous donne une liste d'entiers. Ecrire un programme Python qui permet de :
1. Trouver le plus grand élément de la liste.
2. Trouver le plus petit élément de la liste.
3. Calculer la somme de tous les éléments de la liste.
4. Calculer la moyenne de tous les éléments de la liste.
5. Créer une nouvelle liste contenant uniquement les éléments de la liste initiale qui sont pairs.
6. Créer une nouvelle liste contenant tous les éléments de la liste initiale, sauf le premier et le dernier.
7. Inverser l'ordre des éléments dans la liste initiale.
8. Trier la liste initiale par ordre croissant.
9. Trouver l'indice de la première occurrence d'un élément donné dans la liste initiale.
10.Supprimer la première occurrence d'un élément donné dans la liste initiale.

```python
# Liste d'entiers de départ
lst = [3, 7, 2, 8, 5, 9, 1, 4, 6]

# 1. Trouver le plus grand élément de la liste.
max_element = max(lst)
print("Le plus grand élément de la liste est :", max_element)

# 2. Trouver le plus petit élément de la liste.
min_element = min(lst)
print("Le plus petit élément de la liste est :", min_element)

# 3. Calculer la somme de tous les éléments de la liste.
sum_lst = sum(lst)
print("La somme de tous les éléments de la liste est :", sum_lst)

# 4. Calculer la moyenne de tous les éléments de la liste.
avg_lst = sum_lst / len(lst)
print("La moyenne de tous les éléments de la liste est :", avg_lst)

# 5. Créer une nouvelle liste contenant uniquement les éléments de la liste initiale qui sont pairs.
lst_even = [x for x in lst if x % 2 == 0]
print("La liste contenant uniquement les éléments pairs est :", lst_even)

# 6. Créer une nouvelle liste contenant tous les éléments de la liste initiale, sauf le premier et le dernier.
lst_middle = lst[1:-1]
print("La liste sans le premier et le dernier élément est :", lst_middle)

# 7. Inverser l'ordre des éléments dans la liste initiale.
lst.reverse()
print("La liste inversée est :", lst)

# 8. Trier la liste initiale par ordre croissant.
lst.sort()
print("La liste triée par ordre croissant est :", lst)

# 9. Trouver l'indice de la première occurrence d'un élément donné dans la liste initiale.
element = 5
index = lst.index(element)
print("L'indice de la première occurrence de", element, "est :", index)
## Exercice 2: Les listes
# 10. Supprimer la première occurrence d'un élément donné dans la liste initiale.
lst.remove(element)
print("La liste après suppression de la première occurrence de", element, "est :", lst)
```
## Exercice 2: Les piles (STACK)
Écrivez une classe **Pile** en Python qui implémente une pile (stack) avec les méthodes suivantes :

- $empiler(element)$: Ajoute un élément au sommet de la pile.
- $depiler()$: Retire et retourne l'élément en haut de la pile.
- `est_vide()`: Renvoie $True$ si la pile est vide, $False$ sinon.
- $taille()$: Renvoie la taille de la pile.
```python
class Pile:
    def __init__(self):
        self.elements = []

    def empiler(self, element):
        self.elements.append(element)

    def depiler(self):
        if not self.est_vide():
            return self.elements.pop()
        else:
            print("La pile est vide. Impossible de dépiler.")

    def est_vide(self):
        return len(self.elements) == 0

    def taille(self):
        return len(self.elements)

# Exemple d'utilisation de la classe Pile
ma_pile = Pile()
ma_pile.empiler(1)
ma_pile.empiler(2)
ma_pile.empiler(3)

print("Taille de la pile :", ma_pile.taille())  # Output: 3

element_depile = ma_pile.depiler()
print("Élément dépilé :", element_depile)  # Output: 3
print("Taille de la pile après dépilage :", ma_pile.taille())  # Output: 2

print("La pile est vide :", ma_pile.est_vide())  # Output: False
```
## Exercice 3:Lancer n fois d'un dé a 6 faces
Simuler le lancer d'un dé à six faces (1, 2, 3, 4, 5, ou 6) n fois. La fonction doit retourner True si au moins l'un des n lancers a donné un résultat de 6, sinon elle retourne False. 
```python
from random import randint

def lancer(n) :
    # YOUR CODE HERE
    res = []
    for i in range(n):
        res.append(randint(1,6) == 6)
    return any(res)
```

