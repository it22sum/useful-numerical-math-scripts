def anz_verschied_maschinZahlen(basis, mantisse, exponent, vorzeichen_exp):
    """
    Funktion zum Berechnen der Anzahl verschiedener Maschinenzahlen in einem numerischen System.

    :param basis: Basis des Zahlenformats, z.B. 10 für dezimales, 2 für binäres System.
    :param mantisse: Anzahl der Stellen in der Mantisse. Die effektive Länge der Mantisse ist `mantisse - 1`,
                     wenn ein hidden bit berücksichtigt wird.
    :param exponent: Anzahl der Stellen im Exponententeil des Formats.
    :param vorzeichen_exp: Gibt an, ob der Exponent ein Vorzeichen hat. 0 für nein, 1 für ja.

    :return: Gibt die Gesamtzahl der verschiedenen Maschinenzahlen zurück, die in dem spezifizierten
             numerischen Format dargestellt werden können. Dies umfasst alle Kombinationen von Mantisse,
             Exponent und Vorzeichen (falls vorhanden).

    Die Berechnung basiert auf der Formel:
    basis^(mantisse - 1) * (basis^(exponent + vorzeichen_exp) - 1) + 1
    Hierbei wird die Anzahl der möglichen Werte für die Mantisse und den Exponenten (inklusive Vorzeichen) berechnet.
    Das zusätzliche +1 berücksichtigt den Fall der Darstellung der Zahl Null.
    """
    return basis ** (mantisse) * (basis ** (exponent + vorzeichen_exp) - 1) + 1

if __name__ == '__main__':
    # Beispiel aus Prüfung FS20 Aufgabe 1a)

    anzahl = anz_verschied_maschinZahlen(2, 15, 5, 1)
    print(anzahl)