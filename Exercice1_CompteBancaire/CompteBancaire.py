class CompteBancaire:
    def __init__(self, titulaire, solde_initial=0):
        self._titulaire = titulaire
        self.__solde = solde_initial
        self._operations = []

    def deposer(self, montant):
        if montant > 0:
            self.__solde += montant
            self._operations.append(f"Dépôt de {montant} €")
        else:
            print("Montant invalide.")

    def retirer(self, montant):
        if 0 < montant <= self.__solde:
            self.__solde -= montant
            self._operations.append(f"Retrait de {montant} €")
        else:
            print("Fonds insuffisants ou montant invalide.")

    @property
    def solde(self):
        return self.__solde

    def afficher_historique(self):
        print("Historique des opérations :")
        for op in self._operations:
            print("-", op)

    def __str__(self):
        return f"Titulaire : {self._titulaire}, Solde : {self.solde} €"
