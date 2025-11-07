from Client import Client
from CompteBancaire import CompteBancaire

if __name__ == "__main__":
    cli = Client("Yassir")

    cli.comptes[0].deposer(300)
    cli.comptes[0].retirer(50)
    cli.afficher()

    compte2 = CompteBancaire(500)
    cli.ajouter_compte(compte2)
    cli.comptes[1].deposer(200)
    cli.afficher()

    for compte in cli.comptes:
        compte.afficher_operations()
