class DetaljnaTacka(object):

    n_stabilizacije = {1: "Nestabilisana na terenu",
                       2: "Stabilisana kamenom belegom"}
    
    def __init__(self, id_detaljne_tacke, oznaka_tacke, nacin_stabilizacije, x, y):
        self.id_detaljne_tacke = id_detaljne_tacke
        self.oznaka_tacke = oznaka_tacke
        self.nacin_stabilizacije = nacin_stabilizacije
        self.x = x
        self.y = y

    def get_id_detaljne_tacke (self): return self.id_detaljne_tacke
    def set_id_detaljne_tacke (self, new_id_detaljne_tacke): self.id_detaljne_tacke = new_id_detaljne_tacke

    def get_oznaka_tacke (self): return self.oznaka_tacke
    def set_oznaka_tacke (self, new_oznaka_tacke): self.oznaka_tacke = new_oznaka_tacke

    def get_nacin_stabilizacije (self): return self.nacin_stabilizacije
    def set_nacin_stabilizacije (self, new_nacin_stabilizacije): self.nacin_stabilizacije = new_nacin_stabilizacije
    def daj_nacin_stabilizacije (self): return self.n_stabilizacije [self.nacin_stabilizacije]

    def get_x (self): return self.x
    def set_x (self, new_x): self.x = new_x

    def get_y (self): return self.y
    def set_y (self, new_y): self.y = new_y

    def get_wkt_tacke (self): 
        wkt_tacke = ("POINT (%s %s)" % (self.y, self.x))
        return wkt_tacke