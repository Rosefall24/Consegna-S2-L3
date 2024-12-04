def genera_nome_band(citta, animale):
    # Combina i due input in vari modi per creare un nome interessante
    nome_band = citta.capitalize() + " " + animale.capitalize()
    return nome_band

# Input
citta = input("Inserisci la tua città di origine: ")
animale = input("Inserisci il nome del tuo animale domestico: ")

# Generazione
nome_band = genera_nome_band(citta, animale)
print("Il nome della tua band potrebbe essere:", nome_band)
