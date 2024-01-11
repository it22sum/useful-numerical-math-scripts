import pandas as pd

# Anpassung der Fixpunktiteration, um den Overflow zu vermeiden
def fixpunkt_iteration_verlauf(g, startwert, toleranz, max_iter):
    verlauf = []
    x_alt = startwert
    for i in range(max_iter):
        x_neu = g(x_alt)
        # Hinzugefügt: Abbruch, wenn x_neu zu groß wird, um Overflow zu vermeiden
        if abs(x_neu) > 1e10:
            break
        verlauf.append((i, x_alt, x_neu))
        if abs(x_neu - x_alt) < toleranz:
            break
        x_alt = x_neu
    return verlauf

# Funktion zur Erstellung einer Tabelle für mehrere Startwerte
def erstelle_tabelle(g, startwerte, toleranz, max_iter):
    tabelle = []
    for wert in startwerte:
        verlauf = fixpunkt_iteration_verlauf(g, wert, toleranz, max_iter)
        # Erweitern der Liste für jeden Iterationsschritt
        for i, (n, x_alt, x_neu) in enumerate(verlauf):
            # Füge die Iterationsergebnisse in die Tabelle ein
            while len(tabelle) <= i:  # Sicherstellen, dass die Liste lang genug ist
                tabelle.append({})
            tabelle[i][wert] = x_neu
    return tabelle


# Definiert die Funktion g für die Fixpunktiteration
def g(x):
    return x**3 + 0.3

# Parameter
startwerte = [-1, 0, 1]  # Verschiedene Startwerte
toleranz = 1e-10
max_iter = 15

# Tabelle erstellen
tabelle = erstelle_tabelle(g, startwerte, toleranz, max_iter)

# Umwandlung in DataFrame für die Ausgabe
df_tabelle = pd.DataFrame(tabelle)

print(df_tabelle)
