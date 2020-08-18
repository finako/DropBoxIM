#In dieser Datei werden Funktions- und Klassendefinitionen ausgelagert, um das eigentliche Chatprogramm übersichtlicher zu gestalten
from contextlib import suppress

"""
entferne_sonderzeichtn(string):
    entfernt Sonderzeichen (wie z.B. Umlaute) aus dem gegebenen [string] und ersetzt sie durch ASCII-Zeichenabfolgen

sonderzeichen(string):
    kehrt die Wirkung von entferne_sonderzeichen() wieder um

Klasse Nachricht:
    erzeugt ein Nachrichtenobjekt, das verwendet wird, um Nachrichten besser sortieren zu könnet, etc.
    Verwendung:
        - beim Initialisieren eines Nachrichtenobjekts muss der Klasse eine Nachricht der Syntax "hh:mm:ss;nickname::inhalt"(ohne ';') als String übergeben werden
        - bei Aufruf des Objekts gibt es sich selbst zurück
        - die Klassenfunktion gesamt() gib die Nachricht in Form eines Strings zurück, in der Syntax: "hh:mm:ss Name> Inhalt"

sortieren(nachrichtenliste):
    sortiert die gegebene [nachrichtenliste], die aus Nachrichtenobjekten bestehen muss, nach Uhrzeit

erzeuge_nachrichtenliste(*dateien):
    erzeugt aus beliebig vielen gegebenen [dateien], die in jeder Zeile eine Nachricht enthalten, eine Liste aus Nachrichtenobjekten
"""

def entferne_sonderzeichen(string):
    ersetzen = [("ö", "<&oe&>"), ("ä", "<&ae&>"), ("ü", "<&ue&>"), ("Ö", "<&Oe&>"), ("Ä", "<&Ae&>"),
    ("Ü", "<&Ue&>"), ("§", "<&paragraph&>"), ("$", "<&dollar&>"), ("<br>", "<&NL&>"), ("µ", "<&mycro&>"),
    ("²", "<&superscript2&>"), ("³", "<&superscript3&>"), ("€", "<&euro&>"), ("°", "<&degree&>")]
    for element in ersetzen:
        string = string.replace(element[0], element[1])
    return string

def sonderzeichen(string):
    ersetzen = [("<&oe&>", "ö"), ("<&ae&>", "ä"), ("<&ue&>", "ü"), ("<&Oe&>", "Ö"), ("<&Ae&>", "Ä"), ("<&Ue&>", "Ü"),
    ("<&paragraph&>", "§"), ("<&dollar&>", "$"), ("<&NL&>", "\n"), ("<&mycro&>", "µ"), ("<&superscript2&>", "²"),
    ("<&superscript3&>", "³"), ("<&euro&>", "€"), ("<&degree&>", "°")]
    for element in ersetzen:
        string = string.replace(element[0], element[1])
    return string

class Nachricht:
    def __init__(self, nachricht):
        self.stunde = nachricht[:2]
        self.minute = nachricht[3:5]
        self.sekunde = nachricht[6:8]
        self.name = nachricht[8:nachricht.find("::")]
        self.inhalt = nachricht[nachricht.find("::")+2:]
        #Syntax: 12:33:27Nickname::Inhalt
    def __repr__(self):
        return repr((self.stunde, self.minute, self.sekunde, self.name, self.inhalt))
    def gesamt(self):
        return self.stunde + ":" + self.minute + ":" + self.sekunde + " " + self.name + "> " + self.inhalt

def sortieren(nachrichtenliste):
    with suppress(TypeError):
        return sorted(sorted(sorted(nachrichtenliste, key=lambda nachricht: nachricht.sekunde), key=lambda nachricht: nachricht.minute), key=lambda nachricht: nachricht.stunde)

def erzeuge_nachrichtenliste(*dateien):
    liste = []
    for file in dateien:
        with open(file, "r") as f:
            for zeile in f.readlines():
                liste.append(Nachricht(zeile))
    return liste

def isOnly(string, allowedChars, caseSensitive=True):
    counter = 0
    string = str(string)
    if caseSensitive == False:
        string = string.lower()
        allowedChars = allowedChars.lower()
    for char in allowedChars:
        counter += string.count(char)
    if counter == len(string):
        return True
    elif counter != len(string):
        return False
    else:
        return None