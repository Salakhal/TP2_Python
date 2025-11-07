# TP 2 : Encapsulation :

---

# Exercice 1

## Objectif pédagogique
Appliquer les principes d’**encapsulation** en Python :
- Utiliser des **attributs protégés** (`_`) et **privés** (`__`)
- Employer des **propriétés (@property)** pour contrôler l’accès aux données
- **Valider** les valeurs avant toute modification
- Distinguer **interface publique** et **implémentation interne**

---

## Classe `CompteBancaire`

- **Attributs :**
  - `_titulaire` (protégé) : nom du titulaire.
  - `__solde` (privé) : solde du compte.
  - `_operations` : liste des opérations (historique).

- **Méthodes :**
  - `deposer(montant)` : ajouter de l’argent au compte (montant > 0).
  - `retirer(montant)` : retirer de l’argent si disponible.
  - `afficher_historique()` : afficher toutes les opérations.
  - `__str__()` : afficher le titulaire et le solde.
  - `@property solde` : accès en lecture seule au solde.

- **Encapsulation avancée :**
  - `__setattr__` protège `__solde` contre toute modification directe.

---


##  Résultat attendu
  
```
Titulaire : Ali, Solde : 1050 €
Solde accessible (lecture) : 1050
Historique des opérations :
- Dépôt de 200 €
- Retrait de 150 €
Erreur : property 'solde' of 'CompteBancaire' object has no setterer
Titulaire : Sara, Solde : 2000 €
Intérêts ajoutés : 100.0 €
Historique des opérations :
- Dépôt de 100.0 €
- Intérêt ajouté : 100.0 € 
```
##  Exemple d’exécution (image)
 
Voici un exemple de l'exécution du programme (screenshot) :

<img width="954" height="349" alt="image" src="https://github.com/user-attachments/assets/561fabcd-1aa1-4f97-9129-3bd5b8d29d71" />


#  Exercice 2 : Association entre classes

## Objectif pédagogique
Mettre en œuvre l’association entre classes via la composition.  
Ce TP montre comment une classe peut utiliser une autre sans héritage, illustrant une relation de type « a un » ou « utilise ».

## Classes

### 1. `CompteBancaire`
- Attributs :
  - `__solde` (privé) : solde du compte.
  - `_operations` : liste des opérations (avec horodatage).
  - `id` : identifiant unique du compte.
- Méthodes :
  - `deposer(montant)` : ajouter de l’argent au compte.
  - `retirer(montant)` : retirer de l’argent si suffisant.
  - `get_solde()` : accéder au solde.
  - `afficher_operations()` : afficher l’historique avec date/heure.

### 2. `Client`
- Attributs :
  - `nom` : nom du client.
  - `comptes` : liste de comptes du client.
- Méthodes :
  - `ajouter_compte(compte)` : ajouter un compte supplémentaire.
  - `afficher()` : afficher le nom du client et le solde de tous ses comptes.

---
## Résultat attendu
```
Client : Yassir
  Compte 1 : Solde = 250.0€
Client : Yassir
  Compte 1 : Solde = 250.0€
  Compte 2 : Solde = 700€
Relevé du compte 1 :
- 2025-11-07 16:29:55 - Dépôt de 300€
- 2025-11-07 16:29:55 - Retrait de 50€
Relevé du compte 2 :
- 2025-11-07 16:29:55 - Dépôt de 200€

```

##  Exemple d’exécution (image)
 
Voici un exemple de l'exécution du programme (screenshot) :

<img width="769" height="318" alt="image" src="https://github.com/user-attachments/assets/ed432988-e09c-45f5-893b-9504161c4875" />



