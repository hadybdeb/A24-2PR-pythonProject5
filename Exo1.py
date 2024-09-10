# coding: utf-8
import sqlite3

conn = sqlite3.connect('school.db')
# Création d'un cursor
cur = conn.cursor()

# Création de la requete
req = "CREATE TABLE students(id INTEGER PRIMARY KEY AUTOINCREMENT, name TEXT NOT NULL, email TEXT NOT NULL , phone INTEGER not null, section TEXT NOT NULL)"
# Exécution de la requete
cur.execute(req)
# Envoyer la requete
conn.commit()
# Fermer la connexion
conn.close

