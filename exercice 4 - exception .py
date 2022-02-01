x = input('entrer la valeur x :')

if (type(x) == str) :
    print (" Il est impossible de saisir une chaine de caractére")
    print (" veuillez saisir des valeurs numérique")
    while (type(x)== str):
        x = int(input('Entrez une valeur numérique pour x ='))
elif (type(x) == complex) : 
    print (" Nous ne pouvons pas choiri un nombre complexe")
    while (type(x) == complex) :     
        x = int(input(" Veuillez saisir un nombre numérique pour x"))
elif (x < 0) :
    print (" nous ne pouvons pas choisir un numéro négatif")
    while (x<0):
        x = int(input("veuillez entrer un nombre positif pour x ")) 
elif (len(str(x)) > 3) :
    print (" Nous ne pouvons pas choisir un nombre trop grand")
    while len(str(x) > 3):
        x = int(input("LA valeur que vous avez tapez est supérieur à 3 unités"))
elif (len(str(x)) < 1) :
    while len(str(x) < 1):
        x = int(input("la valeur que vous avez taper est inférieur à 1 "))

polynome = x**3 - 1.5 * x**2 -6*x +5 


print(polynome)


    