from location import SystemeLocation

class SystemeGlobal:
    def __init__(self, clients=[], vehicules=[], locations=[]):
        self.clients = clients
        self.vehicules = vehicules
        self.sys_location = SystemeLocation(locations)
    def ajouter_chose(self, chose, type_chose):
        self[type_chose].append(chose)
        return True
    def trouver_chose(self, chose_id, type_chose):
        for chose in self[type_chose]:
            if chose.id == chose_id:
                return chose
        return None
    def supprimer_chose(self, chose_id, type_chose):
        for i in range(len(self[type_chose])):
            chose = self[type_chose][i]
            if chose.id == chose_id:
                del self.chose[i]
                return True
        return False
    def calculer_gains(self):
        somme = 0
        for location in self.sys_location.locations:
            somme += location.cout + location.penalite
        return somme
    def calculer_pertes(self):
        somme = 0
        for voiture in self.vehicules:
            for entretien in voiture.entretiens:
                somme += entretien[0]
        return somme
    def calculer_benef(self):
        return self.calculer_gains() - self.calculer_pertes()
    def calculer_statistiques(self):
        return {
            vehicules: len(self.vehicules),
            locations: len(self.sys_location.locations),
            clients: len(self.clients)
        }