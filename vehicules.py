class Vehicule:
    def __init__(self, id, marque, modele, categorie, tarif, etat, entretien=[]):
        self.id = id
        self.marque = marque
        self.modele = modele 
        self.categorie = categorie
        self.tarif = tarif
        self.etat = etat
    
    def __str__(self):
        return f"Le véhicule {self.id} est un {self.marque} {self.modele} de {self.categorie} au tarif de {self.tarif} en état {self.etat}"


class Voiture(Vehicule):
    age_req=17
class Camion(Vehicule):
    age_req=25
class Moto(Vehicule):
    age_req=14
