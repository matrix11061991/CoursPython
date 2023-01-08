# Cours Python 3
Ce cours s’adresse aux débutants qui souhaitent acquérir des bases de programmation en python.
## Présentation des outils de programmation
Python est un langage de programmation populaire pour la science des données, le développement web, l'automatisation de tâches et bien d'autres choses. Il existe plusieurs outils qui peuvent vous aider à utiliser Python de manière efficace et productive. Voici quelques exemples d'outils couramment utilisés :

* Interpréteur Python : c'est l'outil de base pour exécuter du code Python. Vous pouvez l'utiliser en mode interactif en entrant des instructions une par une, ou bien en exécutant un fichier de code en utilisant la commande `python mon_fichier.py`.

* IDE (Integrated Development Environment) : ce sont des environnements de développement intégrés qui vous permettent d'écrire, de déboguer et de tester du code Python de manière plus pratique. Exemples d'IDE populaires : PyCharm, IDLE (inclus avec l'installation de Python), Visual Studio Code, Eclipse avec le plugin PyDev.

* Bibliothèques et modules : Python est livré avec un certain nombre de bibliothèques standard qui vous permettent d'utiliser des fonctionnalités prédéfinies, telles que la gestion des fichiers, la communication réseau, etc. Vous pouvez également utiliser des modules tiers, disponibles sur PyPI (Python Package Index), qui étendent les fonctionnalités de base de Python.

* Virtualenv : cet outil vous permet de créer des environnements virtuels Python isolés, ce qui est utile pour développer plusieurs projets qui ont des exigences de dépendances différentes. Cela vous permet également de facilement changer de version de Python ou de modules pour chaque projet.

* Jupyter Notebook : c'est un environnement de développement web interactif qui vous permet d'écrire, d'exécuter et de partager du code Python, ainsi que de documenter votre travail avec du texte et des équations. Il est souvent utilisé dans le domaine de la science des données et de la formation.

Il y a bien d'autres outils disponibles, en fonction des besoins et du domaine d'application.
## Les bases rapides en Python
Les variables en Python sont des noms qui peuvent être utilisés pour stocker des valeurs de différents types (nombres, chaînes de caractères, listes, dictionnaires, etc). Voici comment déclarer et utiliser des variables en Python :
```python
# déclaration d'une variable x et affectation de la valeur 10
x = 10
# affichage de la valeur de la variable x
print(x)  # affiche 10
# déclaration d'une variable y et affectation de la valeur "Bonjour"
y = "Bonjour"
# concaténation de la variable y avec la chaîne " tout le monde" et affectation du résultat à la variable z
z = y + " tout le monde"
# affichage de la valeur de la variable z
print(z)  # affiche "Bonjour tout le monde"
```
Il y a quelques règles à respecter lors de la déclaration de variables en Python :

* Le nom d'une variable ne peut pas commencer par un chiffre.
* Le nom d'une variable ne peut pas contenir d'espaces ni de caractères spéciaux, à l'exception de l'underscore (_).
* Le nom d'une variable ne peut pas être un mot clé réservé (par exemple `for`, `while`, `def`, etc.).
En général, il est recommandé de donner des noms de variables significatifs et de respecter les conventions de style de Python, telles que le "camelCase" pour les noms de variables composées (par exemple `maVariable`) et l'underscore pour les noms de variables séparées par des mots (par exemple `mon_nom`).
## Exécution d’un premier programme
```python
# ce code est un commentaire, il est ignoré par l'interpréteur
# pour écrire un commentaire, utilisez le caractère #
print("Bonjour tout le monde !")  # la fonction print() affiche du texte à l'écran
```
Pour exécuter ce code, vous pouvez utiliser l'interpréteur Python en mode interactif. Ouvrez votre terminal et tapez python pour lancer l'interpréteur. Vous pouvez alors entrer chaque ligne de code individuellement et appuyer sur entrée pour l'exécuter :
```bash
$ python
Python 3.9.0 (default, Jan  5 2023, 14:59:48) 
[Clang 10.0.0 (clang-1000.11.45.5)] on darwin
Type "help", "copyright", "credits" or "license" for more information.
>>> # ce code est un commentaire, il est ignoré par l'interpréteur
>>> # pour écrire un commentaire, utilisez le caractère #
>>> 
>>> print("Bonjour tout le monde !")  # la fonction print() affiche du texte à l'écran
Bonjour tout le monde !
>>> 
```
Vous pouvez également enregistrer ce code dans un fichier, par exemple `mon_programme.py`, et l'exécuter en utilisant la commande `python mon_programme.py`. Le résultat sera le même que précédemment :
```bash
$ python mon_programme.py
Bonjour tout le monde ! 
```
## Les conditions
La structure conditionnelle `if`est une structure de base qu'on retrouve dans de nombreux langages de programmation. Cette condition va nous permettre d'exécuter un code si (et seulement si) une certaine condition est vérifiée. On va en fait passer une expression à cette condition qui va être évaluée par Python.
```python
# flux parent
if condition:
    #bloc d'instructions exécuté si la valeur de condition est True
else:
    #bloc d'instructions exécuté si la valeur de condition est False
#retour au  flux parent
```
### Les opérateurs de comparaison
Les opérateurs de comparaison en Python sont utilisés pour comparer des valeurs et renvoyer un résultat booléen (True ou False). Voici la liste des opérateurs de comparaison disponibles en Python :
* `==` : égal à
* `!=` : différent de
* `<` : strictement inférieur à
* `<=` : inférieur ou égal à
* `>` : strictement supérieur à
* `>=` : supérieur ou égal à
Voici quelques exemples d'utilisation des opérateurs de comparaison :
```python
x = 10
y = 20

print(x == y)  # False
print(x != y)  # True
print(x < y)   # True
print(x <= y)  # True
print(x > y)   # False
print(x >= y)  # False

s1 = "Bonjour"
s2 = "Bonjour"
s3 = "Salut"

print(s1 == s2)  # True
print(s1 != s3)  # True
print(s1 < s3)   # True
print(s1 <= s3)  # True
print(s1 > s3)   # False
print(s1 >= s3)  # False
```
Il est important de noter que les opérateurs de comparaison sont différents des opérateurs de calcul (`+`, `-`, `*`, `/`, etc.). Par exemple, l'expression `10 + 20` ne sera pas évaluée comme une comparaison, mais comme une opération de calcul qui renvoie la valeur 30.
## Les boucles
En programmation, les boucles servent à executer une ou plusieurs instructions plusieurs fois. En python il existe deux types de boucles.
### La boucle `while`
La boucle while permet d'executer une ou plusieurs instructions à la suite et s'arrête lorsque sa condition de départ est fausse. Voici un petit schéma pour vous donner un aperçu:
```python
while <condition>:
    <instructions>
```
Voici un exemple en cas réel, ce programme affiche les nombre allant de 1 à 30 puis s'arrête car la condition jour <= 30 n'est plus vraie après que jour soit égal à 31 :
```python
jour = 1
while jour <= 30:
    print(jour)
    jour = jour + 1 
```
> **Note**
> : Attention si vous n'actualiser pas la variable jour, ça risque de créer une boucle infinie. Si vous désirez en utiliser une, vous pouvez écrire `while True:`
### La boucle `for`
La boucle `for` en Python permet de répéter un bloc de code un nombre de fois déterminé. Voici un exemple de boucle for qui parcourt une séquence de nombres de 0 à 4 et affiche chaque nombre :
```python
for i in range(5):
    print(i)
```
Le résultat de ce code sera :
```bash
0
1
2
3
4
```
**Comment ça marche ?**

La boucle `for` en Python prend chaque valeur de la séquence une par une, et assigne cette valeur à la variable itérative (ici, `i`). Le bloc de code à l'intérieur de la boucle est alors exécuté pour chaque valeur de la séquence.

Dans l'exemple ci-dessus, nous avons utilisé la fonction `range(5)`, qui retourne une séquence de nombres de `0` à `4`. La boucle `for` parcourt cette séquence, et exécute le bloc de code (ici, l'instruction `print(i)`) pour chaque valeur de `i`.

Autres exemples de boucles for
Voici quelques autres exemples de boucles for avec différentes séquences :
```python
# Imprime les nombres de 1 à 5
for i in range(1, 6):
    print(i)

# Imprime les nombres pairs de 0 à 10
for i in range(0, 11, 2):
    print(i)

# Imprime les éléments d'une liste
fruits = ['pomme', 'banane', 'mangue']
for fruit in fruits:
    print(fruit)

# Imprime les caractères d'une chaîne de caractères
for caractere in "Bonjour":
    print(caractere)
```
Il est également possible de mettre une condition if dans une boucle for pour exécuter le bloc de code uniquement si la condition est vraie :
```python
# Imprime les nombres impairs de 0 à 10
for i in range(0, 11):
    if i % 2 == 1:
        print(i)
```
Il est également possible d'utiliser la fonction break pour sortir d'une boucle for avant la fin de la séquence, et la fonction continue pour passer à l'itération suivante sans exécuter le reste du code de l'itération en cours.
```python
# Cherche un nombre pair dans la séquence et sort de la boucle dès qu'il est trouvé
for i in range(0, 11):
    if i % 2 == 0:
        print("Trouvé :", i)
        break

# Ne traite pas les nombres pairs
for i in range(0, 11):
    if i % 2 == 0:
        continue
    print(i)
```


## Les principaux types de données

## Les tuples en Python
```python

```
## Les fonctions en Python
```python

```
