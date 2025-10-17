class Angajat:
    def __init__(self, id_angajat, nume, prenume, salariu, post):
        self.id_angajat = id_angajat
        self.nume = nume
        self.prenume = prenume
        self.salariu = salariu
        self.post = post

    def __str__(self):
        return f"{self.id_angajat}. Nume: {self.nume} {self.prenume} - Salariu: {self.salariu} - Post: {self.post}"

    def to_dict(self):
        return {
            "id_angajat": self.id_angajat,
            "nume": self.nume,
            "prenume": self.prenume,
            "salariu": self.salariu,
            "post": self.post
        }
    
    @staticmethod
    def from_dict(data):
        return Angajat(data["id_angajat"], data["nume"], data["prenume"], data["salariu"], data["post"])
