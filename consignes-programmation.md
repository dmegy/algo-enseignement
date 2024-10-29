Consignes / conseils de programmation
=================

Table des matières : 
- tests
- gestion des erreurs
- autres conseils

Tests
---

En TP ou chez soi lorsqu'on travaille sur le cours, il est nécessaire de tester les fonctions que l'on écrit, à l'aide d'un jeu de tests.

Pour ne pas avoir à tester à la main un grand nombre de fois à chaque petite modification, on peut utiliser une fonction dédiée dont le seul objectif est de tester un algorithme dans plusieurs configurations "classiques".

Il est même conseillé de commencer par écrire le jeu de tests avant même d'écrire la fonction qui sera testée, cela aide à réflechir et à isoler tous les cas particuliers à gérer.

Par exemple, s'il est demandé une fonction moyenne(L) qui prend en entrée une liste non vide de nombres, et qui renvoie la moyenne des valeurs, alors on peut commencer par écrire les tests, puis ensuite écrire la fonction et la tester.
On peut tester à l'aide du mot-clef 'assert', par exemple, de la façon suivante.

```python
def test_moyenne():
	assert moyenne([0]) == 0, "pb avec zéro"
	assert moyenne([2.7]) == 2.7, "pb avec un décimal positif"
	assert moyenne([1/3]) == 1/3, "pb avec un rationnel positif"
	assert moyenne([-3]) == -3, "pb avec un entier négatif"
	assert moyenne([-3,3]) == 0, "pb avec deux valeurs opposées"
	assert moyenne([6,7]) == 6.5, "pb avec [6,7]"
	assert moyenne([1,3,4]) == 8/3, "pb avec [1,3,4]"
	assert moyenne([1,-2]) == -0.5, "pb avec [1,-2]"
	assert moyenne([6,7,8,9,10]) == 8, "pb avec [6,7,8,9,10]"
	print("Test réussis")

def moyenne(L: list) -> float:
	# maintenant, on écrit le code
```

Pour de plus grands projets, il existe des modules spécialisés pour tester tout le code d'un grand nombre de manières en couvrant tous les cas de figure, y compris avec des tests aléatoires.


Gestion des erreurs
---

Dans cette UE, lorsque l'on écrit un algorithme en pseudo-code (ou en Python), on ne s'occupera *pas* de gérer les erreurs.
Les fonctions sont supposées recevoir un objet d'un certain type, et on supposera toujours que l'argument est du bon type.

Exemple : si un énoncé demande d'écrire une fonction qui prend une liste non vide de nombres et renvoie la moyenne des valeurs, il est attendu quelque chose du genre : 

```python
def moyenne(L: list) -> float:
	somme = 0
	for i in range(len(L)):
		somme += L[i]
	return somme/len(L)
```

Si l'on fournit une liste vide, ou autre chose qu'une liste (par exemple un nombre), Python affichera une erreur de toute façon, pas besoin de prévoir un message d'erreur spécifique dans le code lui-même.

Remarque : dans certaines situations, si l'on a vraiment du mal à débugguer un code, on peut rajouter des tests à l'aide du mot-clef "assert" :

```python
def moyenne(L: list) -> float:
	assert isinstance(L,list), "L'entrée du mauvais type. Type attendu : liste"
	assert len(L) != 0, "La liste en entrée est vide."
	somme = 0
	for i in range(len(L)):
		assert isinstance(L[i],(int,float)), "L[i] doit être un entier ou flottant"
		somme += L[i]
	return somme/len(L)
```

L'exemple n'est pas forcément très bon, mais c'est pour illustrer. 

Dans tous les cas, en conditions d'examen, on n'écrira *pas* de telles vérifications.

Dernières remarques : pour la fonction de moyenne, Python permet d'itérer de manière plus élégante sur les objets d'une liste comme ceci :

```python
def moyenne(L: list) -> float:
	somme = 0
	for valeur in L:
		somme += valeur
	return somme/len(L)
```
En réalité, Python propose dispose d'une fonction somme intégrée donc on pourrait simplement écrire :

```python
def moyenne(L: list) -> float:
	return sum(L)/len(L)
```





Conseils pour améliorer la clarté du code
---

- Donner des noms compréhensibles et explicites aux variables autant que possible, éviter les noms de variable à une lettre (à part pour des compteurs de boucle)
- éviter d'imbriquer trop de "ifs", surtout lorsqu'il s'agit de traiter à part un cas particulier.