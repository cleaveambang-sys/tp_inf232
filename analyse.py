import pandas as pd
import matplotlib.pyplot as plt

# Charger les données
df = pd.read_csv("data.csv", names=["nom", "age", "sexe", "ville", "secteur"])

print("\n📌 Aperçu des données")
print(df.head())

# -----------------------------
# 📊 1. Statistiques sur l'âge
# -----------------------------
print("\n📊 Statistiques âge")
print(df["age"].describe())

print("\n📊 Moyenne d'âge :", df["age"].mean())

# -----------------------------
# 📊 2. Répartition par sexe
# -----------------------------
print("\n📊 Répartition par sexe")
print(df["sexe"].value_counts())

df["sexe"].value_counts().plot(kind="bar")
plt.title("Répartition par sexe")
plt.show()

# -----------------------------
# 📊 3. Répartition par ville
# -----------------------------
print("\n📊 Répartition par ville")
print(df["ville"].value_counts())

df["ville"].value_counts().plot(kind="bar")
plt.title("Répartition par ville")
plt.show()

# -----------------------------
# 📊 4. Répartition par secteur
# -----------------------------
print("\n📊 Répartition par secteur")
print(df["secteur"].value_counts())

df["secteur"].value_counts().plot(kind="bar")
plt.title("Répartition par secteur")
plt.show()