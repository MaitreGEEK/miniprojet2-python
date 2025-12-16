import os
from systeme import SystemeGlobal

def nettoyer() -> None:
    os.system('cls' if os.name == 'nt' else 'clear')

def entree() -> None:
    input("\nAppuyez sur entrée pour continuer...")

location_sys = SystemeGlobal()
def menu() -> None:
    while True:
        nettoyer()
        print(
            "\n=== MENU LOCATION DE VOITURES ===\n"
            "1️⃣ Gérer le parc de véhicules\n"
            "2️⃣ Gérer les clients\n"
            "3️⃣ Gérer les locations\n"
            "4️⃣ Calculer le coût d’une location\n"
            "5️⃣ Générer des rapports\n"
            "6️⃣ Quitter"
        )

        choix: str = input("Votre choix (1-6) : ").strip()
        nettoyer()

        if choix == "1":
            menu_parc_vehicules()
        elif choix == "2":
            menu_clients()
        elif choix == "3":
            menu_locations()
        elif choix == "4":

            entree()
        elif choix == "5":
            print(location_sys.generer_rapports())
            entree()
        elif choix == "6":
            print("Fin du programme.")
            break
        else:
            print("Choix invalide.")
            entree()


# ===== SOUS-MENUS =====

def menu_parc_vehicules() -> None:
    while True:
        nettoyer()
        print(
            "\n=== GESTION DU PARC DE VÉHICULES ===\n"
            "1️⃣ Ajouter un véhicule\n"
            "2️⃣ Afficher un véhicule\n"
            "3️⃣ Retirer un véhicule\n"
            "4️⃣ Enregistrer un entretien sur un véhicule\n"
            "5️⃣ Afficher tous les véhicules\n"
            "0️⃣ Retour"
        )

        choix: str = input("Votre choix : ").strip()
        nettoyer()

        if choix == "1":
            print(location_sys.ajouter_vehicule())
            entree()
        elif choix == "2":
            print(location_sys.afficher_vehicule())
            entree()
        elif choix == "3":
            print(location_sys.retirer_vehicule())
            entree()
        elif choix == "4":
            print(location_sys.entretien_vehicule())
            entree()
        elif choix == "5":
            print(location_sys.afficher_vehicules())
            entree()
        elif choix == "0":
            break
        else:
            print("Choix invalide.")
            entree()


def menu_clients() -> None:
    while True:
        nettoyer()
        print(
            "\n=== GESTION DES CLIENTS ===\n"
            "1️⃣ Ajouter un client\n"
            "2️⃣ Afficher un client\n"
            "3️⃣ Retirer un client\n"
            "4️⃣ Afficher tous les clients\n"
            "0️⃣ Retour"
        )

        choix: str = input("Votre choix : ").strip()
        nettoyer()

        if choix == "1":
            print(location_sys.ajouter_client())
            entree()
        elif choix == "2":
            print(location_sys.afficher_client())
            entree()
        elif choix == "3":
            print(location_sys.retirer_client())
            entree()
        elif choix == "4":
            print(location_sys.afficher_clients())
            entree()
        elif choix == "0":
            break
        else:
            print("Choix invalide.")
            entree()


def menu_locations() -> None:
    while True:
        nettoyer()
        print(
            "\n=== GESTION DES LOCATIONS ===\n"
            "1️⃣ Ajouter une location\n"
            "2️⃣ Afficher les locations\n"
            "3️⃣ Retirer une location\n"
            "0️⃣ Retour"
        )

        choix: str = input("Votre choix : ").strip()
        nettoyer()

        if choix == "1":
            print(location_sys.ajouter_location())
            entree()
        elif choix == "2":
            print(location_sys.afficher_locations())
            entree()
        elif choix == "3":
            print(location_sys.retirer_location())
            entree()
        elif choix == "0":
            break
        else:
            print("Choix invalide.")
            entree()

menu()