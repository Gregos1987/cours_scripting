#chiffre = int(input())
#print(type (chiffre))
#if chiffre >= 0:
#    print("chiffre positif")
#else:
#    print("chiffre négatif")



#pour dire si la lettre entré est une voyelle ou une consonne

lettre = input()

voyelle = {"a","e","i","o","u","y"}

if lettre in voyelle:
    print("la lettre est une voyelle")
else:
    print("la lettre est une consonne")
    
    
    
#pour sortir le nombre le plus grand d'une liste    

def maxlist(list):
    return max(list)
print(maxlist([65,88,105,55,22,36]))



