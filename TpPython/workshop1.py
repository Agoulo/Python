conso=input("consommation energetique : ")
nombre_heure= input("insere le nombre d'heure : ")
consommation_total=int(conso) * int(nombre_heure)#int permet ici de converti l'energie
print(str(consommation_total) + "kw")
print(consommation_total, "kw")
print(f"{consommation_total} kw")
print("{} kw {}".format(consommation_total,conso))