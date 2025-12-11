from datetime import datetime

def chevauche(resa_exist: tuple[datetime, datetime], nouvelle: tuple[datetime, datetime]) -> bool:
    start1, end1 = resa_exist
    start2, end2 = nouvelle
    return start1 < end2 and start2 < end1

class Location:
    def __init__(self, client, vehicule, dates, penalite=0):
        self.client = client
        self.vehicule = vehicule
        self.dates = dates
        self.cout = vehicule.tarif * (dates[0]-dates[1])
        self.penalite = penalite
    def __str__(self):
        return f"Location: {self.client} a loué {self.vehicule} pour dates {self.dates} au prix de {cout}"

class SystemeLocation():
    def __init__(self, locations=[]):
        self.locations:[Location] = locations
    def verifier_disponibilite(self, dates, vehicule):
        disponible = True
        for location in self.locations:
            if chevauche(location.dates, dates) and location.vehicule.id == vehicule.id: 
                # Ce véhicule est déjà utilisé sur cette intervalle
                disponible = False
                break
        return disponible
    def ajouter_location(self, client, vehicule, dates):
        if client.age < vehicule.age_req: return False
        if (self.verifier_disponibilite(dates, vehicule)): return False
        else: 
            self.locations.append(Location(client, vehicule, dates))
            return True
    def supprimer_location(self, client, vehicule, dates):
        for i in range(len(self.location)):
            location = self.location[i]
            if location.client.id == location.client.id and location.dates == dates and location.vehicule.id == vehicule.id:
                del self.location[i]
                return True
        return False
    
