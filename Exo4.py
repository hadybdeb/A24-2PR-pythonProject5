# coding: utf-8
import sqlite3

conn = sqlite3.connect('school.db')
cur = conn.cursor()
# Insérer une ligne de données
cur.execute("SELECT * FROM students")

# Engager l'opération
conn.commit()
resultat = cur.fetchall()
print(resultat[0])
print(resultat[0][2])

# Fermer la connexion
conn.close()
