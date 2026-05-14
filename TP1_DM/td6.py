import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.preprocessing import StandardScaler, MinMaxScaler
from sklearn.feature_selection import SelectKBest, chi2, f_classif, RFE
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.linear_model import LogisticRegression, Lasso, Ridge, ElasticNet
from sklearn.decomposition import PCA
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from mlxtend.feature_selection import SequentialFeatureSelector as SFS
import warnings

warnings.filterwarnings('ignore')

URL = "https://raw.githubusercontent.com/datasciencedojo/datasets/master/titanic.csv"
df = pd.read_csv(URL)

# Suppression des colonnes inutiles
df = df.drop(['PassengerId', 'Name', 'Ticket', 'Cabin'], axis=1)

# Encodage des variables catégorielles
df['Sex'] = df['Sex'].map({'male': 0, 'female': 1})
df['Embarked'] = df['Embarked'].map({'S': 0, 'C': 1, 'Q': 2})

# Imputation des valeurs manquantes
df = df.assign(Age=df['Age'].fillna(df['Age'].median()))
df = df.assign(Embarked=df['Embarked'].fillna(df['Embarked'].mode()[0]))

print("Shape:", df.shape)
print("NaN restants:", df.isnull().sum().sum())
print(df.head())


X = df.drop('Survived', axis=1)
y = df['Survived']


# Q2
corr = df.corr()['Survived'].drop('Survived').sort_values(key=abs, ascending=False)
print(corr.round(4))

# Q3
print(df.drop('Survived', axis=1).corr().round(2))

# Q4
print(corr[abs(corr) > 0.4].round(4))

# Heatmap de corrélation
plt.figure(figsize=(9, 7))
sns.heatmap(df.corr(), annot=True, fmt='.2f', cmap='coolwarm', linewidths=.5)
plt.title('Matrice de corrélation  Titanic')
plt.tight_layout()
plt.savefig('heatmap_correlation.png', dpi=150)
plt.show()

# Q5 – SelectKBest Chi2
X_mm = pd.DataFrame(MinMaxScaler().fit_transform(X), columns=X.columns)
kb_chi2 = SelectKBest(chi2, k=5).fit(X_mm, y)
chi2_scores = pd.Series(kb_chi2.scores_, index=X.columns).sort_values(ascending=False)
print(chi2_scores.head(5).round(2))

# Q6 – SelectKBest f_classif

kb_f = SelectKBest(f_classif, k=5).fit(X, y)
f_scores = pd.Series(kb_f.scores_, index=X.columns).sort_values(ascending=False)
print(f_scores.head(5).round(2))

# Visualisation Chi2 vs f_classif
fig, axes = plt.subplots(1, 2, figsize=(12, 4))
chi2_scores.sort_values().plot(kind='barh', ax=axes[0], color='coral')
axes[0].set_title('Scores Chi2')
f_scores.sort_values().plot(kind='barh', ax=axes[1], color='teal')
axes[1].set_title('Scores f_classif')
plt.tight_layout()
plt.savefig('filter_scores.png', dpi=150)
plt.show()


lr = LogisticRegression(max_iter=1000)

# Q9 – Forward Selection

sfs_fwd = SFS(lr, k_features=5, forward=True, scoring='accuracy', cv=5)
sfs_fwd.fit(X, y)
fwd_feats = list(sfs_fwd.k_feature_names_)
print("Features:", fwd_feats)
print(f"Score CV: {sfs_fwd.k_score_:.4f}")

# Q9 – Backward Selection
sfs_bwd = SFS(lr, k_features=5, forward=False, scoring='accuracy', cv=5)
sfs_bwd.fit(X, y)
bwd_feats = list(sfs_bwd.k_feature_names_)
print("Features:", bwd_feats)
print(f"Score CV: {sfs_bwd.k_score_:.4f}")
print("Communes Forward ∩ Backward:", sorted(set(fwd_feats) & set(bwd_feats)))

# Q10 – RFE

rfe = RFE(LogisticRegression(max_iter=1000), n_features_to_select=5)
rfe.fit(X, y)
rfe_feats = X.columns[rfe.support_].tolist()
rfe_ranking = pd.Series(rfe.ranking_, index=X.columns).sort_values()
print("Features sélectionnées:", rfe_feats)
print("Ranking complet:\n", rfe_ranking)


# Q11 – ID3 (entropy)

id3 = DecisionTreeClassifier(criterion='entropy', random_state=42)
id3.fit(X, y)
id3_imp = pd.Series(id3.feature_importances_, index=X.columns).sort_values(ascending=False)
print(id3_imp.round(4))

# Q12 – CART (gini)

cart = DecisionTreeClassifier(criterion='gini', random_state=42)
cart.fit(X, y)
cart_imp = pd.Series(cart.feature_importances_, index=X.columns).sort_values(ascending=False)
print(cart_imp.round(4))

# Q13 – Random Forest

rf = RandomForestClassifier(n_estimators=100, random_state=42)
rf.fit(X, y)
rf_imp = pd.Series(rf.feature_importances_, index=X.columns).sort_values(ascending=False)
print(rf_imp.round(4))

# Visualisation importance des arbres
fig, axes = plt.subplots(1, 3, figsize=(16, 5))
for ax, imp, title, color in zip(
    axes,
    [id3_imp, cart_imp, rf_imp],
    ['ID3 (entropy)', 'CART (gini)', 'Random Forest'],
    ['darkorange', 'forestgreen', 'mediumpurple']
):
    imp.sort_values().plot(kind='barh', ax=ax, color=color)
    ax.set_title(title)
    for i, v in enumerate(imp.sort_values()):
        ax.text(v + 0.002, i, f'{v:.3f}', va='center', fontsize=9)
plt.suptitle('Importance des variables – Méthodes basées sur les arbres', fontsize=13)
plt.tight_layout()
plt.savefig('tree_importances.png', dpi=150)
plt.show()


X_sc = StandardScaler().fit_transform(X)

# Q15-16 – Lasso

lasso = Lasso(alpha=0.01, max_iter=10000)
lasso.fit(X_sc, y)
lasso_coef = pd.Series(lasso.coef_, index=X.columns).sort_values(key=abs, ascending=False)
print(lasso_coef.round(4))
print("Variables à zéro:", lasso_coef[lasso_coef == 0].index.tolist() or ["Aucune"])

# Q17 – Ridge

ridge = Ridge(alpha=1.0)
ridge.fit(X_sc, y)
ridge_coef = pd.Series(ridge.coef_, index=X.columns).sort_values(key=abs, ascending=False)
print(ridge_coef.round(4))

# Q18 – ElasticNet

en = ElasticNet(alpha=0.01, l1_ratio=0.5, max_iter=10000)
en.fit(X_sc, y)
en_coef = pd.Series(en.coef_, index=X.columns).sort_values(key=abs, ascending=False)
print(en_coef.round(4))
print("Variables à zéro:", en_coef[en_coef == 0].index.tolist() or ["Aucune"])

# Graphique des coefficients de régularisation
fig, ax = plt.subplots(figsize=(10, 5))
x = np.arange(len(X.columns))
w = 0.25
ax.bar(x - w, lasso_coef[X.columns], w, label='Lasso', color='red', alpha=0.75)
ax.bar(x,     ridge_coef[X.columns], w, label='Ridge', color='navy', alpha=0.75)
ax.bar(x + w, en_coef[X.columns],    w, label='ElasticNet', color='seagreen', alpha=0.75)
ax.set_xticks(x)
ax.set_xticklabels(X.columns, rotation=30, ha='right')
ax.axhline(0, color='black', linewidth=0.8)
ax.set_title('Coefficients – Lasso / Ridge / ElasticNet')
ax.legend()
plt.tight_layout()
plt.savefig('regularisation_coefs.png', dpi=150)
plt.show()


# Q20 – Application PCA

pca = PCA(n_components=0.95, random_state=42)
pca.fit(X_sc)

# Scree plot
cumvar = np.cumsum(pca.explained_variance_ratio_)
plt.figure(figsize=(7, 4))
plt.bar(range(1, pca.n_components_ + 1), pca.explained_variance_ratio_,
        color='teal', alpha=0.8, label='Variance individuelle')
plt.plot(range(1, pca.n_components_ + 1), cumvar, 'r-o', ms=5, label='Variance cumulée')
plt.axhline(0.95, color='gray', linestyle='--', lw=1, label='Seuil 95%')
plt.xlabel('Composante principale')
plt.ylabel('Variance expliquée')
plt.title(f'PCA – {pca.n_components_} composantes retenues')
plt.legend()
plt.tight_layout()
plt.savefig('pca_scree.png', dpi=150)
plt.show()

# Q21 – Comparaison précision avec / sans PCA

X_train, X_test, y_train, y_test = train_test_split(X_sc, y, test_size=0.2, random_state=42)

lr_full = LogisticRegression(max_iter=1000).fit(X_train, y_train)
acc_full = accuracy_score(y_test, lr_full.predict(X_test))

X_pca_train = pca.transform(X_train)
X_pca_test  = pca.transform(X_test)
lr_pca = LogisticRegression(max_iter=1000).fit(X_pca_train, y_train)
acc_pca = accuracy_score(y_test, lr_pca.predict(X_pca_test))

print(f"Précision sans PCA : {acc_full:.4f}")
print(f"Précision avec PCA : {acc_pca:.4f}")

plt.figure(figsize=(5, 4))
bars = plt.bar(['Sans PCA', 'Avec PCA'], [acc_full, acc_pca],
               color=['steelblue', 'tomato'], width=0.4)
for bar, v in zip(bars, [acc_full, acc_pca]):
    plt.text(bar.get_x() + bar.get_width() / 2, v + 0.005,
             f'{v:.3f}', ha='center', fontweight='bold')
plt.ylim(0, 1)
plt.title('Précision – Régression Logistique: Sans vs Avec PCA')
plt.tight_layout()
plt.savefig('pca_accuracy.png', dpi=150)
plt.show()