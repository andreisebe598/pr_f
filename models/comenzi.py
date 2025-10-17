class Comanda:
    def __init__(self, id_comanda, id_client, id_angajat, produse, data=None):
        self.id_comanda = id_comanda

        if hasattr(id_client, "id_client"):
            self.id_client = id_client.id_client
            self.client = id_client
        else:
            self.id_client = id_client
            self.client = None

        if hasattr(id_angajat, "id_angajat"):
            self.id_angajat = id_angajat.id_angajat
            self.angajat = id_angajat
        else:
            self.id_angajat = id_angajat
            self.angajat = None

        self.produse = produse
        self.data = data

    def __str__(self):
        produse_str = ", ".join([f"{item['produs'].denumire} x{item['cantitate']}" for item in self.produse])
        return f"Comanda #{self.id_comanda} - Client: {self.id_client}, Angajat: {self.id_angajat}, Produse: [{produse_str}], Data: {self.data}"

    def __repr__(self):
        return self.__str__()
    
    def to_dict(self):
        return {
            "id_comanda": self.id_comanda,
            "id_client": self.id_client,
            "id_angajat": self.id_angajat,
            "produse": [
                {
                    "id_produs": item["produs"].id_produs,
                    "denumire": item["produs"].denumire,
                    "categorie": item["produs"].categorie,     
                    "pret_vanzare": item["produs"].pret_vanzare,
                    "cost_achizitie": item["produs"].cost_achizitie, 
                    "cantitate": item["cantitate"]
                }
                for item in self.produse
            ],
            "data": self.data
    }
    
    @staticmethod
    def from_dict(data):
        produse_lista = []

        from models.produse import Produs

        for item in data["produse"]:
            produs = Produs(
                id_produs=item["id_produs"],
                denumire=item["denumire"],
                categorie=item.get("categorie", "Necunoscut"), 
                pret_vanzare=item.get("pret_vanzare", 0),
                cost_achizitie=item.get("cost_achizitie", 0),
                cantitate=item.get("cantitate", 0)
            )

            produse_lista.append({
                "produs": produs,
                "cantitate": item["cantitate"]
            })
        
        return Comanda(
            id_comanda=data["id_comanda"],
            id_client=data["id_client"],
            id_angajat=data["id_angajat"],
            produse=produse_lista,
            data=data["data"]
        )