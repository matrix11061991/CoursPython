# Nombres premiers (Utilisation de la boucle for... in...) - Rappel
Écrire une fonction 𝑝𝑟𝑒𝑚𝑖𝑒𝑟(𝑛) en langage python qui affiche si un nombre est premier ou pas
```python
def premier(n):
    if n < 2:
        return False
    for i in range(2, n-1):
        if n % i == 0:
            return False
    return True

print(premier(17))

```
ou encore:
```python
def premier(n):
    return n > 1 and all(n % i != 0 for i in range(2, int(n**0.5) + 1))
```
