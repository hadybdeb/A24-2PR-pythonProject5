# Utiliser une base de donnée :
import sqlite3

from PyQt6.QtWidgets import QWidget, QApplication, QPushButton, QLineEdit


# Créer une table
def CreerTable():
    print("Créer la table ")
    conn = sqlite3.connect('projet2.db')
    cursor = conn.cursor()  # cursor objet qui permet d'executer les requetes
    req1 = """CREATE TABLE Persons (
    PersonID int,
    Prenom varchar(255),
    Nom varchar(255),
    Mail varchar(255)
);"""
    cursor.execute(req1)
    conn.commit()


# inser dans une table
def InsererDansTablePersonne(PersonID, Prenom, Nom, Mail):
    print("Inserer une personne")
    conn = sqlite3.connect('projet2.db')
    cursor = conn.cursor()
    req2 = "INSERT INTO Persons (PersonID, Prenom, Nom, Mail) VALUES (" + str(
        PersonID) + ", '" + Prenom + "', '" + Nom + " ', '" + Mail + "');"
    cursor.execute(req2)
    conn.commit()
    AfficherPersonnes()


# Affiche le contenu select
def AfficherPersonnes():
    print("Afficher les personne")
    conn = sqlite3.connect('projet2.db')
    cursor = conn.cursor()
    req2 = "SELECT * FROM persons;"
    cursor.execute(req2)
    resultat = cursor.fetchall()
    print(resultat)


def commitAction():
    InsererDansTablePersonne(inputID.text(), inputPrenom.text(), inputNom.text(), inputMail.text())


#

# App PyQt
app = QApplication([])
fen = QWidget()

##1 pushButton

btnCommit = QPushButton(fen)
btnCommit.setText("Commit")
btnCommit.setGeometry(500, 150, 100, 30)
btnCommit.clicked.connect(commitAction)

# lineEdit x 4 +
inputID = QLineEdit(fen)
inputID.setGeometry(50, 150, 100, 30)
inputPrenom = QLineEdit(fen)
inputPrenom.setGeometry(150, 150, 100, 30)
inputNom = QLineEdit(fen)
inputNom.setGeometry(250, 150, 100, 30)
inputMail = QLineEdit(fen)
inputMail.setGeometry(350, 150, 100, 30)

fen.show()
app.exec()

