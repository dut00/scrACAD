"""Program do tworzenia skryptów w AutoCadzie """
import math
from CommandsACAD import *

# -*- coding: utf-8 -*-

# Komenda w konsoli do tworzenia plików scr
# python trzeci.py > out.scr


# RYSUJE OBSZAR I RAMKĘ RYSUNKU -------------------------------------------
class Frame:
    ODSUNIECIE_RAMKI = 4
    MIEJSCE_NA_WPIECIE = 16    

    def __init__(self, x_0=0, y_0=0, paper_format="A4", orientation="v", scale=100):
        self.x_0 = x_0
        self.y_0 = y_0
        self.paper_format = paper_format
        self.orientation = orientation
        self.scale = scale
            
    def paper_size(self):
        """Funkcja zwraca rozmmiar papieru w formie listy.
        Pierwszy wymiar jest długością krótszego boku, a drugi dłuższego.
        Fromat papieru należy podać w formie, np. "A4" """
        A0 = [841, 1189]
        B0 = [1000, 1414]
        C0 = [917, 1297]

        if (self.paper_format[0] == "A"):
            paper_size = A0
        elif (self.paper_format[0] == "B"):
            paper_size = B0
        elif (self.paper_format[0] == "C"):
            paper_size = C0

        n = int(self.paper_format[1:])

        while n > 0:
            paper_size[paper_size.index(max(paper_size))] = int(
                max(paper_size) / 2)
            n = n - 1

        paper_size.sort()
        return paper_size

    def draw(self):
        """Rysuje obszar i ramkę rysunku. Zwraca współrzędne prawego dolnego narożnika ramki - miejsce wstawienia tabelki - oraz skalę rysunku."""
        # obszar rysunku
        plot_area = [i * self.scale for i in self.paper_size()]
        if self.orientation != "v":
            plot_area.reverse()
        cRECTANG(self.x_0, self.y_0, self.x_0 + plot_area[0], self.y_0 + plot_area[1])

        # ramka rysunku
        odr = self.ODSUNIECIE_RAMKI * self.scale
        mnw = self.ODSUNIECIE_RAMKI * self.scale

        frame_size = [i - 2 * odr for i in plot_area]

        x_1 = self.x_0 + odr
        y_1 = self.x_0 + odr

        if self.paper_format == "A4":
            if self.orientation == "v":
                cRECTANG(x_1 + mnw, y_1, x_1 + frame_size[0], y_1 + frame_size[1])
            else:
                cRECTANG(x_1, y_1, x_1 + frame_size[0], y_1 + frame_size[1] - mnw)
        elif self.paper_format == "A3":
            frame_size.reverse
            if self.orientation == "v":
                cRECTANG(x_1, y_1, x_1 + frame_size[0], y_1 + frame_size[1] - mnw)
            else:
                cRECTANG(x_1 + mnw, y_1, x_1 + frame_size[0], y_1 + frame_size[1])
        else:
            cRECTANG(x_1, y_1, x_1 + frame_size[0], y_1 + frame_size[1])
        return [x_1 + frame_size[0], y_1, self.scale]

    def plot(self):
        pass

# TABELKA RYSUNKU --------------------------------------------------
class InfoTable:
    """Tabelka rysunku zawierająca wszystkie informacje o nim."""

    def __init__(self, x_0=0, y_0=0, scale=100):
        self.x_0 = x_0
        self.y_0 = y_0
        self.scale = scale


    rewizja = "1."
    zmiany = "Nowa stacja"
    data = "12.2017"
    inicjaly = "JD"
    adres_1 = "Wieża BOT-E2/54 wys. całk. H=55,95m"
    adres_2 = "Wierzchucin, 89-512 Iwiec, dz. nr 120 obręb 0013 Wysoka"
    opracowal = "inż. Jan Kowalski"
    nr_stacji = "TUC 0001 X"
    faza = "PROJEKT WYKONAWCZY"
    nazwa_rysunku = "FUNDAMENT cz.1"
    skala = "1:50"
    nr_rysunku = "K04"

    template = [["scrKD_romans",    "Center",   -11120,  6432,  180,    0,  rewizja],
                ["scrKD_romans",    "Left",     -10276, 6432,   180,    0,  zmiany],
                ["scrKD_romans",    "Left",     -3560,  6432,   180,    0,  data],
                ["scrKD_romans",    "Center",   -922,   2845,   240,    0,  data],  # drugie wystąpienie daty
                ["scrKD_romans",    "Center",   -923,   6432,   180,    0,  inicjaly],
                ["scrKD_romans",    "Left",     -11720, 4068,   240,    0,  adres_1],
                ["scrKD_romans",    "Left",     -11720, 3642,   240,    0,  adres_2],
                ["scrKD_romans",    "Left",     -11745, 1216,   200,    0,  opracowal],
                ["scrKD_romans",    "Center",   -7763,  160,    300,    0,  nr_stacji],
                ["scrKD_romans",    "Center",   -1843,  2085,   240,    0,  faza],
                ["scrKD_romans",    "Center",   -7763,  2821,   270,    0,  nazwa_rysunku],
                ["scrKD_romans",    "Center",   -2765,  2845,   240,    0,  skala],
                ["scrKD_romans",    "Center",   -1843,  160,    300,    0,  nr_rysunku]]

    def draw(self):
        """Wstawia tabelkę rysunku"""
        sc = self.scale / 100
        cINSERT("scrKD_tabelka", self.x_0, self.y_0, sc)
        for i in self.template:
            cTEXT(i[0], i[1], self.x_0 + i[2] * sc, self.y_0 + i[3] * sc, i[4] * sc, i[5], i[6])

# RYSUNEK PŁYTY W RZUCIE  --------------------------------------------------
class PlytaBOT:
    ROZSTAW_PRETOW = 250

    def __init__(self, x_0=0, y_0=0, radius=4000):
        self.x_0 = x_0
        self.y_0 = y_0
        self.radius = radius


    def plyta_rzut(self):
        """Rysuje rzut płyty"""
        cCIRCLE(self.x_0, self.y_0, self.radius)
        rd = self.radius - 50    # otulina
        cCIRCLE(self.x_0, self.y_0, rd)


    def zbrojenie_obwodowe(self):
        """Rysuje zbrojenie obwodowe płyty"""
        rd = self.radius - 70    # odległość pierwszego pręta od krawędzi
        cCIRCLE(self.x_0, self.y_0, rd)
        while rd > 1000:
            rd = rd - 200   # rozstaw prętów obwodowych
            cCIRCLE(self.x_0, self.y_0, rd)


    def zbrojenie_promieniste(self):
        """Rysuje zbrojenie promieniste płyty"""
        rd = self.radius - 50
        cLINE(1200 + self.x_0, 0 + self.y_0, rd + self.x_0, 0 + self.y_0)
        kat_pomiedzy_pretami = math.asin(self.ROZSTAW_PRETOW / 2 / rd)
        ilosc_pretow = math.ceil(math.pi / kat_pomiedzy_pretami / 5) * 5
        cARRAYPOLAR(self.x_0, self.y_0, ilosc_pretow)
        return ilosc_pretow

    def draw(self):
        self.plyta_rzut()
        self.zbrojenie_obwodowe()
        self.zbrojenie_promieniste()


# cERASE()
# cLAYER()

ramka_K04 = Frame(1000, 1000)
ramka_K04.draw()

tabelka_K04 = InfoTable(20000,-5000)
tabelka_K04.draw()

plyta_K04 = PlytaBOT()
plyta_K04.draw()


