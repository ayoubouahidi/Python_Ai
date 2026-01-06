def puissance(a, b):
    if (b == 1 ):
        return a * b
    return  a * puissance(a, b - 1)

print(puissance(3, 3))

def factorielle(a):
    if (a == 1) :
        return a
    return  a * factorielle(a -1)


print(factorielle(3))

def fibomacci(n):
    if (n < 2):
        return 1
    return fibomacci(n - 1) + fibomacci(n - 2)
print(3)

def PGCD(a, b):
    if (b == 0):
        return a
    return PGCD(b, a % b)

print("*** PGCD *** : ", PGCD(6, 3))

# def somme_list(list_des_nbr):
    
def somme_chiffre(n):
    if (n == 0):
        return n
    return n % 10  + somme_chiffre(n // 10)
print("*** Somme chiffre *** : ", somme_chiffre(123))

D = {'nom': 'Dupuis', 'prenom': 'Jacque', 'age': 30}

D['prenom'] = 'Jacques'

print("Clés :", list(D.keys()))

print("Valeurs :", list(D.values()))

print("Paires clé/valeur :", list(D.items()))

print(f"{D['prenom']} {D['nom']} a {D['age']} ans")


def total_ventes(ventes):
    return sum(ventes.values())

def meilleur_vendeur(ventes):
    return max(ventes, key=ventes.get)

Ventes = {"Dupont":14, "Hervy":19, "Geoffroy":15, "Layce":21}

print("Total des ventes :", total_ventes(Ventes))
print("Meilleur vendeur :", meilleur_vendeur(Ventes))


import seaborn as sns
import matplotlib.pyplot as plt
data = {
    'Étudiant': ['Ali', 'Sara', 'Omar', 'Lina', 'Yassine'],
    'Python': [15, 18, 10, 13, 9],
    'Maths': [14, 16, 12, 15, 11]
}
df = pd.DataFrame(data)
df.head()
print("Moyenne en Python :", df['Python'].mean())
print("Moyenne en Maths  :", df['Maths'].mean())
df['Moyenne'] = df[['Python', 'Maths']].mean(axis=1)
print(df)
sns.barplot(x='Étudiant', y='Moyenne', data=df)
plt.title("Moyenne des étudiants")
plt.show()


import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

data = {
    "Étudiant": ["Ali", "Sara", "Omar", "Lina", "Yassine"],
    "Python": [15, 18, 10, 13, 9],
    "Maths": [14, 16, 12, 15, 11]
}

df = pd.DataFrame(data)


print("DataFrame :")
print(df)


print("\nLes 5 premières lignes du DataFrame :")
print(df.head())

print("\nMoyenne des notes en Python :")
print(df["Python"].mean())

print("\nMoyenne des notes en Maths :")
print(df["Maths"].mean())


df["Moyenne"] = (df["Python"] + df["Maths"]) / 2

print("\nDataFrame avec la colonne Moyenne :")
print(df)


sns.barplot(x="Étudiant", y="Moyenne", data=df)

plt.title("Moyenne des notes par étudiant")
plt.xlabel("Étudiant")
plt.ylabel("Note moyenne")

plt.show()