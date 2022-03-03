import sys
clients = set()
for ligne in sys.stdin:
	client = ligne.split()[0]
	clients.add(client)
print('*****************************************')
print("le nombre de clients differents" , len(clients))



    
grand_nombre_commande = 0
produits = set()
fichier = open('commandes.txt', 'r')
for  ligne in fichier:
    unused, *liste_produit = ligne.split()[1:]
    if len (liste_produit) > grand_nombre_commande :
        grand_nombre_commande = len (liste_produit)
        plus_gross_commande = liste_produit
    
    for produit in liste_produit:
            produits.add(produit)
            
print('*****************************************')
print("nb produits", len(produits))
print('*****************************************')
print("plus grosse commande", plus_gross_commande)

	