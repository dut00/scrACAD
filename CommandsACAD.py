"""Ten moduł zawiera komendy wykorzystywane w Audocadzie"""

def cARRAYPOLAR(x_0=0, y_0=0, number_of_items=6, fill_angle=360, rotate_items="Y"):
    """Szyk  biegunowy"""
    print("_arraypolar")
    print("Last")
    print("")
    print(x_0, ",", y_0, sep='')
    print("I")      # Items
    print(number_of_items)
    print("F")      # Fill angle
    print(fill_angle)
    print("ROT")    # ROTate items
    print(rotate_items)
    print("X")      # eXit


def cCIRCLE(x_0=0, y_0=0, radius=1):
    """Okrąg"""
    print("_circle")
    print(x_0, ",", y_0, sep='')
    print(radius)


def cERASE(select="all"):
    """Usuń"""
    print("_erase")
    print(select)
    print("")

def cINSERT(block_name, x_0=0, y_0=0, scale=1, rotation=0):
    """Wstaw blok. Bloki muszą mieć zablokowaną proprcję."""
    print("_insert")
    print(block_name)
    print(x_0, ",", y_0, sep='')
    print(scale)
    # print(scale_y) # pierwotna wersja obsługiwała różne skale na Y, ale rezygnuje z tego, bo powodowoduje to dużo kłopotów
    print(rotation)


def cLAYER(layer="0", color="white", line_type="continuous", line_weight="0.25"):
    """Edytuje lub tworzy (jeśli nie ma) nową warstwę."""
    print("_layer")
    print("make")
    print(layer)
    print("color")      # 0 - 255
    print(color)
    print("")
    print("ltype")
    print(line_type)
    print("")
    print("lweight")    # 0.00 - 2.11
    print(line_weight)
    print("")
    print("")

def cCOLOR(color="bylayer"):
    """Ustawia kolor. Należy podać nazwę koloru lub nr indeksu."""
    print("-color")     # ByLayer, ByBlock, 0 - 255
    print(color)

def cLINETYPE(line_type="bylayer"):
    """Ustawia rodzaj lini."""
    print("-linetype")
    print("set")
    print(line_type)    # ByLayer, ByBlock, Continuous, Dashed, Dot ...

# def cLINETYPESCALE ??????

def cLINEWEIGHT(line_weight="bylayer"):
    print("-lweight")
    print(line_weight)  # ByLayer, ByBlock, 0.00 - 2.11


def cLINE(x_0=0, y_0=0, x_end=100, y_end=100):
    """Linia - jeden segment"""
    print("_line")
    print(x_0, ",", y_0, sep='')
    print(x_end, ",", y_end, sep='')
    print("")


def cRECTANG(x_0=0, y_0=0, x_end=200, y_end=100):
    """Prostokat"""
    print("_rectang")
    print(x_0, ",", y_0, sep='')
    print(x_end, ",", y_end, sep='')


def cTEXT(style="Standard", justify="Left", x_0=0, y_0=0, height=2.5, rotation=0, text="empty"):
    """Tekst jednowierszowy. Styl tekstu nie może mieć z góry ustawionej wysokosci (ma być ustawiona na 0)"""
    print("_text")
    print("s")
    print(style)  # Standard, ...
    print("j")
    # Left, Center, Right, Align, Middle, Fit, TL, TC, TR, ML, MC, MR, BL, BC, BR
    print(justify)
    print(x_0, ",", y_0, sep='')
    print(height)
    print(rotation)
    print(text)
