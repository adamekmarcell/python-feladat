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

        self.lista.sort(key=lambda orszag: orszag.terulet)

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

    def atlag_nepsuruseg(self):
        ossz_suruseg = 0
        for orszag in self.lista:
            ossz_suruseg = ossz_suruseg + orszag.nepsuruseg

        return ossz_suruseg / len(self.lista)

    def osszterulet(self):
        ossz_terulet = 0
        for orszag in self.lista:
            ossz_terulet = ossz_terulet + orszag.terulet

        return ossz_terulet

    def median(self):
        return self.lista[len(self.lista) - 1].nepesseg

    def nagyobb_mint_suruseg(self, filter):
        eredmény_lista = []

        for orszag in self.lista:
            if orszag.nepsuruseg > filter:
                eredmény_lista.append(orszag)

        return eredmény_lista

    def feladat_kiiras(self):
        nepesseg_feladat = self.legnepesebb_orszag()
        print(f"{self.kontinens} legnagyobb népességű országa: {nepesseg_feladat.info()}")

        terulet_feladat = self.legnagyobb_terulet()
        print(f"{self.kontinens} legnagyobb területű országa: {terulet_feladat.info()}")

        nepsuruseg_feladat = self.legnagyobb_nepsuruseg()
        print(f"{self.kontinens} legnagyobb népsűrűségű országa: {nepsuruseg_feladat.info()}")

        atlag_suruseg = self.atlag_nepsuruseg()
        print(f"{self.kontinens} átlag népsűrűsége: {atlag_suruseg} km/2")

        ossz_terulet_feladat = self.osszterulet()
        print(f"{self.kontinens} összterülete: {ossz_terulet_feladat} négyzetkilométer")

        median_feladat = self.median()
        print(f"{self.kontinens} népességének a mediánja: {median_feladat} fő")

        print()

        nepsuruseg_feladat_2 = self.nagyobb_mint_suruseg(150)
        print(f"{self.kontinens} következő országainak kisebb a népsűrűsége mint 150 fő/km2:")
        for orszag in nepsuruseg_feladat_2:
            print(f"\t-{orszag.info()}")

        print()

        print(f"{self.kontinens} kontinens országai terület szerint növekvő sorrendben:")
        for orszag in self.lista:
            print(f"\t-{orszag.info()}")


europa = Kontinens("forrasok/europa.txt", "Európa")
europa.feladat_kiiras()

print()

azsia = Kontinens("forrasok/azsia.txt", "Ázsia")
azsia.feladat_kiiras()

print()

azsia = Kontinens("forrasok/afrika.txt", "Afrika")
azsia.feladat_kiiras()



