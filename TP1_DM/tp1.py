# import pandas as pd
# import numpy as np

# # 1.
# # pip install pandas

# # 2.
# import pandas as pd

# # 3.
# df = pd.read_csv("Housing.csv")

# # 4.
# print(df.head())

# # 5.
# print(df.shape)

# # 6.
# print(df.columns.tolist())

# # 7.
# print(df.dtypes)

# # 8.
# numeric_cols = df.select_dtypes(include=[np.number]).columns.tolist()
# categorical_cols = df.select_dtypes(include=['object']).columns.tolist()
# print(f"Numériques : {len(numeric_cols)}, Catégoriques : {len(categorical_cols)}")

# # 9.
# print(df.info())
# print(df.isnull().sum())

# # 10.
# print(df.describe())

# # 11.
# print(df[numeric_cols].quantile([0.25, 0.75]))

# # 12.
# print(f"Moyenne : {df['price'].mean()}")
# print(f"Médiane : {df['price'].median()}")

# # 13.
# for col in categorical_cols:
#     print(f"\n{col} :\n{df[col].value_counts()}")

# # 14.
# print(df.isnull().sum())

# # 15.
# if 'neighborhood' in df.columns:
#     print(df.groupby('neighborhood')['price'].mean().nlargest(5))
# else:
#     print("Colonne 'neighborhood' absente du dataset.")

# # 16.
# print(df.groupby('furnishingstatus')['price'].mean())

# # 17.
# print(df[df['airconditioning'] == 'yes']['price'].mean())
# print(df[df['basement'] == 'yes']['price'].mean())
# print(df[df['mainroad'] == 'yes']['price'].mean())

# # 18.
# print(df.groupby('stories')['price'].mean())

# # 

import numpy as np

# Profils des étudiants
A = np.array([85, 90, 12])
B = np.array([80, 85, 10])

# 1. Normes
norm_A = np.linalg.norm(A)
norm_B = np.linalg.norm(B)

# 2. Produit scalaire
dot_AB = np.dot(A, B)

# 3. Similarité cosinus
cosine_similarity = dot_AB / (norm_A * norm_B)

# Affichage des résultats
print("Norme de A :", norm_A)
print("Norme de B :", norm_B)
print("Produit scalaire A·B :", dot_AB)
print("Similarité cosinus :", cosine_similarity)


