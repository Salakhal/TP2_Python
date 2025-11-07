from datetime import datetime

class CompteBancaire:
    _compteur_id = 1  

    def __init__(self, solde_initial=0.0):
        self.id = CompteBancaire._compteur_id
        CompteBancaire._compteur_id += 1
        self.__solde = solde_initial
        self._operations = []

    def deposer(self, montant):
        if montant > 0:
            self.__solde += montant
            self._operations.append(f"{datetime.now()} - Dépôt de {montant}€")
        else:
            print("Montant invalide.")

    def retirer(self, montant):
        if 0 < montant <= self.__solde:
            self.__solde -= montant
            self._operations.append(f"{datetime.now()} - Retrait de {montant}€")
        else:
            print("Fonds insuffisants ou montant invalide.")

    def get_solde(self):
        return self.__solde

    def afficher_operations(self):
        print(f"Relevé du compte {self.id} :")
        for op in self._operations:
            print("-", op)
