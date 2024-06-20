reponse_utilisateur = input("le serveur est-il en maintenance ? (oui/non) : ") == "oui"
message = "serveur marche" if reponse_utilisateur == true else "serveur en maintenance"
print(message)

Maintenance = input("le serveur est-il en maintenance :")
Maintenance = Maintenance.lower()
Maint = bool(Maintenance == "oui")
print(f"le serveur est en maintenance :{Maint}")
