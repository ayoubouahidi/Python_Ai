# import pandas as pd
# import seaborn as sns
# import matplotlib.pyplot as plt

# dataset = pd.read_excel("dataset.xlsx")
# df = dataset.copy()
# print(df.head())
# # print("Shape :", df.shape)
# # print(df.dtypes.value_counts())

# sns.heatmap(df.isna(), cbar=False)
# # plt.show()

# nan_percent = df.isna().mean() * 100
# print(nan_percent)

# df = df.dropna(thresh=len(df)*0.1, axis=1)

# print("nouveau shape :", df.shape)
# target_counts = df["SARS-Cov-2 exam result"].value_counts(normalize=True) * 100
# print("******* target ******* :", target_counts)


# # ex 04


# float_cols = df.select_dtypes(include='float').columns
# object_cols = df.select_dtypes(include='object').columns

# print("Variables sanguines :", float_cols)
# print("Variables virales :", object_cols)


# print("***********" * 3)



# # for col in float_cols:   
# #     plt.figure(figsize=(6,4))
# #     sns.distplot(df[col], kde=True, bins=30)   
# #     plt.title(f"Distribution de {col}")
# #     plt.show()




# # Liste des résultats possibles
# targets = df["SARS-Cov-2 exam result"].unique()

# # for col in float_cols:  
# #     plt.figure(figsize=(6,4))

# #     for target in targets:
# #         subset = df[df["SARS-Cov-2 exam result"] == target]
# #         sns.distplot(subset[col], hist=True, kde=True, label=target)    
# #     plt.title(f"{col} vs Résultat Covid")
# #     plt.legend()
# #     plt.show()


# table = pd.crosstab(df["SARS-Cov-2 exam result"], df["Influenza A"]) 
# print(table)

# co_infections = table.loc["positive"].sum() 
# print("Nombre de co-infections avec Influenza A :", co_infections)


# df["est_malade"] = df[object_cols].apply(lambda row: any(val == "detected" for val in row), axis=1)


# print(pd.crosstab(df["SARS-Cov-2 exam result"], df["est_malade"]))


# # ex06 

# corr_matrix = df[float_cols].corr()

# plt.figure(figsize=(12,8))
# sns.heatmap(corr_matrix, annot=True, cmap="coolwarm", center=0)
# plt.title("Matrice de corrélation des variables sanguines")
# plt.show()




# #Test de Student (t-test)
# positif = df[df ["SARS-Cov-2 exam result"]=="positive"]
# negatif = df [df ["SARS-Cov-2 exam result"]=="negative"]
# significant_cols = []
# for col in float_cols:
#     stat, p = ttest_ind(positif [col].dropna(), negatif [col].dropna())
#     if p < 0.05:
#         significant_cols.append(col)
#     print(f"{col}: p-value = {p:.4f} (significatif)")
# Imports
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt


# Stats
from scipy import stats
import statsmodels.api as sm
from statsmodels.formula.api import ols
from statsmodels.stats.multicomp import pairwise_tukeyhsd
from statsmodels.stats.anova import anova_lm




url = "https://raw.githubusercontent.com/stedy/Machine-Learning-with-R-datasets/master/insurance.csv"
df = pd.read_csv(url)
# 1. Importez le fichier CSV  

print(df.head())
# 2 Vérifiez la structure des données (types de variables) et la présence éventuelle de valeurs manquantes (NA
print(df.info())
print(df.isna().sum())
# 3  Affichez les statistiques descriptives 
print(df.describe())


# plt.figure(figsize=(8,5))
# sns.boxplot(data=df, x="region", y="bmi")
# sns.stripplot(data=df, x="region", y="bmi", color="black", alpha=0.25)
# plt.title("BMI par région")
# plt.show()


desc_bmi = df.groupby("region")["bmi"].agg(["mean","std","count"])
print(desc_bmi)

model = ols("bmi ~ C(region)", data=df).fit()
anova_res = anova_lm(model, typ=2)
print(anova_res)

ct = pd.crosstab(df["region"], df["smoker"])
print(ct)


chi2, p, dof, expected = stats.chi2_contingency(ct)
print(f"Chi2={chi2:.3f}, p-value={p:.5f}, dof={dof}")
exp = pd.DataFrame(expected, index=ct.index, columns=ct.columns)
print("Effectifs attendus (si indépendance):\n", exp)
