import math

import pandas as pd

# Angepasste Funktion zur Fixpunktiteration
def fixpunkt_iteration_verlauf(g, startwert, toleranz, max_iter):
    verlauf = []
    x_alt = startwert
    for i in range(max_iter):
        x_neu = g(x_alt)
        if abs(x_neu) > 1e10:  # Abbruch bei zu großem Wert
            break
        verlauf.append((i, x_alt, x_neu))
        if abs(x_neu - x_alt) < toleranz:
            break
        x_alt = x_neu
    return verlauf

# Funktion zur Erstellung einer verbesserten Tabelle
def erstelle_tabelle(g, startwerte, toleranz, max_iter):
    tabelle = []
    for wert in startwerte:
        verlauf = fixpunkt_iteration_verlauf(g, wert, toleranz, max_iter)
        for schritt in verlauf:
            n, x_alt, x_neu = schritt
            # Erweitere die Tabelle um den aktuellen Iterationsschritt
            while len(tabelle) <= n:
                tabelle.append({})
            tabelle[n][f"x_alt ({wert})"] = x_alt
            tabelle[n][f"x_neu ({wert})"] = x_neu
    return tabelle

# Definiert die Funktion g für die Fixpunktiteration
def g(x):
    return 2*math.sin(x)

# Parameter
startwerte = [-1, 0, 1]  # Verschiedene Startwerte
toleranz = 1e-3
max_iter = 30

# Tabelle erstellen und in DataFrame umwandeln
tabelle = erstelle_tabelle(g, startwerte, toleranz, max_iter)
df_tabelle = pd.DataFrame(tabelle)

# Ausgabe der Tabelle
print(df_tabelle)
