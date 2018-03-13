etudiants = [
    {'nom': 'Dupont', 'promo': 'M1'},
    {'nom': 'Durand', 'promo': 'M2'},
    {'nom': 'Dupontel', 'promo': 'M1'},
    {'nom': 'Antoine', 'promo': 'M2'},
]

etudiants_m1 = [e['nom'] for e in etudiants if e['promo'] == 'M1']
etudiants_m2 = [e['nom'] for e in etudiants if e['promo'] == 'M2']

print("Inscrits en M1 :", etudiants_m1)
print("Inscrits en M2 :", etudiants_m2)
