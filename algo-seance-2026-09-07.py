# ===========================
# Implémentation en Python de quelques algorithmes vus lors de la séance du 7 septembre 2026 (1ère séance de l'année)
# ===========================


# En Python, on définit une fonction avec le mot-clé "def" (au lieu de "fonction" en pseudo-code), puis deux points ":"

# === Rappel : en Python, les listes sont numérotées à partir de l'indice zéro. Le premier élément d'une liste L est L[0]

# === Remarque : déclarer les types n'est pas obligatoire en Python, mais conseillé. J'essaierai de toujours le faire.
# Les types de base sont `int` pour les entiers, `float` pour les flottants (ce qui émule les réels, mais pas toujours bien), `bool`, `list` et quelques autres que l'on verra par la suite

# === Attention : les fonctions suivantes n'effectuent pas de tests sur les variables d'entrée.
# Par exemple, les fonctions pour Fibonacci(n) ne vérifient pas que "n" est bien un entier, et qu'il est positif.
# La raison est que ceci n'est pas un cours de développement informatique, c'est un cours d'algo.
# Si on voulait avoir un code plus sûr pour une utilisation réelle, on pourrait mettre des "assert" dans les fonctions, ou tout autre mécanisme de gestion des erreurs. Ce n'est pas le but ici.


def sommeRecursif(L:list[float]) -> float:
	if L == []:
		return 0
	return L[0] + sommeRecursif(L[1:])

# Rq : en Python, L[1:] est la liste extraite de L en ne prenant que les éléments à partir de l'indice 1 (donc en ne prenant pas l'élément en indice zéro)
# De même, L[3:] est la sous-liste obtenue en ne prenant que les termes à l'indice 3 et plus (donc à partir du 4ème élément de la liste, celui en indice 3.)

# Rq d'optimisation en Python (un peu plus hors-sujet pour ce qui nous intéresse) : `L[1:]` crée en fait une nouvelle liste, donc ceci est "lent"

# =====
# Tests
# =====

# Explication de la syntaxe de "assert" : 
# À chaque fois, si la condition après le `assert` n'est pas vérifiée, Python renverra une erreur.
# Si "rien ne se passe", cela signifie que les tests ont réussi et que tout va bien

assert sommeRecursif([]) == 0
assert sommeRecursif([0]) == 0
assert sommeRecursif([3.14]) == 3.14
assert sommeRecursif([0,-2,0,2,0]) == 0
assert sommeRecursif([0,1,0,-3,57.6,0,0]) == 55.6
print("Tests réussis pour la somme en récursif !")



# La somme en itératif, avec une boucle for :

def sommeIteratif(L: list[float]) -> float:
	s = 0
	n = len(L)
	for k in range(n):
		s = s + L[k]
	return s

# Rq : on écrit les boucles "de base" : on n'utilisera pas les raccourcis Python comme "for x in L", qui n'existent pas forcément dans d'autres langages.

# Les mêmes tests : 

assert sommeIteratif([]) == 0
assert sommeIteratif([0]) == 0
assert sommeIteratif([3.14]) == 3.14
assert sommeIteratif([0,-2,0,2,0]) == 0
assert sommeIteratif([0,1,0,-3,57.6,0,0]) == 55.6
print("Tests réussis pour la somme en itératif !")

# === Attention aux flottants !
# Ne **PAS** tester si sommeIteratif([0.1,0.2]) == 0.3 !!! 
# Il y aurait une erreur due non pas à une erreur dans l'algo de somme, mais due aux approximations sur les flottants.


# ================
# Fibonacci
# ================


def FibonacciRecursif(n: int) -> int:
	if n <= 1:
		return n
	return FibonacciRecursif(n-1) + FibonacciRecursif(n-2)



def FibonacciIteratif1(n: int) -> int:
	# liste qui va contenir tous les nombres de Fibonacci de 0 à n:
	# on préremplit les deux termes initiaux
	F = [0,1]
	# attention, la borne de fin est exclue en Python !
	# mathématiquement, ceci est une boucle de i= 2 à n
	# en pseudo code, il faudra écrire "Pour i allant de 2 à n : "
	for i in range(2,n+1):
		F.append(F[i-1] + F[i-2])
		# alternative : concaténer avec F = F + [F[i-1] + F[i-2]]
		# note : en Python, F[i]=F[i-1] + F[i-2] provoquera une erreur car F[i] n'existe pas encore
	return F[n]


# l'implémentation suivante n'est pas plus rapide, mais elle est plus économe en mémoire car elle ne garde pas en mémoire tous les nombres de Fibonacci, juste les deux derniers à chaque étape
def FibonacciIteratif2(n: int) -> int:
	if n <= 1:
		return n
	a, b = 0, 1
	for i in range(2,n+1):
		a, b = b, a+b
	return b


# Affichage de quelques valeurs :  
for k in range(100):
	print(FibonacciIteratif2(k))

# Ceci devrait donner les 100 nombres (jusqu'à F_{99}, donc) de façon quasi-immédiate. (0,1s sur mon ordi qui date de 2020)
# N'essayez surtout pas ceci avec Fibonacci récursif, vous planterez vraisemblablement votre machine.
# Même avec 40 au lieu de 100, l'algorithme récursif va effectuer des millions d'appels récursif. 
# Exercice : combien de millions ?

# =====================
# Suggestion de travail sur le contenu de ce document : 
# - chronométrez la vitesse de ces algorithmes
# - tracez les graphes de la vitesse d'exécution de Fibonacci(n) en fonction de n : est-ce que ça semble linéaire ? Pour lesquels de ces algorithmes ?

# N'oubliez pas non plus de regarder les exercices de la feuille de TD distribuée.

