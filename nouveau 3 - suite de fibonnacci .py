nbre_terms = int(input("Entrez un nombre: "))
 
n1 = 0
n2 = 1
 
print("la suite fibonacci est :")
print(n1,",", n2,end=",")
 
for i in range(2, nbre_terms):
  terms_suivant = n1 + n2
  print(terms_suivant, end=",")
 
  n1 = n2
  n2 = terms_suivant