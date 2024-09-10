# importer sqlite
import sqlite3
# se connecter
connection = sqlite3.connect('test.db')
# on créer un objet cursor. cet ovjet permet d'envoyer des requetes
cursor = connection.cursor()

# creéer une table si cela n'existe pas ...
#cursor.execute("CREATE TABLE Persons (PersonID int,LastName varchar(255),FirstName varchar(255),City varchar(255))")

# Faire des requetes


cursor.execute("INSERT INTO Persons (PersonID, LastName, FirstName, Address, City) VALUES (3, 'samiha', 'mecheri', 'H4N3B1', 'montreal');")

#cursor.execute("CREATE TABLE Persons ( PersonID int, LastName varchar(255), FirstName varchar(255),Address varchar(255),City varchar(255))")

cursor.execute("select * from persons;")

# delete from Persons WHERE PersonID = 3;

data = cursor.fetchall()
print(data)

connection.commit()
connection.close()