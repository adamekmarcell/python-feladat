class Orszag:
    def __init__(self, nev = "-", fovaros = "-", terulet = 0, nepesseg = 0, nepsuruseg = 0.0):
        self.nev = nev
        self.fovaros = fovaros
        self.terulet = terulet
        self.nepesseg = nepesseg
        self.nepsuruseg = nepsuruseg

    def info(self):
        return f"Ország: {self.nev}, népesség: {self.nepesseg}, főváros: {self.fovaros}, terület: {self.terulet}, népsűrűség: {self.nepsuruseg}"
    

class Kontinens:
    def __init__(self, adatok, kontinens):
        self.lista = []
        self.eleres = adatok
        self.kontinens = kontinens

        self.importalas()
    
    def orszag_hozzaad(self, orszag):
        self.lista.append(orszag)

    def importalas(self):
        file = open(self.eleres, "r", encoding="utf-8")
        next(file)

        for sor in file:
            adatok = sor.strip().split(";")

            self.orszag_hozzaad(Orszag(adatok[0], adatok[1], int(adatok[2]), int(adatok[3]), float(adatok[4])))

    def legnepesebb_orszag(self):
        legnagyobb_nepessegu_orszag = Orszag()
        for orszag in self.lista:
            if orszag.nepesseg > legnagyobb_nepessegu_orszag.nepesseg:
                legnagyobb_nepessegu_orszag = orszag

        return legnagyobb_nepessegu_orszag

    def legnagyobb_terulet(self):
        legnagyobb_orszag = Orszag()
        for orszag in self.lista:
            if orszag.terulet > legnagyobb_orszag.terulet:
                legnagyobb_orszag = orszag

        return legnagyobb_orszag
    
    def legnagyobb_nepsuruseg(self):
        suru_orszag = Orszag()
        for orszag in self.lista:
            if orszag.nepsuruseg > suru_orszag.nepsuruseg:
                suru_orszag = orszag

        return suru_orszag

    def feladat_kiiras(self):
        nepesseg_feladat = self.legnepesebb_orszag()
        print(f"{self.kontinens} legnagyobb népességű országa: {nepesseg_feladat.info()}")

        terulet_feladat = self.legnagyobb_terulet()
        print(f"{self.kontinens} legnagyobb területű országa: {terulet_feladat.info()}")

        nepsuruseg_feladat = self.legnagyobb_nepsuruseg()
        print(f"{self.kontinens} legnagyobb népsűrűségű országa: {nepsuruseg_feladat.info()}")

europa = Kontinens("forrasok/europa.txt", "Európa")
europa.feladat_kiiras()

print()

azsia = Kontinens("forrasok/azsia.txt", "Ázsia")
azsia.feladat_kiiras()

print()

azsia = Kontinens("forrasok/afrika.txt", "Afrika")
azsia.feladat_kiiras()



