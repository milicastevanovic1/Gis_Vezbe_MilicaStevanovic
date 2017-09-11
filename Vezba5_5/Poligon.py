class Poligon(object):

    def __init__(self, id_poligon, prelomne_tacke):
        self.id_poligon = id_poligon
        self.prelomne_tacke = prelomne_tacke

    def get_id_poligon (self): return self.id_poligon
    def set_id_poligon (self, new_id_poligon): self.id_poligon = new_id_poligon

    def get_prelomne_tacke (self): return self.prelomne_tacke
    def set_prelomne_tacke (self, new_prelomne_tacke): self.prelomne_tacke = new_prelomne_tacke

    def br_prelomne_tacke(self): return len(self.prelomne_tacke)

    def polygonArea (self):
        area = 0
        for n in range(0, len(self.prelomne_tacke)-1):
            area = area + self.prelomne_tacke[n].get_y() * (self.prelomne_tacke[n + 1].get_x()) - (self.prelomne_tacke[n - 1].get_x())
        area = area + self.prelomne_tacke[len(self.prelomne_tacke) - 1].get_y() * (self.prelomne_tacke[0].get_x() - self.prelomne_tacke[len(self.prelomne_tacke) - 2].get_x())
        return abs(area/2)
       
    def get_wkt_poligon(self):
        list = []
        for i in self.get_prelomne_tacke():
            tacka = "%s %s" % (i.get_y(), i.get_x())
            list.append(tacka)
        m = ','.join(list)
        wkt = "POLYGON ((%s))" % m
        return wkt
