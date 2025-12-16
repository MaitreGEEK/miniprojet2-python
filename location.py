from datetime import datetime

def chevauche(resa_exist: tuple[datetime, datetime], nouvelle: tuple[datetime, datetime]) -> bool:
    start1, end1 = resa_exist
    start2, end2 = nouvelle
    return start1 < end2 and start2 < end1

class Location:
    def __init__(self, id, client, vehicule, dates, penalite=0)->None:
        self.id = id
        self.client = client
        self.vehicule = vehicule
        self.dates = dates
        nb_jours = (dates[1] - dates[0]).days
        self.cout = vehicule.tarif * nb_jours
        self.penalite = penalite
    def __str__(self)->str:
        return (
            f"Location | Client: {self.client.id} | "
            f"Véhicule: {self.vehicule.id} | "
            f"Du {self.dates[0].date()} au {self.dates[1].date()} | "
            f"Prix: {self.cout} €"
        )

class SystemeLocation():
    def __init__(self, locations=[])->None:
        self.locations:[Location] = locations
    def verifier_disponibilite(self, dates, vehicule)->bool:
        disponible = True
        for location in self.locations:
            if chevauche(location.dates, dates) and location.vehicule.id == vehicule.id: 
                disponible = False
                break
        return disponible
    def ajouter_location(self, client, vehicule, dates)->bool:
        if client.age < vehicule.age_req: return False
        if not self.verifier_disponibilite(dates, vehicule): return False
        else: 
            _id = len(self.locations)
            self.locations.append(Location(_id, client, vehicule, dates))
            return True
    def supprimer_location(self, id)->bool:
        for i in range(len(self.location)):
            location = self.locations[i]
            if location.id == id:
                del self.locations[i]
                return True
        return False
    def trouver_location(self, id)->None|Location:
        for location in self.location:
            if location.id == id:
                return location
        return None