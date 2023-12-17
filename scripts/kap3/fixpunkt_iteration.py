def g(x):
    # Ersetzen durch eine geeignete Umformung der Funktion f(x)
    return x**3+0.3





def finde_nullstellen_mit_fixpunktiteration(g, startwerte, toleranz, max_iter):
    def anzahl_nachkommastellen(zahl):
        from decimal import Decimal
        # Convert the number to a Decimal, which can handle arbitrary precision
        number_as_decimal = Decimal(str(zahl))

        # Check if the number is an integer, in which case return 0
        if number_as_decimal == number_as_decimal.to_integral():
            return 0

        # Convert to a string, ensuring no scientific notation
        number_str = format(number_as_decimal, 'f')

        # Count the number of characters after the decimal point
        decimal_places = len(number_str.split('.')[1])

        return decimal_places
    #-------------------------------------------------------------------
    def fixpunkt_iteration(g, startwert, toleranz, max_iter):
        x_alt = startwert
        for i in range(max_iter):
            x_neu = g(x_alt)
            if abs(x_neu - x_alt) < toleranz:
                return x_neu, i
            x_alt = x_neu

            if x_neu > 1e10:
                return None, i

        return x_neu, max_iter
    #-------------------------------------------------------------------

    gefundene_nullstellen = []
    for startwert in startwerte:
        nullstelle, iterationen = fixpunkt_iteration(g, startwert, toleranz, max_iter)
        if nullstelle is not None:
            if iterationen < max_iter:
                # Überprüfen, ob die Nullstelle bereits gefunden wurde
                if not any(abs(nullstelle - n) < toleranz for n in gefundene_nullstellen):
                    gefundene_nullstellen.append(round(nullstelle, anzahl_nachkommastellen(toleranz)))
    return gefundene_nullstellen



# Parameter
startwerte = [-1, 0, 1]  # Verschiedene Startwerte
toleranz = 1e-10
max_iter = 50


#print(fixpunkt_iteration(g, 0, toleranz, max_iter))

# Nullstellen finden
nullstellen = finde_nullstellen_mit_fixpunktiteration(g, startwerte, toleranz, max_iter)
for nullstelle in nullstellen:
    print(f"Nullstelle gefunden bei: {nullstelle}")
