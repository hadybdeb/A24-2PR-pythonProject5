# -*- coding: utf-8 -*-
import sqlite3

conn = sqlite3.connect('school.db')
cur = conn.cursor()
# Insérer une ligne de données
cur.execute(
    "INSERT INTO students(`name` , `email` , `phone` , `section`) VALUES ('David', 'david@gmail.com' , 333785123 , 'Math')")
# Engager l'opération
conn.commit()
# Fermer la connexion
conn.close()

