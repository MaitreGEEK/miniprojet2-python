class Client:
    def __init__(self, id, nom, prenom, age, permis, historique):
        self.id = id
        self.nom = nom
        self.prenom = prenom
        self.age = age
        self.permis = permis | []
        self.historique = historique | []
   
    def __str__(self):
        return f"Client {self.id}: {self.nom} {self.prenom} ({self.age}) {self.permis} {self.historique}"
