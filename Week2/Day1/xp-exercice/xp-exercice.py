#!/usr/bin/env python
# coding: utf-8

# # Exercice 1

# - Qu'est-ce que l'analyse de données ?
# 
# L'analyse de données est un processus qui consiste à collecter, nettoyer, transformer et interpréter des données brutes afin d'en extraire des informations utiles, des tendances significatives ou des conclusions exploitables. 
# 
# - Pourquoi l'analyse des données est-elle importante dans les contextes modernes ?
# 
# Une aide à la décision fondée sur les faits
# Réponse aux défis sociétaux
# 
# - Trois domaines d'application actuels
# 
#   La santé et la médecine de précision
#   La finance et la détection de fraudes

# # Exercice 2

# In[10]:


import pandas as pd


# In[29]:


clean_dataset=pd.read_csv(r"C:\Users\AKRE\Documents\FORMATION\FORMATION TTA\DI-Bootcamp-TTA\Week2\Day1\xp-exercice\Credit Card Approvals (Clean Data)\clean_dataset.csv")
clean_dataset.head()
clean_dataset.describe()


# In[28]:


crx=pd.read_csv(r"C:\Users\AKRE\Documents\FORMATION\FORMATION TTA\DI-Bootcamp-TTA\Week2\Day1\xp-exercice\Credit Card Approvals (Clean Data)\crx.csv")
crx.head()
crx.describe()


# In[27]:


mental = pd.read_csv(
    r"C:\Users\AKRE\Documents\FORMATION\FORMATION TTA\DI-Bootcamp-TTA\Week2\Day1\xp-exercice\Global Trends in Mental Health Disorder\Mental health Depression disorder Data.csv",
    low_memory=False
)

mental.head()
mental.describe()


# # Exercice 3

# In[38]:


import pandas as pd

clean_dataset=pd.read_csv(r"C:\Users\AKRE\Documents\FORMATION\FORMATION TTA\DI-Bootcamp-TTA\Week2\Day1\xp-exercice\Credit Card Approvals (Clean Data)\clean_dataset.csv")
crx=pd.read_csv(r"C:\Users\AKRE\Documents\FORMATION\FORMATION TTA\DI-Bootcamp-TTA\Week2\Day1\xp-exercice\Credit Card Approvals (Clean Data)\crx.csv")
mental = pd.read_csv(
    r"C:\Users\AKRE\Documents\FORMATION\FORMATION TTA\DI-Bootcamp-TTA\Week2\Day1\xp-exercice\Global Trends in Mental Health Disorder\Mental health Depression disorder Data.csv",
    low_memory=False
)


# In[40]:


datas=[clean_dataset,crx,mental]
i=0

for data in datas:
    i+=1
    print(f"AFFichage pour la data {i}: {i} ")
    for col in data.columns:

        if (
            data[col].dtype == "int64"
            or
            data[col].dtype == "float64"
        ):

            print(f"{col} -> Quantitative")

        else:

            print(f"{col} -> Qualitative")


# In[41]:


crx


# # Exercice 4

# In[51]:


data_iris=pd.read_csv(r"C:\Users\AKRE\Documents\FORMATION\FORMATION TTA\DI-Bootcamp-TTA\Week2\Day1\xp-exercice\Iris Dataset\Iris.csv")
data_iris


# In[49]:


for col in data_iris.columns:

    if (
        data_iris[col].dtype == "int64"
        or
        data_iris[col].dtype == "float64"
    ):

        print(f"{col} -> Quantitative")

    else:

        print(f"{col} -> Qualitative")


# # Exercice 5

# In[56]:


sommeil=pd.read_csv(r"C:\Users\AKRE\Documents\FORMATION\FORMATION TTA\DI-Bootcamp-TTA\Week2\Day1\xp-exercice\How Much Sleep Do Americans\Time Americans Spend Sleeping.csv")

sommeil


# For a trend analysis, the most relevant columns are:
# 
# - Year:
# This column allows us to observe changes over time.
# 
# - Avg hrs per day sleeping:
# This is the main quantitative variable measuring the mean sleeping duration.
# 
# These columns can help identify whether Americans are sleeping more or less over the years.

# For group comparison analysis, the following columns are relevant:
# 
# - Gender:
# This column separates individuals into groups.
# 
# - Avg hrs per day sleeping:
# This variable measures the amount of sleep and can be compared between genders.
# 
# This analysis could help determine whether sleep duration differs between men and women.

# # Exercice 6 : Identification des types de donnée

# - Structurée: 
# 
# Les rapports financiers d'une entreprise sont stockés dans un fichier Excel.
# Données d'inventaire dans une base de données relationnelle.
# 
# - Non structurée
#   
# Photographies téléchargées sur une plateforme de médias sociaux.
# Une collection d'articles de presse sur un site web.
# Enregistrements d'entretiens issus d'une étude de marché.

# #  Exercice 7 : Exercice de transformation
# Pour chacune des sources de données non structurées suivantes, proposez une méthode pour la convertir en données structurées. Justifiez votre choix.

# # 1- Une série d'articles de blog sur les expériences de voyage.
# 
#    - méthode : Utiliser le traitement du langage naturel (NLP) pour extraire des informations clés
#    - jusitification: Les articles peuvent être analysés afin d’extraire des données structurées comme les lieux visités, les dates, les activités ou les avis. Ces informations peuvent ensuite être stockées dans un tableau ou une base de données.
# 
# # 2- Enregistrements audio des appels au service client
# 
# - méthode: Utiliser la reconnaissance vocale (Speech-to-Text) puis analyser le texte obtenu
# - justification: Les fichiers audio sont d’abord convertis en texte. Ensuite, les données importantes (nom du client, type de problème, satisfaction, durée de l’appel) peuvent être organisées sous forme structurée.
# 
# # 3- Notes manuscrites issues d’une séance de brainstorming:
# 
# - méthode : Utiliser un système OCR (Optical Character Recognition)
# - justification: L’OCR permet de convertir l’écriture manuscrite en texte numérique. Ce texte peut ensuite être classé en catégories ou stocké dans une base de données structurée.
# 
# # 4- Un tutoriel vidéo sur la cuisine
# - méthode : Extraire l’audio puis utiliser Speech-to-Text et l’analyse vidéo
# - justification : La vidéo peut être transformée en texte grâce à la transcription audio. On peut ensuite structurer les informations comme les ingrédients, les étapes de préparation et le temps de cuisson.

# #  Exercice 8 : Importer un fichier depuis Kaggle

# In[63]:


train_data=pd.read_csv(r"C:\Users\AKRE\Documents\FORMATION\FORMATION TTA\DI-Bootcamp-TTA\Week2\Day1\xp-exercice\train.csv")
train_data.head()


# # Exercice 9 : Exporter un dataframe au format Excel et au format JSON.

# In[68]:


import pandas as pd

# Création d'un dataframe simple
data = {
    "Nom": ["Alice", "Bob", "Charlie"],
    "Age": [25, 30, 22],
    "Ville": ["Paris", "Londres", "Abidjan"]
}

df = pd.DataFrame(data)

# Affichage du dataframe
print(df)

# Export vers un fichier Excel
df.to_excel("dataframe.xlsx", index=False)

# Export vers un fichier JSON
df.to_json("dataframe.json", orient="records", indent=4)

print("Export terminé avec succès !")


# In[69]:


get_ipython().system('pip install openpyxl')


# # Exercice 10 : Lecture de données JSON

# In[74]:


import pandas as pd

# URL du fichier JSON compressé
url = "https://github.com/devtlv/Datasets-DA-Bootcamp-2-/raw/refs/heads/main/Week%204%20-%20Data%20Understanding/W4D3%20-%20Importing%20Data,%20Exporting%20D/posts.zip"

# Lire les données JSON
df = pd.read_json(url, compression="zip")

# Afficher les 5 premières lignes
print(df.head())

