import sys
base = set(sys.argv[1:])
recommandation = set()
fichier = open('commandes.txt', 'r')
for ligne in fichier :
	ensemble_produits = set(ligne.split()[1:])
	base.issubset(ensemble_produits) 
	for produit in ensemble_produits.difference(base) :
		recommandation.add(produit)
print(recommandation)
