import pandas as pd
import numpy as np

df = pd.DataFrame({
    'Âge':          [25, None, 30, 45, 22],
    'Salaire (MAD)': [5000, 7000, np.nan, np.nan, 4500],
    'Ville':        ['Casablanca', 'Rabat', 'Fès', 'Marrakech', 'Agadir']
})


print(df.isnull())
print(df.isnull().sum())

print(f"Nombre total de valeurs manquantes : {df.isnull().sum().sum()}")
print(f"Colonnes incomplètes : {df.columns[df.isnull().any()].tolist()}")

import pandas as pd
import numpy as np

data = {
    "Âge": [25, 30, np.nan, 40, None],
    "Salaire": [3000, None, 2500, 4000, 3500],
    "Ville": ["Paris", "Lyon", "Marseille", None, "Toulouse"]
}
df = pd.DataFrame(data)

print("✅ Données initiales :")
print(df)

# 3. Supprimer les lignes incomplètes
df_clean = df.dropna()

# 4. Afficher le nombre de lignes avant et après
print("\nNombre de lignes avant suppression :", len(df))
print("Nombre de lignes après suppression :", len(df_clean))

# 5. Comparer l’impact
print("\n✅ Données nettoyées :")
print(df_clean)



# exercice 3 
 
df = pd.DataFrame({
    'Salaire original': [5000, 7000, None, 10000, None]
})
 
print("=== DataFrame original ===")
print(df)
 
# Imputation par la moyenne
imputer_mean = SimpleImputer(strategy='mean')
df['Salaire imputé (moyenne)'] = imputer_mean.fit_transform(df[['Salaire original']])
 
# Imputation par la médiane
imputer_median = SimpleImputer(strategy='median')
df['Salaire imputé (médiane)'] = imputer_median.fit_transform(df[['Salaire original']])
 
print(f"\nMoyenne calculée  : {df['Salaire original'].mean():.2f} MAD")
print(f"Médiane calculée  : {df['Salaire original'].median():.2f} MAD")
 
print("\n=== Résultat final ===")
print(df)
 

#   exercice 4 
