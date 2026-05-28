"""
==========================================================
  DAILY CHALLENGE - Data Handling and Analysis in Python
==========================================================
Thèmes couverts :
  1. Min-Max Normalization de la colonne 'salary'
  2. Réduction de dimension avec PCA
  3. Agrégation par 'experience_level' (moyenne + médiane)
"""

import pandas as pd
import numpy as np
from sklearn.preprocessing import MinMaxScaler, LabelEncoder
from sklearn.decomposition import PCA


# ─────────────────────────────────────────────
# 0. CHARGEMENT DU DATASET
# ─────────────────────────────────────────────
df = pd.read_csv('datascience_salaries.csv', index_col=0)

print("=== Aperçu du dataset ===")
print(df.head())
print(f"\nDimensions : {df.shape[0]} lignes × {df.shape[1]} colonnes")
print("\nColonnes disponibles :", df.columns.tolist())
print("\nNiveaux d'expérience :", df['experience_level'].unique().tolist())


# ─────────────────────────────────────────────
# 1. MIN-MAX NORMALIZATION
# ─────────────────────────────────────────────
# Pourquoi ? Les salaires vont de 30 000 $ à 228 000 $.
# Cette grande plage peut déséquilibrer les modèles ML.
# On ramène tout entre 0 et 1 avec la formule :
#   x_norm = (x - x_min) / (x_max - x_min)

scaler = MinMaxScaler()

# fit_transform : apprend le min/max PUIS transforme
df['salary_normalized'] = scaler.fit_transform(df[['salary']])

print("\n" + "=" * 50)
print("ÉTAPE 1 : Min-Max Normalization")
print("=" * 50)
print(df[['salary', 'salary_normalized']].head(10).to_string())
print(f"\n→ Salaire min normalisé : {df['salary_normalized'].min()}  (était {df['salary'].min()} $)")
print(f"→ Salaire max normalisé : {df['salary_normalized'].max()}  (était {df['salary'].max()} $)")
# Vérification : min doit être 0.0 et max doit être 1.0


# ─────────────────────────────────────────────
# 2. RÉDUCTION DE DIMENSION AVEC PCA
# ─────────────────────────────────────────────
# Pourquoi ? Notre dataset a plusieurs colonnes (features).
# PCA (Principal Component Analysis) résume ces colonnes
# en 2 nouvelles variables (PCA_1, PCA_2) qui capturent
# l'essentiel de l'information.

# PCA ne fonctionne qu'avec des nombres → on encode
# d'abord les colonnes texte avec LabelEncoder.
le = LabelEncoder()
df_encoded = df.copy()

colonnes_texte = ['job_title', 'job_type', 'experience_level', 'location', 'salary_currency']
for col in colonnes_texte:
    # LabelEncoder transforme : "Senior" → 2, "Entry" → 0, etc.
    df_encoded[col + '_enc'] = le.fit_transform(df[col])

# On sélectionne les features numériques à réduire
features = ['job_title_enc', 'job_type_enc', 'experience_level_enc',
            'location_enc', 'salary_normalized']
X = df_encoded[features]

print("\n" + "=" * 50)
print("ÉTAPE 2 : Réduction de dimension (PCA)")
print("=" * 50)
print(f"Dimensions AVANT PCA : {X.shape[1]} colonnes")

# n_components=2 → on garde 2 composantes principales
pca = PCA(n_components=2)
pca_result = pca.fit_transform(X)

# On ajoute les nouvelles colonnes au DataFrame original
df['PCA_1'] = pca_result[:, 0]
df['PCA_2'] = pca_result[:, 1]

print(f"Dimensions APRÈS  PCA : 2 colonnes (PCA_1, PCA_2)")
print(f"\nVariance expliquée par PCA_1 : {pca.explained_variance_ratio_[0]:.2%}")
print(f"Variance expliquée par PCA_2 : {pca.explained_variance_ratio_[1]:.2%}")
print(f"Variance TOTALE capturée     : {pca.explained_variance_ratio_.sum():.2%}")
# Un score proche de 100 % = presque aucune info perdue !

print("\nAperçu des composantes PCA :")
print(df[['PCA_1', 'PCA_2']].head())


# ─────────────────────────────────────────────
# 3. AGRÉGATION PAR NIVEAU D'EXPÉRIENCE
# ─────────────────────────────────────────────
# Pourquoi ? On veut comprendre comment le salaire évolue
# selon le niveau (Entry, Mid, Senior, Executive).
# - La moyenne donne une idée générale.
# - La médiane est plus robuste aux valeurs extrêmes.

print("\n" + "=" * 50)
print("ÉTAPE 3 : Agrégation par niveau d'expérience")
print("=" * 50)

agg = (
    df.groupby('experience_level')['salary']
    .agg(
        moyenne='mean',
        mediane='median'
    )
    .round(2)
    .sort_values('moyenne')          # tri croissant pour mieux lire
)

print(agg.to_string())

print("\n→ Interprétation :")
for level, row in agg.iterrows():
    print(f"   {level:12s} | Moyenne : {row['moyenne']:>10,.0f} $  |  Médiane : {row['mediane']:>10,.0f} $")

print("\n✅ Analyse terminée avec succès !")
