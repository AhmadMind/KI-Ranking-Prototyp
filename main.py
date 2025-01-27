from questions import QUESTIONS

class KIScoringSystem:
    def __init__(self):
        self.risk_criteria = {
            "Anwendungsbereich": 0,
            "Auswirkungen auf Menschen": 0,
            "Fehlerfolgen": 0,
            "Automatisierungsgrad": 0,
            "Transparenzanforderungen": 0,
            "Datennutzung": 0,
        }
        self.categories = {
            "Transparenz": [],
            "Sicherheit": [],
            "Ethik": [],
            "Dokumentation": []
        }
        self.weights = {
            "Transparenz": 0.35,
            "Sicherheit": 0.35,
            "Ethik": 0.20,
            "Dokumentation": 0.10
        }
        self.questions = QUESTIONS

    def classify_risk(self):
        print("\nRisikoklassifizierung:")

        # Anwendungsbereich
        print("Anwendungsbereich:")
        print("1: Medizinischer Bereich")
        print("2: Verkehr")
        print("3: Justiz")
        print("4: Bildung")
        print("5: Verbraucherdienste")
        print("6: Andere (weniger sensibel)")
        while True:
            try:
                choice = int(input("Bitte wählen Sie einen Anwendungsbereich (1-6): "))
                if choice in [1, 2, 3, 4, 5, 6]:
                    break
                else:
                    print("Ungültige Eingabe. Bitte wählen Sie eine Zahl zwischen 1 und 6.")
            except ValueError:
                print("Ungültige Eingabe. Bitte geben Sie eine Zahl ein.")

        if choice == 1:
            self.risk_criteria["Anwendungsbereich"] = 5
        elif choice == 2:
            self.risk_criteria["Anwendungsbereich"] = 5
        elif choice == 3:
            self.risk_criteria["Anwendungsbereich"] = 5
        elif choice == 4:
            self.risk_criteria["Anwendungsbereich"] = 3
        elif choice == 5:
            self.risk_criteria["Anwendungsbereich"] = 2
        else:
            self.risk_criteria["Anwendungsbereich"] = 1

        # Auswirkungen auf Menschen
        print("\nHat die KI potenziell Auswirkungen auf die Rechte und Freiheiten von Menschen?")
        print("1: Keine Auswirkungen")
        print("2: Geringe Auswirkungen")
        print("3: Moderate Auswirkungen")
        print("4: Hohe Auswirkungen")
        print("5: Kritische Auswirkungen")
        while True:
            try:
                impact = int(input("Wählen Sie eine Stufe (1-5): "))
                if impact in [1, 2, 3, 4, 5]:
                    self.risk_criteria["Auswirkungen auf Menschen"] = impact
                    break
                else:
                    print("Ungültige Eingabe. Bitte wählen Sie eine Zahl zwischen 1 und 5.")
            except ValueError:
                print("Ungültige Eingabe. Bitte geben Sie eine Zahl ein.")

        # Fehlerfolgen
        print("\nWie schwerwiegend wären mögliche Fehlerfolgen?")
        print("1: Keine schwerwiegenden Folgen")
        print("2: Geringe Folgen")
        print("3: Moderate Folgen")
        print("4: Hohe Folgen")
        print("5: Kritische Folgen")
        while True:
            try:
                consequences = int(input("Wählen Sie eine Stufe (1-5): "))
                if consequences in [1, 2, 3, 4, 5]:
                    self.risk_criteria["Fehlerfolgen"] = consequences
                    break
                else:
                    print("Ungültige Eingabe. Bitte wählen Sie eine Zahl zwischen 1 und 5.")
            except ValueError:
                print("Ungültige Eingabe. Bitte geben Sie eine Zahl ein.")

        # Automatisierungsgrad
        print("\nWie hoch ist der Automatisierungsgrad der KI?")
        print("1: Unterstützend (nur Empfehlungen)")
        print("2: Teilweise automatisiert")
        print("3: Überwiegend automatisiert")
        print("4: Vollautomatisch mit menschlicher Überprüfung")
        print("5: Vollautomatisch ohne menschliche Überprüfung")
        while True:
            try:
                automation = int(input("Wählen Sie eine Stufe (1-5): "))
                if automation in [1, 2, 3, 4, 5]:
                    self.risk_criteria["Automatisierungsgrad"] = automation
                    break
                else:
                    print("Ungültige Eingabe. Bitte wählen Sie eine Zahl zwischen 1 und 5.")
            except ValueError:
                print("Ungültige Eingabe. Bitte geben Sie eine Zahl ein.")

        # Transparenzanforderungen
        print("\nWie transparent ist die Entscheidungsfindung der KI?")
        print("1: Vollständig transparent")
        print("2: Weitgehend transparent")
        print("3: Teilweise transparent")
        print("4: Geringe Transparenz")
        print("5: Keine Transparenz (Black-Box)")
        while True:
            try:
                transparency = int(input("Wählen Sie eine Stufe (1-5): "))
                if transparency in [1, 2, 3, 4, 5]:
                    self.risk_criteria["Transparenzanforderungen"] = transparency
                    break
                else:
                    print("Ungültige Eingabe. Bitte wählen Sie eine Zahl zwischen 1 und 5.")
            except ValueError:
                print("Ungültige Eingabe. Bitte geben Sie eine Zahl ein.")

        # Datennutzung
        print("\nVerarbeitet die KI sensible oder personenbezogene Daten?")
        print("1: Keine Daten")
        print("2: Wenig sensible Daten")
        print("3: Moderate Menge sensibler Daten")
        print("4: Viele sensible Daten")
        print("5: Kritische personenbezogene Daten")
        while True:
            try:
                data_usage = int(input("Wählen Sie eine Stufe (1-5): "))
                if data_usage in [1, 2, 3, 4, 5]:
                    self.risk_criteria["Datennutzung"] = data_usage
                    break
                else:
                    print("Ungültige Eingabe. Bitte wählen Sie eine Zahl zwischen 1 und 5.")
            except ValueError:
                print("Ungültige Eingabe. Bitte geben Sie eine Zahl ein.")

        total_risk_score = sum(self.risk_criteria.values())
        if total_risk_score >= 21:
            return "Hochrisiko"
        elif total_risk_score >= 11:
            return "Begrenztes Risiko"
        else:
            return "Minimal"

    def evaluate_category(self, category):
        print(f"\nFragenkatalog für {category}:")
        scores = []
        for i, question in enumerate(self.questions[category], 1):
            while True:
                print(f"Frage {i}: {question}")
                try:
                    score = int(input("Punkte (0-2): "))
                    if score not in [0, 1, 2]:
                        print("Ungültige Eingabe. Bitte geben Sie 0, 1 oder 2 ein.")
                    else:
                        scores.append(score)
                        break
                except ValueError:
                    print("Ungültige Eingabe. Bitte geben Sie eine Zahl ein.")
        self.categories[category] = scores

    def calculate_scores(self):
        normalized_scores = {}
        total_compliance_score = 0

        for category, scores in self.categories.items():
            category_score = sum(scores) / (2 * len(scores))  # Maximal 20 Punkte pro Kategorie
            normalized_scores[category] = category_score
            total_compliance_score += category_score * self.weights[category]

        return normalized_scores, total_compliance_score

    def run(self):
        print("Willkommen zum KI Scoring System!\n")

        # Schritt 1: Risikoklassifizierung
        risk_level = self.classify_risk()
        print(f"\nRisikostufe: {risk_level}\n")

        # Schritt 2: Fragenkatalog ausfüllen
        for category in self.categories.keys():
            self.evaluate_category(category)

        # Schritt 3: Konformitätsbewertung
        normalized_scores, total_compliance_score = self.calculate_scores()

        # Schritt 4: Ergebnisse anzeigen
        print("\nDie Score:")
        print(f"Risikostufe: {risk_level}")
        for category, score in normalized_scores.items():
            print(f"{category} Score: {score * 100:.0f}%")
        print(f"Konformitätsbewertung: {total_compliance_score * 100:.0f}%")

        if risk_level == "Hochrisiko" and total_compliance_score >= 0.95:
            print("Status: Konform")
        elif risk_level == "Begrenztes Risiko" and total_compliance_score >= 0.75:
            print("Status: Konform")
        elif risk_level == "Minimal" and total_compliance_score >= 0.60:
            print("Status: Konform")
        else:
            print("Status: Nicht konform")

# Anwendung ausführen
if __name__ == "__main__":
    system = KIScoringSystem()
    system.run()
