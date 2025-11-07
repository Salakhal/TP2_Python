from CompteBancaire import CompteBancaire

class Client:
    def __init__(self, nom):
        self.nom = nom
        self.comptes = [CompteBancaire()]  

    def ajouter_compte(self, compte):
        self.comptes.append(compte)

    def afficher(self):
        print(f"Client : {self.nom}")
        for compte in self.comptes:
            print(f"  Compte {compte.id} : Solde = {compte.get_solde()}€")
