mon_age = int(input("quel age avez-vous ?"))
if mon_age >= 21:
    print("vous etes majeur aux USA")

elif(mon_age >= 18):
    print("vous etes majeur en france")
    
else:
    print("vous etes mineur")


    is_admin = True
    if(mon_age >= 18 and is_admin):
        print("vous etes majeur et admin")


    jour = int(input("le numero d'un jour de la semaine :"))

    match  jour:                        #permet de faire la verification du jours
        case 1:
            print("Lundi")
        case  2:
            print("Mardi")
        case 3:
            print("Mercredi")
        case 4:
            print("Jeudi")
        case 5:
            print("Vendredi")
