import pandas as pd
import numpy as np

# Les données du dictionnaire
exam_data = {
    'name': ['Anastasia', 'Dima', 'Katherine', 'James', 'Emily', 'Michael', 'Matthew', 'Laura', 'Kevin', 'Jonas'],
    'score': [12.5, 9, 16.5, np.nan, 9, 20, 14.5, np.nan, 8, 19],
    'attempts': [1, 3, 2, 3, 2, 3, 1, 1, 2, 1],
    'qualify': ['yes', 'no', 'yes', 'no', 'no', 'yes', 'yes', 'no', 'no', 'yes']
}

labels = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']

df = pd.DataFrame(exam_data, index=labels)

print("Les trois premières lignes du DataFrame:")
print(df.head(3))

df_cleaned = df.dropna()
print("\nDataFrame après suppression des lignes avec des valeurs NaN:")
print(df_cleaned)

df_name_score = df_cleaned[['name', 'score']]
print("\nLes colonnes 'name' et 'score':")
print(df_name_score)

# Ajouter une nouvelle ligne 'k'
df_cleaned.loc['k'] = ['Suresh', 15.5, 1, 'yes']
print("\nDataFrame après ajout de la ligne 'k':")
print(df_cleaned)

df_no_attempts = df_cleaned.drop('attempts', axis=1)
print("\nDataFrame après suppression de la colonne 'attempts':")
print(df_no_attempts)

# Ajouter une nouvelle colonne "Success"
df_no_attempts['Success'] = df_no_attempts['score'].apply(lambda x: 1 if x > 10 else 0)
print("\nDataFrame après ajout de la colonne 'Success':")
print(df_no_attempts)

# Exporter le DataFrame final dans un fichier CSV
df_no_attempts.to_csv('my_data.csv', index=True)

print("\nLe DataFrame final a été exporté dans 'my_data.csv'")

