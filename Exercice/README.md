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

# 10. Supprimer la première occurrence d'un élément donné dans la liste initiale.
lst.remove(element)
print("La liste après suppression de la première occurrence de", element, "est :", lst)
```
