# Les fonctions

En informatique, __les fonctions servent à mieux structurer votre code. Par exemple, elles permettent d'éviter de répéter plusieurs fois des portions de codes identiques__. 

Ainsi, une fonction peut être vu comme un «petit» programme :

- à qui on donne (le plus souvent) des __paramètres en entrée__,
- puis qui effectue alors un __traitement sur ces paramètres__,
- qui __renvoie enfin un résultat en sortie__.

Une fonction qui modifie des variables mais __sans renvoyer de résultat est appelée une procédure__. Le langage Python ne fait pas de différence dans la syntaxe entre fonction et procédure.


## Les fonctions en Python

En Python, une fonction est définie en suivant toujours le même formalisme :

- Commencer par le __mot clé `def`__,
- Poursuivre sur la même ligne par l'entête constituée des 3 éléments successifs suivants :
  - le __nom de la fonction__
  - entre __parenthèses, les paramètres__, avec pour chacun un nom
  - terminer la première ligne par __deux points `:`__
- En dessous, écrire le __blocs des instructions__. Attention il faut __indenter__ (décaler de 4 espaces avec la touche TAB) ce bloc !
- Finir en dernière ligne par le __mot clé `return`__, suivi de ce que renvoie la fonction (ou `None` si la fonction ne retourne rien). Cette ligne est indentée également et marque la fin de la fonction.

### Structure d'une fonction en Python

```python
def nom_fonction(liste des paramètres):
	blocs des instructions
	return résultat
```

### Un exemple d'application : la fonction `carre()`
```python
def carre(x):
    return x ** 2   # l'opérateur ** correspond à une puissance
```
