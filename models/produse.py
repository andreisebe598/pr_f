class Produs:
    def __init__(self, id_produs, denumire, categorie, pret_vanzare, cost_achizitie, cantitate):
        self.id_produs = id_produs
        self.denumire = denumire
        self.categorie = categorie
        self.pret_vanzare = pret_vanzare
        self.cost_achizitie = cost_achizitie
        self.cantitate = cantitate

    def __str__(self):
        return (
            f"ID: {self.id_produs}, Denumire: {self.denumire}, "
            f"Categorie: {self.categorie}, "
            f"Pret vanzare: {self.pret_vanzare}, "
            f"Cost achizitie: {self.cost_achizitie}, "
            f"Cantitate: {self.cantitate}"
        )

    def to_dict(self):
        return {
            "id_produs": self.id_produs,
            "denumire": self.denumire,
            "categorie": self.categorie,
            "pret_vanzare": self.pret_vanzare,
            "cost_achizitie": self.cost_achizitie,
            "cantitate": self.cantitate
        }
    
    @staticmethod
    def from_dict(data):
        return Produs(
            data["id_produs"],
            data["denumire"],
            data.get("categorie", "Necunoscut"),
            data.get("pret_vanzare", 0),
            data.get("cost_achizitie", 0),
            data.get("cantitate", 0)
        )
    
