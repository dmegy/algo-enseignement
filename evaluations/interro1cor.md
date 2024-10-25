Correction de l'interrogation 1
===

On donne des corrections en Python au lieu de pseudo-code, ça permet d'executer et tester le code ou des variations.

Rappel : on n'a pas à gérer les erreurs : les fonctions sont supposées recevoir un argument du bon type.

Exercice 1 (calcul de factorielle)
---

1) Factorielle, algorithme itératif : 


```python
def factorielle(n):
	result = 1
	for i in range(1, n+1): 
		result = result * i
	return result
```

Preuve de terminaison : 
La boucle 'for' tourne exactement $n$ fois.

Preuve de correction : 
Si $n=0$, la fonction ne rentre pas dans la boucle et renvoie $1$ ce qui est bien égal à $0!$. On suppose maintenant $n\geq 1$. 
Notons, pour $i \in [[1,n]]$, $r_i$ la valeur de la variable ```result``` à  la fin de la boucle d'indice $i$.
Prouvons que pour tout $i \in [[1,n]]$, $r_i = i!$. On le fait par récurrence sur $i$.
- Initialisation :  On a bien $r_1=1$.
- Hérédité : Soit $i \in [[1,n-1]]$. Suposons que $r_i = i!$. Montrons que $r_{i+1} = (i+1)!$. L'instruction dans la boucle implique $r_{i+1} = r_i \times  (i+1)$, donc en utilisant l'hypothèse de récurrence, on a bien $r_{i+1} = (i+1)!$.

Ceci termine la récurrence.
Conclusion : à la fin de la dernière boucle, c'est-à-dire de la boucle d'indice $n$, on a $r_n = n!$.

Remarque : on peut aussi utiliser une boucle 'while', ascendante ou bien descendante, par exemple : 
```python
def factorielle(n):
	result = 1
	while n > 0: # ou n>1
		result = result * n
		n = n - 1
	return n
```
Bien sûr, la justification est alors différente. 
Si l'on exclut le cas $n=0$, on peut par exemple noter $r_i$ la valeur de la variable result à la fin de la boucle indéxée par $i$, c'est-à-dire la boucle au début de laquelle la variable n vaut $i$. On a donc $r_n = n$, $r_{n-1}=n(n-1)$ etc et en général, pour $j\geq 1$, on a $r_i = \prod_{j=i}^n j$. On le montre par récurrence descendante sur $j$.
On conclut en remarquant que la valeur retournée est $r_1 = n!$.


2) Factorielle, algorithme récursif : 

```python
def factorielleR(n):
	if n < 1: # on pourrait écrire n==0, ou n<2
		return 1 
	return n * factorielleR(n-1)
```

Preuve de terminaison:
- version 1 : les appels récursifs sont faits sur des entiers diminuant strictement, donc $<1$ en temps fini, moment où la récursivité prend fin.
- version 2 : lorsque l'on appelle factorielleR(n), il y a au total exactement $n+1$ appels de la fonction (et donc l'algorithme termine). Preuve par récurrence, laissé en exo.

Preuve de correction:
Pour $n\in\mathbb N$, notons $A(n)$ l'assertion: « factorielleR(n) retourne $n!$. »
Montrons $\forall n\in\mathbb N, A(n)$, par récurrence sur $n$.

- Initialisation : $A(0)$ est vraie car factorielleR(0) renvoie bien $1$.
- Hérédité :  Soit $n\in \mathbb N$. Supposons $A(n)$. Montrons $A(n+1)$. Comme $n+1 >=1$, la fonction factorielleR(n+1) ne rentre pas dans le 'if' et retourne le produit de $n+1$ par factorielleR(n), qui vaut $n!$ par hypothèse de récurrence. Ceci montre bien $A(n+1)$.



Exercice 2 (minimum de liste)
---

Attention, la liste en entrée est non vide par hypothèse.

1) Minimum de liste, algorithme itératif :

```python
def minimumListeIteratif(L): # liste non vide
	m = L[0] # valeur provisoire, destiné à contenir le minimum
	n = len(L)
	for k in range(1,n):
		if L[k] < m:
			m = L[k]
	return m
```

Preuve de terminaison : 
Boucle "for" de longueur n.

Preuve de correction :
Notons $m_0$ la valeur de $L[0]$ et pour $k in [[0,n-1]]$, notons $m_k$ la valeur de la variable m en fin de boucle d'indice $k$. Notons $P(k)$ l'assertion «  $m_k$ est le minimum des $k+1$ premiers termes de la liste L. »
Prouvons $P(k)$ pour tout $k$ de $0$ à $n-1$, par récurrence.

- Initialisation à $k=0$ : $m_0$ est bien le minimum des valeurs parmi la première valeur.
- Hérédité : soit $k \in [[0,n-2]]$. Supposons $P(k)$. Montrons $P(k+1)$.
Dans la boucle, on teste si $L[k+1] < m_k$ et si oui, $m_{k+1}=L[k+1]$. Sinon, $m_{k+1}=m_k$.
Dans les deux cas, en fin de boucle, $m_{k+1}$ contient bien le minimum des $k+2$ premières valeurs.



2) Minimum de liste, algorithme récursif :

```python
def minimumListeRecursif(L):
	if len(L) == 1:
		return L[0]
	return min(L[0],minimumListeRecursif(L[1:]))
```

Preuve de terminaison :
Version 1 : l'appel récursif se fait sur une liste de longueur n-1. La longueur finit donc par atteindre 1, moment où la récursivité prend fin.
Version 2 : on peut montrer par récurrence que pour une liste de longueur $n$, il y aura $n$ appels à la fonction en tout, en comptant le premier appel. (Laissé en exercice.)

Preuve de correction:
Pour $k \in \mathbb N^*$, notons $P(k)$ l'assertion « pour une liste L de longueur $k$, la fonction renvoie la valeur minimale de la liste. »
Montrons $\forall k\in \mathbb N^*, P(k)$ par récurrence sur $k$.
- Initialisation : La fonction fournit le bon résultat pour une liste de longeur un.
- Hérédité :  Soit $k\in \mathbb N^*$. Supposons $P(k)$. Montrons $P(k+1)$. Soit L une liste de longueur $k+1$. ALors L[1:] est une liste de longueur $k$ donc minimumListeR(L[1:]) renvoie le minimum des $k$ dernières valeurs par hypothèse de récurrence.
La fonction renvoie alors le minimum de L[0] et du minimum du reste, donc le minimum de toutes les valeurs.


Exercice 3
---

Fonction prenant un entier naturel et retournant la liste de ses chiffres en base $10$.

```python
def chiffresBase10(n: int) -> list:
	if n<10:
		return [n]
	return chiffresBase10(n//10) + [n % 10]

```

Preuve de terminaison : 
Les appels récursifs se font avec des valeurs strictement décroissantes, donc <10 à partir d'un moment. La récursion s'arrète à ce moment.

Preuve de correction : 
Pour $k>0$, notons $P(k)$ l'assertion "si $n$ est un entier à $k$ chiffres, chiffresBase10(n) renvoie la liste des chiffres de son écriture décimale."
- Initialisation : P(1) est vraie
- Hérédité : Soit $k>0$ et supposons $P(k)$ vraie. Soit $n$ entier à $k+1$ chiffres, c'est-à-dire $10^{k} \leq n < 10^{k+1}$. Alors $n//10$ est un entier à $k$ chiffres, et ce sont les $k$ premiers chiffres en base $10$ de $n$ (car n = 10(n//10)+(n%10)). Par ailleurs n%10 est le dernier chiffre.



```python
def chiffres(n: int) -> list: #
	L=[]
	while n>10:
		L = [n%10] +L  
		n = n // 10
	L = [n] + L
	return L
```



Exercice 4 : est un carré
---

```python
def est_un_carre(chaine: str) -> bool:
	if len(chaine) % 2 != 0:
		return False

	milieu = len(chaine) / 2
	for i in range(milieu):
		if chaine[i] != chaine[milieu+i]:
			return False
	return True
```

Evidemment, on aurait pu 'tricher' et écrire :

```python
def est_un_carre(s : str) -> bool:
	m = len(s) // 2
	return s[:m] == s[m:]
```
Mais ce n'était pas le principe de l'exercice.


Exercice 5 : contient un carré
---

```python
def contient_un_carre(s: str) -> bool:
	n = len(s)
	for i in range(n):
		for j in range(i+1, n+1):
			if est_un_carre(s[i:j]):
				return True
	return False
```

- Preuve de terminaison : les boucles for terminent en moins de $n$ étapes.
- Preuve de correction : il s'agit de montrer qu'on teste bien toutes les sous-chaînes non vides de s. La double boucle parcourt tous les couples (i,j) avec 0 <= i < j <= n, suite à quoi on teste la sous-chaîne s[i:j] donc des indices i à j-1 (donc jamais une sous-chaîne vide).
On teste donc bien toutes les sous-chaînes non-vides.

Optimisations possibles (non nécessaires) : on pourrait écrire ```for j in range(i+2, n+1)``` car une chaîne de longueur 1 ne sera jamais un carré. Dans le même ordre d'idées, on pourrait aussi utiliser la possibilité qu'offre Python d'incrémenter l'indice de 2 et non 1 dans la deuxième boucle, pour ne tester que les sous-chaînes de longueur paire : ```for j in range(i+2, n+1, 2)```.

Exercice 6 Triplets pythagoriciens
---


```python
def pythagore(N : int):
	L=[]
	for c in range(1,N+1):
		for b in range(1,c+1):
			for a in range(1,b+1):
				if a**2 + b**2 == c**2:
					L = L + [[a,b,c]]
	return L

```
Par exemple pour N=20, on trouve six triplets : 
[[3, 4, 5], [6, 8, 10], [5, 12, 13], [9, 12, 15], [8, 15, 17], [12, 16, 20]]

Optimisations possibles : 
- ```L.append([a,b,c])```est plus rapide que ```L = L + [[a,b,c]]```.
- Un triplet pythagoricien est formé d'entiers distincts : en effet, si deux entiers étaient égaux, le triplet correspondrait à un triangle isocèle rectangle, mais un tel triangle va alors vérifier $a=b=c\sqrt{2}$, les trois côtés ne peuvent être entiers, contradiction.
On peut donc améliorer (très) légèrement la boucle pour ne tester que des triplets $(a,b,c)$ vérifiant $1\leq a<b<c\leq N$.
Autrement dit, on peut faire commencer $b$ à $2$ et $c$ à $3$.


Suggestion de travail personnel d'approfondissement
---

Lire des choses sur les triplets pythagoriciens, c'est de la culture gé mathématique de base qui vous servira toujours et c'est exploitable de très nombreuses manières par un enseignant.

