import pandas as pd
from sklearn.preprocessing import MinMaxScaler, StandardScaler

# 
df = pd.read_csv("https://raw.githubusercontent.com/datasciencedojo/datasets/master/titanic.csv")

df['Age'] = df['Age'].fillna(df['Age'].median())
df['Fare'] = df['Fare'].fillna(df['Fare'].median())


scaler_minmax = MinMaxScaler()
df[['Age_minmax', 'Fare_minmax']] = scaler_minmax.fit_transform(df[['Age', 'Fare']])

# Standardisation
scaler_std = StandardScaler()
df[['Age_std', 'Fare_std']] = scaler_std.fit_transform(df[['Age', 'Fare']])

# Vérification
print("Min-Max - Age:", df['Age_minmax'].min(), "à", df['Age_minmax'].max())
print("Min-Max - Fare:", df['Fare_minmax'].min(), "à", df['Fare_minmax'].max())
print("Z-score - Age: moyenne=", round(df['Age_std'].mean(),2), ", écart-type=", round(df['Age_std'].std(),2))
print("Z-score - Fare: moyenne=", round(df['Fare_std'].mean(),2), ", écart-type=", round(df['Fare_std'].std(),2))