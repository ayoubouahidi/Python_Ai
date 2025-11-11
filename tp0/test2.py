h_travailer = int(input('entrer le nombre d\'heure : '))
t_horaire = float(input('entrer le taux d\'heure : '))


if h_travailer > 40 :
    h_supl =h_travailer - 40
else :
    h_supl = 0

salaire_b = (40 * t_horaire) + (h_supl * t_horaire * 1.5)
print(salaire_b)