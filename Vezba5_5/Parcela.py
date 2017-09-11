from Poligon import Poligon

class Parcela(Poligon):

    n_koriscenja = { 1 : "gradjevinsko zemjiste",
                     2 : "njiva"}

    def __init__(self, id_poligon, prelomne_tacke, id_parcela, br_parcela, nacin_koriscenja_parcela):
        super(Parcela, self).__init__(id_poligon, prelomne_tacke)

        self.id_parcela = id_parcela
        self.br_parcela = br_parcela
        self.nacin_koriscenja_parcela = nacin_koriscenja_parcela

    def get_id_parcela (self): return self.id_parcela
    def set_id_parcela (self, new_id_parcela): self.id_parcela = new_id_parcela

    def get_br_parcela (self): return self.br_parcela
    def set_br_parcela (self, new_br_parcela): self.br_parcela = new_br_parcela

    def get_nacin_koriscenja_parcela (self): return self.nacin_koriscenja_parcela
    def set_nacin_koriscenja_parcela (self, new_nacin_koriscenja_parcela): self.nacin_koriscenja_parcela = new_nacin_koriscenja_parcela
    def daj_nacin_koriscenja (self): return self.n_koriscenja[self.nacin_koriscenja_parcela]