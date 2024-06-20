#Concatenation de chaines :


str1= "chaine1"
str2= "chaine2"
print(str1 + str2)
str3=  str1 + " " + str2
print(str3)
age = 45
mon_message="voici mon age: "
print(mon_message + str(age))

prenom = "Goulo"
message_prenom ="je m'appelle {0} et j'ai {1} ans".format(prenom,age)
print(message_prenom)
#message_prenom ="je m'appelle {prenom} et j'ai {age} ans".format(prenom,age)
print(message_prenom)


var1 = 12
print("{0:2d} {1:3d} {2:4d}".format(var1, var1**2, var1**3))

#            01234567
ma_chaine = "abcdefgh"

# affiche lettre à la position 0
print(ma_chaine[0])

# affiche lettre à la position 3
print(ma_chaine[3])


# debut à 2 jusqu'à la 5 (exclue)
print(ma_chaine[2:5])

# debut à 0 jusqu'à la 5 (exclue)
print(ma_chaine[:5])

# debut à 1 jusqu'à la fin
print(ma_chaine[1:])

# chaine[<debut>:<fin>:<pas>]
print(ma_chaine[1:7:2])

# retour à la ligne :
print("Hello\ntout\nle monde")

# tabulation :
print("Hello\ttout\tle monde")

# Echappe pour " " : 
print("Hello tout \"le monde\" ")

