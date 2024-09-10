# coding: utf-8
import sqlite3
name      = input("Saisir le nom de l'étudiant : ")
email     = input("Saisir l'email de l'étudiant : ")
phone =int(input("Saisir le téléphone de l'étudiant : "))
section   = input("Saisir la section de l'étudiant : ")
conn = sqlite3.connect('school.db')
cur = conn.cursor()
# Insérer une ligne de données
cur.execute("Insert into students (`name` , `email` , `phone` , `section`) values (? , ? , ? , ?)" , (name , email , phone , section) )
# Engager l'opération
conn.commit()
# Fermer la connexion
conn.close()
