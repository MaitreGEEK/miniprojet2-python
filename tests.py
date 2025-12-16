from datetime import datetime
from systeme import SystemeGlobal
from location import SystemeLocation, Location, chevauche
from vehicules import Voiture, Moto, Camion
from clients import Client

def run_tests():
    print("Démarrage des tests...")

    # ==========================================
    # 1. Tests Module Véhicules
    # ==========================================
    # Test instanciation et héritage
    v1 = Voiture(1, "Toyota", "Yaris", "B", 50, "bon")
    assert v1.marque == "Toyota"
    assert v1.age_req == 17
    assert len(v1.entretiens) == 0

    m1 = Moto(2, "Yamaha", "MT07", "A", 80, "neuf")
    assert m1.age_req == 14

    c1 = Camion(3, "Renault", "Master", "C", 120, "moyen")
    assert c1.age_req == 25

    # Test méthode entretien
    date_entretien = datetime(2023, 1, 15)
    v1.ajouter_entretien(date_entretien, 150.0)
    assert len(v1.entretiens) == 1
    assert v1.entretiens[0] == (150.0, date_entretien)

    # Test __str__
    assert "Toyota Yaris" in str(v1)
    
    print("✅ Tests Véhicules OK")

    # ==========================================
    # 2. Tests Module Clients
    # ==========================================
    cl1 = Client(1, "Dupont", "Jean", 25, ["voiture"])
    assert cl1.nom == "Dupont"
    assert "voiture" in cl1.permis
    assert len(cl1.historique) == 0
    
    # Test __str__
    assert "Dupont Jean" in str(cl1)

    print("✅ Tests Clients OK")

    # ==========================================
    # 3. Tests Module Location (Logique pure)
    # ==========================================
    # Test fonction chevauche
    d1 = datetime(2023, 6, 1)
    d2 = datetime(2023, 6, 10)
    d3 = datetime(2023, 6, 5)  # Chevauche
    d4 = datetime(2023, 6, 15) # Après
    d0 = datetime(2023, 5, 20) # Avant

    assert chevauche((d1, d2), (d3, d4)) is True   # 1-10 vs 5-15
    assert chevauche((d1, d2), (d0, d3)) is True   # 1-10 vs 20mai-5juin
    assert chevauche((d1, d2), (datetime(2023, 6, 11), d4)) is False # Pas de chevauchement

    # Test instanciation Location
    loc = Location(1, cl1, v1, (d1, d2))
    jours = (d2 - d1).days # 9 jours
    attendu = 50 * 9 # tarif * jours
    assert loc.cout == attendu
    assert loc.vehicule.id == v1.id

    print("✅ Tests Logique Location OK")

    # ==========================================
    # 4. Tests Système Global (Intégration)
    # ==========================================
    sys_global = SystemeGlobal()

    # --- Test CRUD Véhicules via Système ---
    # Note: ajouter_vehicule() utilise input(), on teste donc via ajouter_chose manuellement
    # pour éviter de bloquer le script, ou on mocke. Ici on teste la logique interne.
    sys_global.ajouter_chose(v1, "vehicules")
    assert len(sys_global.vehicules) == 1
    found_v = sys_global.trouver_chose(1, "vehicules")
    assert found_v == v1
    
    # --- Test CRUD Clients via Système ---
    sys_global.ajouter_chose(cl1, "clients")
    assert len(sys_global.clients) == 1
    
    # --- Test Logique Location via Système ---
    # Cas passant
    sys_global.sys_location.locations = [] # Reset
    dates_ok = (datetime(2025, 1, 1), datetime(2025, 1, 5))
    res = sys_global.sys_location.ajouter_location(cl1, v1, dates_ok)
    assert res is True
    assert len(sys_global.sys_location.locations) == 1

    # Cas échec : Véhicule déjà pris
    res_conflict = sys_global.sys_location.ajouter_location(cl1, v1, dates_ok)
    assert res_conflict is False # Doit échouer car dates chevauchent

    # Cas échec : Age insuffisant
    jeune_client = Client(99, "Kid", "Billy", 16, ["moto"]) # 16 ans
    grosse_voiture = Voiture(99, "Merco", "Benz", "S", 100, "neuf") # Req 17 ans
    res_age = sys_global.sys_location.ajouter_location(jeune_client, grosse_voiture, (datetime(2025, 2, 1), datetime(2025, 2, 5)))
    assert res_age is False

    # --- Test Calculs Financiers ---
    # On a une location valide (v1, 4 jours, 50€/j = 200€)
    # On a un entretien sur v1 (150€)
    assert sys_global.calculer_gains() == 200.0
    assert sys_global.calculer_pertes() == 150.0
    assert sys_global.calculer_benef() == 50.0 # 200 - 150

    # --- Test Suppression ---
    sys_global.supprimer_chose(1, "vehicules")
    assert len(sys_global.vehicules) == 0
    assert sys_global.trouver_chose(1, "vehicules") is None

    print("✅ Tests Système Global OK")
    print("\nTous les tests sont passés avec succès !")

if __name__ == "__main__":
    run_tests()
