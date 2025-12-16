class Vehicule:
    def __init__(self, id, marque, modele, categorie, tarif, etat, entretiens=[])->None:
        self.id = id
        self.marque = marque
        self.modele = modele 
        self.categorie = categorie
        self.tarif = tarif
        self.etat = etat
        self.entretiens = entretiens
    
    def __str__(self)->str:
        return f"Le véhicule {self.id} est un {self.marque} {self.modele} de {self.categorie} au tarif de {self.tarif} en état {self.etat}"
    
    def ajouter_entretien(self, date, prix)->None:
        self.entretiens.append((prix, date))


class Voiture(Vehicule):
    age_req=17
class Camion(Vehicule):
    age_req=25
class Moto(Vehicule):
    age_req=14
