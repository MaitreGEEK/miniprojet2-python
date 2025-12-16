# Système de Gestion de Location de Véhicules

Application CLI Python pour l'administration d'un parc automobile, la gestion de la clientèle et le suivi des contrats de location.

## Architecture Technique

Le projet suit une architecture orientée objet modulaire :

* **main.py** : Point d'entrée de l'application. Gère l'interface en ligne de commande (CLI) et le routage des actions utilisateur.
* **systeme.py** : Contrôleur principal (`SystemeGlobal`). Agit comme une façade pour orchestrer les interactions entre les sous-systèmes (clients, véhicules, locations).
* **location.py** : Logique métier des réservations. Contient l'algorithme de vérification des disponibilités (détection de chevauchement de dates) et la gestion des contrats.
* **vehicules.py** : Modèles de données avec héritage. La classe abstraite `Vehicule` est étendue par `Voiture`, `Moto` et `Camion`, chacune définissant ses propres contraintes (ex: âge requis).
* **clients.py** : Gestion des entités clients et validation des permis.

## Fonctionnalités Clés

### Gestion du Parc
* Système de classes polymorphes pour gérer différents types de véhicules.
* Suivi du cycle de vie des véhicules (état, historique des entretiens).
* Règles de validation métier (âge minimum selon le type de véhicule : 14 ans pour Moto, 17 pour Voiture, 25 pour Camion).

### Système de Location
* Vérification automatique des conflits de dates avant validation.
* Calcul dynamique des coûts basé sur la durée et le tarif journalier.
* Gestion des pénalités et calcul du coût total.

### Administration & Finance
* Génération de rapports financiers globaux :
  * Calcul du Chiffre d'Affaires (Gains).
  * Suivi des coûts opérationnels (Entretiens).
  * Calcul du Bénéfice Net.
* Statistiques d'utilisation du parc.

## Installation et Exécution

Le projet ne nécessite aucune dépendance externe (utilise uniquement la librairie standard).

1. Lancer l'application :
```python main.py```

2. Navigation :
L'interface utilise un système de menus numériques pour accéder aux différents modules (Parc, Clients, Locations, Rapports).

## Prérequis

* Python 3.8 ou supérieur
