"""
TD N°5 : Arbres de Décision - Solutions Complètes
Machine Learning - Licence d'excellence S6
=================================================
Ce fichier contient les solutions complètes des 5 exercices avec preprocessing détaillé.
"""

# ============================================================
# EXERCICE 1 : Prédiction de la fraude sur carte de crédit
# ============================================================
"""
Dataset : https://www.kaggle.com/datasets/mlg-ulb/creditcardfraud
Télécharger 'creditcard.csv' et le placer dans le même dossier.
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.tree import DecisionTreeClassifier, plot_tree, export_text
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder, StandardScaler
from sklearn.metrics import (classification_report, confusion_matrix,
                             accuracy_score, ConfusionMatrixDisplay)
from sklearn.linear_model import LogisticRegression
from sklearn.utils import resample

# 1. Chargement des données


df1 = pd.read_csv("creditcard.csv")

print(df1.shape)
print(df1.head(3))
print(df1.info())




# 2. Preprocessing

print(df1.isnull().sum())

# 2b. Distribution des classes (déséquilibre)

print(df1['Class'].value_counts())
print(f"Taux de fraude : {df1['Class'].mean()*100:.4f}%")

scaler = StandardScaler()
df1['Amount_scaled'] = scaler.fit_transform(df1[['Amount']])
df1['Time_scaled']   = scaler.fit_transform(df1[['Time']])
df1.drop(['Amount', 'Time'], axis=1, inplace=True)

df_majority = df1[df1['Class'] == 0]
df_minority = df1[df1['Class'] == 1]

df_majority_down = resample(df_majority,
                            replace=False,
                            n_samples=len(df_minority) * 10,
                            random_state=42)
df1_balanced = pd.concat([df_majority_down, df_minority])
print(f"\nApres reechantillonnage : {df1_balanced['Class'].value_counts().to_dict()}")




# 3. Train / Test split
X1 = df1_balanced.drop('Class', axis=1)
y1 = df1_balanced['Class']

X1_train, X1_test, y1_train, y1_test = train_test_split(
    X1, y1, test_size=0.2, random_state=42, stratify=y1)

# 4. Entraînement du modèle
dt1 = DecisionTreeClassifier(max_depth=5, class_weight='balanced', random_state=42)
dt1.fit(X1_train, y1_train)


# 5. Évaluation

y1_pred = dt1.predict(X1_test)
print(classification_report(y1_test, y1_pred, target_names=['Légitime', 'Fraude']))

# Matrice de confusion
cm1 = confusion_matrix(y1_test, y1_pred)
disp1 = ConfusionMatrixDisplay(cm1, display_labels=['Légitime', 'Fraude'])
disp1.plot(cmap='Blues')
plt.title("Exercice 1  Matrice de confusion (Fraude)")
plt.tight_layout()
plt.savefig("ex1_confusion_matrix.png", dpi=150)
plt.show()


#  visualisation 
plt.figure(figsize=(20, 8))
plot_tree(dt1, max_depth=3, feature_names=X1.columns,
          class_names=['Légitime', 'Fraude'], filled=True, fontsize=8)
plt.title("Exercice 1  Arbre de décision (3 premiers niveaux)")
plt.tight_layout()
plt.savefig("ex1_tree.png", dpi=150)
plt.show()

# Importance des features
feat_imp1 = pd.Series(dt1.feature_importances_, index=X1.columns).sort_values(ascending=False)

print(feat_imp1.head(10))

