from CompteBancaire import CompteBancaire

class CompteEpargne(CompteBancaire):
    def __init__(self, titulaire, solde_initial=0, taux_interet=0.02):
        super().__init__(titulaire, solde_initial)
        self._taux_interet = taux_interet

    def calculer_interet(self):
        interet = self.solde * self._taux_interet
        self.deposer(interet)
        self._operations.append(f"Intérêt ajouté : {interet} €")
        print(f"Intérêts ajoutés : {interet} €")
