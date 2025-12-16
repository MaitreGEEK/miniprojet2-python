from location import SystemeLocation
from vehicules import Moto, Voiture, Camion
from datetime import datetime
from clients import Client

class SystemeGlobal:
    def __init__(self, clients=[], vehicules=[], locations=[])->None:
        self.clients = clients
        self.vehicules = vehicules
        self.sys_location = SystemeLocation(locations)
    def ajouter_chose(self, chose, type_chose):
        getattr(self, type_chose).append(chose)
        return True
    def trouver_chose(self, chose_id, type_chose):
        for chose in getattr(self, type_chose):
            if str(chose.id) == str(chose_id):
                return chose
        return None
    def supprimer_chose(self, chose_id, type_chose) -> bool:
        collection = getattr(self, type_chose)

        for i, chose in enumerate(collection):
            if str(chose.id) == str(chose_id):
                del collection[i]
                return True
        return False
    def calculer_gains(self) -> int:
        somme = 0
        for location in self.sys_location.locations:
            somme += location.cout + location.penalite
        return somme
    def calculer_pertes(self) -> int:
        somme = 0
        for voiture in self.vehicules:
            for entretien in voiture.entretiens:
                somme += entretien[0]
        return somme
    def calculer_benef(self) -> int:
        return self.calculer_gains() - self.calculer_pertes()
    def calculer_statistiques(self) -> dict:
        return {
            "vehicules": len(self.vehicules),
            "locations": len(self.sys_location.locations),
            "clients": len(self.clients)
        }
    def generer_rapports(self) -> str:
        stats = self.calculer_statistiques()
        gains = self.calculer_gains()
        pertes = self.calculer_pertes()
        benef = self.calculer_benef()

        return (
            "\n===== RAPPORT GLOBAL =====\n"
            f"Véhicules enregistrés : {stats['vehicules']}\n"
            f"Clients enregistrés   : {stats['clients']}\n"
            f"Locations totales     : {stats['locations']}\n"
            "\n--- Financier ---\n"
            f"Gains totaux  : {gains:.2f} €\n"
            f"Pertes totales: {pertes:.2f} €\n"
            f"Bénéfice net  : {benef:.2f} €\n"
            "=========================="
        )

    def ajouter_vehicule(self) -> str:
        print("=== AJOUT D'UN VÉHICULE ===")

        marque = input("Marque : ").strip()
        modele = input("Modèle : ").strip()
        etat = input("État (neuf / bon / moyen / mauvais) : ").strip()
        tarif = int(input("Tarif journalier (€) : ").strip())
        categorie = input("Catégorie : ").strip()

        print("\nType de véhicule :")
        print("1️⃣ Moto")
        print("2️⃣ Voiture")
        print("3️⃣ Camion")

        type_vehicule = input("Choix (1-3) : ").strip()
        vehicule = None
        _id = len(self.vehicules)
        if type_vehicule == "1":
            vehicule = Moto(_id, marque, modele, categorie, tarif, etat)
        elif type_vehicule == "2":
            vehicule = Voiture(_id, marque, modele, categorie, tarif, etat)
        elif type_vehicule == "3":
            vehicule = Camion(_id, marque, modele, categorie, tarif, etat)
        else:
            return "❌ Type invalide"

        self.ajouter_chose(vehicule, "vehicules")
        
        return "✅ Véhicule ajouté "

    def afficher_vehicule(self)->str:
        print("=== AFFICHER UN VÉHICULE ===")
        vid = input("ID du véhicule : ").strip()

        vehicule = self.trouver_chose(vid, "vehicules")

        if not vehicule:
            return "❌ Véhicule introuvable"

        return str(vehicule)
    def afficher_vehicules(self)->str:
        print("=== AFFICHER TOUS LES VÉHICULES ===")
        vehicules = ""
        for vehicule in self.vehicules:
            vehicules += str(vehicule) + "\n"
        if vehicules == "":
            vehicules = "Aucun véhicule enregistré"
        return vehicules
    def retirer_vehicule(self) -> bool:
        print("=== SUPPRIMER UN VÉHICULE ===")
        vid = input("ID du véhicule : ").strip()

        ok:bool = self.supprimer_chose(vid, "vehicules")
        if not ok:
            return "❌ Aucun véhicule ne correspond à l'id"
        return "✅ Véhicule supprimé"
    def entretien_vehicule(self):
        print("=== ENTRETIEN VÉHICULE ===")

        vid = input("ID du véhicule : ").strip()
        vehicule = self.trouver_chose(vid, "vehicules")

        if not vehicule:
            return "❌ Véhicule introuvable"

        try:
            prix = float(input("Coût de l'entretien (€) : ").strip())
        except ValueError:
            return "❌ Prix invalide"

        date_str = input("Date de l'entretien (YYYY-MM-DD) : ").strip()
        try:
            date = datetime.strptime(date_str, "%Y-%m-%d")
        except ValueError:
            return "❌ Date invalide (format attendu : YYYY-MM-DD)"

        vehicule.ajouter_entretien(date, prix)

        return "✅ Entretien enregistré"

    def ajouter_client(self) -> str:
        print("=== AJOUT D'UN CLIENT ===")

        nom = input("Nom : ").strip()
        prenom = input("Prénom : ").strip()

        try:
            age = int(input("Âge : ").strip())
        except ValueError:
            return "❌ Âge invalide"

        permis = []
        while True:
            print("\nPermis possédés :")
            print("1️⃣ Voiture")
            print("2️⃣ Moto")
            print("3️⃣ Camion")
            print("0️⃣ Terminer")

            choix = input("Choix : ").strip()

            if choix == "1" and "voiture" not in permis:
                permis.append("voiture")
            elif choix == "2" and "moto" not in permis:
                permis.append("moto")
            elif choix == "3" and "camion" not in permis:
                permis.append("camion")
            elif choix == "0":
                break
            else:
                print("Choix invalide ou déjà ajouté")

        if not permis:
            return "❌ Un client doit avoir au moins un permis"

        _id = len(self.clients)
        client = Client(_id, nom, prenom, age, permis)

        self.ajouter_chose(client, "clients")

        return "✅ Client ajouté"
    def afficher_client(self) -> str:
        print("=== AFFICHER UN CLIENT ===")
        cid = input("ID du client : ").strip()

        client = self.trouver_chose(cid, "clients")

        if not client:
            return "❌ Client introuvable"

        return str(client)
    def afficher_clients(self) -> str:
        print("=== LISTE DES CLIENTS ===")

        if not self.clients:
            return "Aucun client enregistré"

        res = ""
        for client in self.clients:
            res += str(client) + "\n"

        return res
    def retirer_client(self) -> str:
        print("=== SUPPRIMER UN CLIENT ===")
        cid = input("ID du client : ").strip()

        ok = self.supprimer_chose(cid, "clients")

        if not ok:
            return "❌ Aucun client ne correspond à l'ID"

        return "✅ Client supprimé"
    def ajouter_location(self) -> str:
        print("=== AJOUT D'UNE LOCATION ===")

        cid = input("ID client : ").strip()
        vid = input("ID véhicule : ").strip()

        client = self.trouver_chose(cid, "clients")
        vehicule = self.trouver_chose(vid, "vehicules")

        if not client or not vehicule:
            return "❌ Client ou véhicule introuvable"

        if client.age < vehicule.age_req:
            return "❌ Client trop jeune pour louer ce véhicule"

        try:
            d1 = datetime.strptime(input("Date début (YYYY-MM-DD) : "), "%Y-%m-%d")
            d2 = datetime.strptime(input("Date fin   (YYYY-MM-DD) : "), "%Y-%m-%d")
        except ValueError:
            return "❌ Date invalide"

        if d1 >= d2:
            return "❌ Intervalle de dates invalide"

        ok = self.sys_location.ajouter_location(client, vehicule, (d1, d2))

        return "✅ Location ajoutée" if ok else "❌ Location impossible"
    def calculer_location(self) -> str: 
        print("=== CALCUL D'UNE LOCATION ===")

        vid = input("ID véhicule : ").strip()

        vehicule = self.trouver_chose(vid, "vehicules")

        if not vehicule:
            return "❌ Véhicule introuvable"

        try:
            d1 = datetime.strptime(input("Date début (YYYY-MM-DD) : "), "%Y-%m-%d")
            d2 = datetime.strptime(input("Date fin   (YYYY-MM-DD) : "), "%Y-%m-%d")
        except ValueError:
            return "❌ Date invalide"

        if d1 >= d2:
            return "❌ Intervalle de dates invalide"
        return f"Prix de la location : {vehicule.tarif*(d2-d1).days} €"        
    def retirer_location(self) -> str:
        print("=== SUPPRIMER UNE LOCATION ===")
        loc_id = input("ID de la location : ").strip()

        ok = self.sys_location.supprimer_location(loc_id)
        return "✅ Location supprimée" if ok else "❌ Location introuvable"
    def afficher_locations(self) -> str:
        print("=== LISTE DES LOCATIONS ===")
        if not self.sys_location.locations:
            return "Aucune location enregistrée"
        return "\n".join(str(loc) for loc in self.sys_location.locations)
    def afficher_location(self) -> str:
        print("=== AFFICHER LOCATION ===")
        loc_id = input("ID de la location : ").strip()
        location = self.sys_location.trouver_location(loc_id)
        if not location:
            return "❌ Location non trouvée"
        return str(location)