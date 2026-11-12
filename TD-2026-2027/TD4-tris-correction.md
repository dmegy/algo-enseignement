# Feuille TD 4 : tris

Ce document  fournit les implémentations Python des algorithmes de la feuille 4. Il ne contient pas les preuves mathématiques (terminaison, correction).

**Avertissement important** : cette UE est une UE d'algo, pas de Python. Les corrections des algorithmes sont données en Python simplement pour vous habituer à la syntaxe, et pour que vous puissiez faire tourner les programmes, ce qui peut avoir un effet bénéfique (essayer concrètement une fonction sur plusieurs listes etc).
Cependant, il y a certaines particularités du langage Python qui rendent certains codes inefficaces, ou qui ajoutent des effets inattendus, non visibles directement dans le code si on ne connaît pas les spécificités de Python par rapport à d'autres langages.
Ces détails sont ignorés dans cette UE : seule l'algorithmique compte. Mais j'ai tout de même laissé des remarques pour vous mettre en garde, pour celles et ceux qui sont un peu plus intéressés par Python lui-même.

## Exercice 1 : test de croissance

Première version, itérative :

```Python

# D'abord, la fonction de test, qui va servir à tester l'implémentation.
# Prenez l'habitude de tester systématiquement votre code et vos algorithmes, à l'ordi ou "à la main".
# Écrire les tests avant d'écrire la fonction peut faire gagner du temps, ça permet d'avoir en tête les cas limite.
# Dans les questions suivantes, je n'écris plus les tests, mais faites-le lorsque vous vous exercez.
def test_est_croissante() :
	assert(est_croissante([]))
	assert(est_croissante([1]))
	assert(est_croissante([-.3]))
	assert(est_croissante([1,1]))
	assert(est_croissante([-2,8,12.3]))
	assert(not est_croissante([1,0,3,4]))
	assert(not est_croissante([1,3,4,2]))
	print("Tests réussis")

def est_croissante(L) :
	for k in range(len(L)-1) :
		if L[k]>L[k+1]: return False
	return True
```

Autre version, récursive :

```Python
def est_croissante(L) :
	if len(L) <= 1 : return True
	return L[0] <= L[1] and est_croissante(L[1:])
```

**Remarque Extra-mathématique** : une particularité de Python est qu'au moment d'évaluer le booléen `L[0] <= L[1] and est_croissante(L[1:])`, Python commence d'abord par évaluer `L[0] <= L[1]` et si c'est faux, il ne prend pas la peine d'évaluer le reste, il renvoie `False` tout de suite. Ceci fait gagner du temps et économise en pratique des appels récursifs.
Un peu comme si on avait écrit :
```Python
	if L[0] > L[1] :
		return False
	return est_croissante(L[1:])
```



## Exercice 2: tri bulle

```Python
def tri_bulle(L) :
	for i in range(len(L)-1) :
		for j in range(len(L)-i-1) :
			if L[j] > L[j+1] :
				L[j],L[j+1] = L[j+1],L[j]
	return L
```

**Remarque extra-mathématique** : en Python, la fonction va recevoir L _par référence_. Par conséquent,  en plus de renvoyer la liste triée, cette fonction modifie aussi la liste L elle-même ...ce qui peut surprendre si on ne s'y attend pas. Si on veut une implémentation Python sans "effet de bord", il faudrait par exemple, dans la fonction, commencer par copier les valeurs avec `M = L.copy()`, travailler sur `M` et renvoyer `M`.

## Exercice 3 : fusion de listes triées (et tri fusion en bonus)

```Python
def fusion(L,M) :
	i,j = 0,0
	F = []
	while i < len(L) and j < len(M) :
		if L[i] <= M[j] :
			F.append(L[i])
			i = i+1
		else :
			F.append(M[j])
			j = j+1
	F = F + L[i:] + M[j:]
	return F

# BONUS : le tri fusion avec la fonction précédente :

def tri_fusion(L) :
	if len(L) <= 1 :
		return L
	coupure = len(L)//2
	return fusion( tri_fusion(L[:coupure]) , tri_fusion(L[coupure:]) )
```



**Remarque extra-mathématique** : Cet algorithme est du type "diviser pour régner". En théorie, il est bien plus efficace que le tri bulle. Cependant, la façon dont Python extrait les sous-listes `L[:coupure]`et `L[coupure:]` annule en fait ce gain d'efficacité, il faudrait implémenter l'algorithme en Python d'une façon un peu différente. Ce sont des détails d'implémentation spécifiques à Python, ça ne nous intéresse pas ici, seul compte le principe général.

## Exercice 4 : tri pivot (plutôt appelé "tri rapide")

L'algorithme prend en entrée une liste non vide $L$. Notons $p$ sa dernière valeur, que l'on appelle le pivot.

L'algorithme renvoie une liste $L'$ contenant les mêmes valeurs que $L$ dans un ordre a priori différent. Si $k$ est un entier tel que $L'[k]=p$, alors $\forall i<k, L'[i]< L'[k]$ et $\forall i>k, L'[i]\geq L'[k]$.

**Bonus** : l'implémentation du «tri tri rapide en adaptant cette fonction de partition à partir d'un pivot:

```Python
def tri_rapide(L):
	n = len(L)
	if n <= 1 :
		return L
	pivot = L[n-1]
	k = 0
	for i in range(n-1) :
		if L[i] < pivot:
			L[k],L[i] = L[i],L[k]
			k = k+1
	L[k],L[n-1] = L[n-1],L[k]
	L[:k] = tri_rapide(L[:k])
	L[k+1:] = tri_rapide(L[k+1:])
	return L
```

**Remarque extra-mathématique** : même problème que précédemment avec l'extraction de sous-listes `L[:k]` et `L[k+1:]` en Python, qui en pratique ralentit l'algorithme.

Ce qui compte ici, c'est de comprendre le principe mathématique : on place la valeur `pivot` à sa place (indice k), après quoi les valeurs pour les indices inférieurs à `k`sont inférieures à `pivot`, et les valeurs d'indice supérieur à `k` sont supérieures à `pivot`. Après quoi, on recommence sur les listes extraites correspondant aux indices $<k$ et $>k$.

Les remarques sur tel ou tel comportement de Python ne sont pas à apprendre dans le cadre de cette UE. Ce qui compte, c'est l'algorithme abstrait.



