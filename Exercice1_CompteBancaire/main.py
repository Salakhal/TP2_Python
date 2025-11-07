from CompteBancaire import CompteBancaire
from CompteEpargne import CompteEpargne

if __name__ == "__main__":
    # --- Test CompteBancaire ---
    compte = CompteBancaire("Ali", 1000)
    compte.deposer(200)
    compte.retirer(150)
    print(compte)
    print("Solde accessible (lecture) :", compte.solde)
    compte.afficher_historique()

    try:
        compte.solde = 500  # Test protection
    except AttributeError as e:
        print("Erreur :", e)

    # --- Test CompteEpargne ---
    compte_epargne = CompteEpargne("Sara", 2000, taux_interet=0.05)
    print(compte_epargne)
    compte_epargne.calculer_interet()
    compte_epargne.afficher_historique()
