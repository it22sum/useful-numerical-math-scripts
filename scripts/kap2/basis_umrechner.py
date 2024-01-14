import numpy as np
import struct

def float_to_binary32(number):
    # Konvertiere die Fließkommazahl in eine 32-Bit-Binärzahl nach IEEE-754
    packed = struct.pack('f', number)
    binary = ''.join(f'{b:08b}' for b in packed)
    return binary

def convert_number(number, from_base, to_base):
    # Versuche, den String als mathematischen Ausdruck zu evaluieren
    if isinstance(number, str):
        try:
            number = eval(number)
        except:
            pass  # Wenn es kein gültiger Ausdruck ist, wird dies ignoriert

    # Überprüfe, ob es sich um eine Fließkommazahl handelt
    if isinstance(number, float):
        # Für die Binärkonvertierung von Fließkommazahlen
        if to_base == "bin":
            return float_to_binary32(number)
        else:
            number = round(number)  # Runde für andere Basen

    # Konvertiere die Eingabe in eine Dezimalzahl
    if from_base == "bin":
        number = int(str(number), 2)  # Stelle sicher, dass number ein String ist
    elif from_base == "hex":
        number = int(str(number), 16) # Stelle sicher, dass number ein String ist
    elif from_base == "dec":
        number = int(number)

    # Konvertiere die Dezimalzahl in das Ziel-Zahlensystem
    if to_base == "bin":
        return bin(number)[2:]
    elif to_base == "hex":
        return hex(number)[2:]
    else:
        return str(number)

# Beispiele
print("Dezimal 15 zu Binär:", convert_number("15", "dec", "bin"))
print("Binär 1111 zu Dezimal:", convert_number("1111", "bin", "dec"))
print("Dezimal 255 zu Hexadezimal:", convert_number("255", "dec", "hex"))
print("Hexadezimal ff zu Dezimal:", convert_number("ff", "hex", "dec"))

