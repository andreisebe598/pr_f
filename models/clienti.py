class Client:
    def __init__(self, id_client, nume, gen, varsta, bautura_preferata):
        self.id_client = id_client
        self.nume = nume
        self.gen = gen
        self.varsta = varsta
        self.bautura_preferat = bautura_preferata

    def __str__(self):
        return f"{self.id_client}: {self.nume} -> ({self.gen}, {self.varsta}) - Bautura Preferata: {self.bautura_preferat}"        

    def to_dict(self):
        return {
            "id_client": self.id_client,
            "nume": self.nume,
            "gen": self.gen,
            "varsta": self.varsta,
            "bautura_preferata": self.bautura_preferat
        }
    
    @staticmethod
    def from_dict(data):
        return Client(data["id_client"], data["nume"], data["gen"], data["varsta"], data["bautura_preferata"])
