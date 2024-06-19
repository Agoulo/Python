capacite_batteries = float(input("Saisissez la capacité des batteries de secours : "))
consommation_energetique = float(input("Saisissez la consommation energetique du data center/heure : "))

temp_restant = capacite_batteries / consommation_energetique

temp_restant_heures = int(temp_restant)

temp_restant_minutes = int((temp_restant - temp_restant_heures)*60)

print(f"le data center peut fonctionner pendant {temp_restant_heures} heures et {temp_restant_minutes} minutes uniquement sur les batteries de secours")