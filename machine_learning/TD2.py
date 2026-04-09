

# EX 01 
# PARTIE 1 
import pandas as pd 
import matplotlib
import matplotlib.pyplot as plt 
import seaborn as sns

print(f"Pandas version: {pd.__version__}") 
print(f"Matplotlib version: {matplotlib.__version__}") 

# PARTIE 2

df_immo = pd.read_csv("immobilier_Casablanca.csv", sep=";" , encoding="utf-8")

# df_immo.info()

valeur_manquantes = df_immo.isnull().sum()
print(" ** les valeurs manquantes **\n", valeur_manquantes)
print("      ****\n")

# partie 3 

print( " avant ", df_immo.columns.to_list())

df_immo.columns = df_immo.columns.str.strip()
df_immo.columns = df_immo.columns.str.replace(" ", "_")
df_immo.columns = df_immo.columns.str.replace("[^A-Za-z0-9_]", "", regex=True)

print( " apres ", df_immo.columns)

print("nombres ligne avant la suppression : " , len(df_immo))
df_immo = df_immo.drop_duplicates()
print("nombres ligne apres la suppression : " , len(df_immo))


# partie 4 

print(df_immo[['name', 'price', 'superficie']].head(15))

bien = df_immo[df_immo['price'] > 2000000]
print(len(bien))



print(df_immo['quartier'].unique())
californie = df_immo[df_immo['quartier'].str.contains("californie", case=False, na=False)]
californie.head()

biens_chambres = df_immo[(df_immo['NbChambres'] >= 2) & (df_immo['NbChambres'] <= 4)]

biens_moyens = df_immo[(df_immo['price'] >= 500000) & (df_immo['price'] <= 1500000)]

bon_etat = df_immo[df_immo['etat'] == "bon état"]

calif_abordable = df_immo[(df_immo['quartier'].str.contains("californie", case=False, na=False)) & (df_immo['price'] < 2000000)]



# partie 5 

moyenne_prix = df_immo['price'].mean()
print("Moyenne des prix :", moyenne_prix)

prix_par_quartier = df_immo.groupby('quartier')['price'].mean()
print(prix_par_quartier)

resume_stats = df_immo.describe()
print(resume_stats)

# colonnes = 

min_value = df_immo[["price", "superficie"]].min()
max_value = df_immo[["price", "superficie"]].max()

print(f"min {min_value}, max : {max_value}")

#  partie 6

plt.hist(df_immo["price"], bins=30)
plt.title("distribition des valeur des prix ")
plt.xlabel("price")
plt.ylabel("nbr des chambres ")
plt.show()

# df_immo[""]

quatier_moy = df_immo.groupby("quartier")['price'].mean()
top15 = quatier_moy.nlargest(15)

top15.plot(kind="bar")
plt.title("top 15 quartier")
plt.xlabel("quarier")
plt.ylabel("prix moy")
plt.show()

df_immo.boxplot(column="price", by="NbChambres")
plt.title("distribution des prix des apparts")
plt.xlabel("nbr des chambres")
plt.ylabel("prix")
plt.show()

corr = df_immo[["price", "superficie", "NbSallesBains", "NbChambres"]].corr()
plt.figure(figsize=(8,6))
sns.heatmap(corr, annot=True, cmap="coolwarm", fmt=".2f")
plt.title("Corrélations entre variables numériques")
plt.show()


# data cleaning 

print(df_immo.isnull().sum())
# drop duplicate
df_immo.drop_duplicates(inplace=True)
df_immo['Prix'] = pd.to_numeric(df_immo['Prix'], errors='coerce')
df_immo['Superficie'] = pd.to_numeric(df_immo['Superficie'], errors='coerce')
df_immo['NbChambres'] = pd.to_numeric(df_immo['NbChambres'], errors='coerce')
df_immo['NbSallesBains'] = pd.to_numeric(df_immo['NbSallesBains'], errors='coerce')