class Raport:
    def __init__(self, perioada_start = None, perioada_end = None, numar_comenzi = 0, total_incasari = 0, total_cheltuieli = 0, total_profit = 0):
        self.perioada_start = perioada_start
        self.perioada_end = perioada_end
        self.numar_comenzi = numar_comenzi
        self.total_incasari = total_incasari
        self.total_cheltuieli = total_cheltuieli
        self.total_profit = total_profit

    def __str__(self):
        return f"Raport({self.perioada_start} - {self.perioada_end}): {self.numar_comenzi} comenzi, Profit: {self.total_profit:.2f} RON"
    
    def __repr__(self):
        return self.__str__()
    
    def to_dict(self):
        return {
            "perioada_start": self.perioada_start,
            "perioada_end": self.perioada_end,
            "numar_comenzi": self.numar_comenzi,
            "total_incasari": self.total_incasari,
            "total_cheltuieli": self.total_cheltuieli,
            "total_profit": self.total_profit
        }
    
    @staticmethod
    def from_dict(data):
        return Raport(
            data.get("perioada_start"),
            data.get("perioada_end"),
            data.get("numar_comenzi", 0),
            data.get("total_incasari", 0),
            data.get("total_cheltuieli", 0),
            data.get("total_profit", 0)
        )