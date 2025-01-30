import numpy as np
from RisikoFragen import RISIKO_FRAGEN, RISIKO_GEWICHTUNG, SCHWELLENWERTE
from KonformitätsFragen import KONFORMITAETS_FRAGEN, KONFORMITAETS_GEWICHTUNG

# ----- Antwortoptionen mit automatischer Punktevergabe -----
RISIKO_ANTWORTEN = {
    "Trifft nicht zu": 0,
    "Trifft teilweise nicht zu": 1,
    "Mittel": 2,
    "Trifft teilweise zu": 3,
    "Trifft zu": 4
}

KONFORMITAETS_ANTWORTEN = {
    "Nicht erfüllt": 0,
    "Teilweise erfüllt": 1,
    "Vollständig erfüllt": 2
}


def fragebogen_ausfuellen(fragen_dict, antwort_möglichkeiten):
    """
    Führt den Nutzer durch einen interaktiven Fragebogen.
    Der Nutzer wählt eine Antwortoption, die in Punkte umgewandelt wird.
    """
    antworten = {}
    print("\nBitte beantworten Sie die folgenden Fragen:")

    for kategorie, fragen in fragen_dict.items():
        print(f"\n=== {kategorie.upper()} ===")
        antworten[kategorie] = []

        for frage in fragen:
            print(f"\n{frage}")
            for idx, option in enumerate(antwort_möglichkeiten.keys(), start=1):
                print(f"{idx}. {option}")

            while True:
                try:
                    auswahl = int(input("Wählen Sie eine Option (1-{}): ".format(len(antwort_möglichkeiten))))
                    if 1 <= auswahl <= len(antwort_möglichkeiten):
                        antworten[kategorie].append(list(antwort_möglichkeiten.values())[auswahl - 1])
                        break
                    else:
                        print("❌ Ungültige Eingabe. Bitte eine Zahl zwischen 1 und {} eingeben.".format(len(antwort_möglichkeiten)))
                except ValueError:
                    print("❌ Bitte eine gültige Zahl eingeben.")

    return antworten


# ---- Risikoanalyse ----
def berechne_risikowertung(antworten):
    """
    Berechnet die Risikowertung basierend auf den gegebenen Antworten (0-4 Skala).
    """
    gesamt_score = 0
    max_möglicher_score = sum(RISIKO_GEWICHTUNG.values()) * 4  # Jede Frage hat max. 4 Punkte

    for kategorie, gewichtung in RISIKO_GEWICHTUNG.items():
        if kategorie in antworten:
            score = np.mean(antworten[kategorie]) * gewichtung  # Durchschnittswerte gewichten
            gesamt_score += score

    risiko_prozent = (gesamt_score / max_möglicher_score) * 100
    return risiko_prozent


def bestimme_risikoklasse(score):
    """
    Bestimmt die Risikoklasse basierend auf dem errechneten Score.
    """
    for klasse, (min_wert, max_wert) in SCHWELLENWERTE.items():
        if min_wert <= score <= max_wert:
            return klasse
    return "Unbekannt"


# ---- Konformitätsbewertung ----
def berechne_konformitätsbewertung(antworten):
    """
    Berechnet die Konformitätsbewertung basierend auf den gegebenen Antworten (0-2 Skala).
    """
    gesamt_score = 0
    max_mögliche_punkte = sum(KONFORMITAETS_GEWICHTUNG.values()) * 20  # Jede Kategorie hat max. 20 Punkte

    for kategorie, gewichtung in KONFORMITAETS_GEWICHTUNG.items():
        if kategorie in antworten:
            score = np.sum(antworten[kategorie]) * gewichtung  # Punkte gewichtet summieren
            gesamt_score += score

    return gesamt_score / max_mögliche_punkte * 100  # Umrechnung in Prozent


def berechne_konformitätsbewertung_in_prozent(konformität_score, risikoklasse):
    """
    Berechnet die endgültige Konformitätsbewertung in % basierend auf der Risikoklasse.
    """
    if risikoklasse == "kein":
        return min(100, konformität_score)  # Lineare Funktion
    elif risikoklasse == "gering":
        return min(100, 0.01 * (konformität_score ** 2))  # Quadratische Funktion
    elif risikoklasse == "mittel":
        return min(100, 0.0001 * (konformität_score ** 3))  # Kubische Funktion
    elif risikoklasse == "hoch":
        return min(100, 100 * (konformität_score / 100) ** 4)  # Exponentielle Funktion
    return 0


if __name__ == "__main__":
    print("\n===== RISIKOKLASSIFIZIERUNG =====")
    antworten_risiko = fragebogen_ausfuellen(RISIKO_FRAGEN, RISIKO_ANTWORTEN)

    # 1. Berechnung der Risikoklasse
    risiko_score = berechne_risikowertung(antworten_risiko)
    risikoklasse = bestimme_risikoklasse(risiko_score)

    print("\n===== KONFORMITÄTSBEWERTUNG =====")
    antworten_konformität = fragebogen_ausfuellen(KONFORMITAETS_FRAGEN, KONFORMITAETS_ANTWORTEN)

    # 2. Berechnung der Konformitätsbewertung
    konformitäts_score = berechne_konformitätsbewertung(antworten_konformität)

    # 3. Berechnung der finalen Konformitätsbewertung in %
    konformitätsbewertung_prozent = berechne_konformitätsbewertung_in_prozent(konformitäts_score, risikoklasse)

    # Ergebnisse ausgeben
    print("\n===== ERGEBNISSE =====")
    print(f"🔹 Berechneter Risiko-Score: {risiko_score:.2f}%")
    print(f"🔹 Risikoklasse: {risikoklasse}")
    print(f"🔹 Konformitätsbewertung: {konformitäts_score:.2f} Punkte")
    print(f"🔹 Konformitätsbewertung in %: {konformitätsbewertung_prozent:.2f}%")
