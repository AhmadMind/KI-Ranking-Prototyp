# RisikoFragen.py

RISIKO_FRAGEN = {
    "datenschutz_sicherheit": [
        "Werden anonymisierte oder pseudonymisierte Daten genutzt?",
        "Gibt es eine Zugriffskontrolle für gespeicherte Daten?",
        "Werden personenbezogene Daten pseudonymisiert?",
        "Sind die gespeicherten Daten verschlüsselt?",
        "Werden Daten regelmäßig auf Sicherheitslücken überprüft?",
        "Wird ein Audit-Log für alle Datenzugriffe geführt?"
    ],
    "einsatzbereich_risiko": [
        "Wird die KI in einem kritischen Bereich eingesetzt (z. B. Medizin, Justiz, Strafverfolgung)?",
        "Trifft die KI automatisierte Entscheidungen, die Menschen betreffen?",
        "Gibt es direkte Auswirkungen auf Grundrechte oder körperliche Unversehrtheit?",
        "Wird die KI im Gesundheitswesen eingesetzt?",
        "Wird die KI im Finanzsektor eingesetzt (z. B. Kreditbewertung, Versicherungen)?",
        "Wird die KI in der Strafverfolgung oder Justiz eingesetzt?",
        "Wird die KI für kritische Infrastruktur (z. B. Energieversorgung, Verkehr) eingesetzt?",
        "Wird die KI in der Personal- oder Bildungsbranche eingesetzt?",
        "Hat die KI einen Einfluss auf demokratische Prozesse oder Wahlen?"
    ],
    "technische_eigenschaft": [
        "Nutzt die KI biometrische Erkennung oder Überwachungstechnologien?",
        "Arbeitet die KI mit sensiblen oder personenbezogenen Daten?",
        "Setzt die KI Algorithmen zur Verhaltensvorhersage oder Profilbildung ein?",
        "Kann die KI ohne menschliche Aufsicht Entscheidungen treffen?"
    ],
    "transparenz_nachvollziehbarkeit": [
        "Ist dokumentiert, wie die KI zu ihren Entscheidungen kommt?",
        "Gibt es eine Möglichkeit für Nutzer, Entscheidungen anzufechten?",
        "Ist die Funktionsweise der KI für Nutzer verständlich erklärt?",
        "Wird die KI regelmäßig auf Fairness und Bias überprüft?",
        "Hat die KI Mechanismen, um transparente Entscheidungen sicherzustellen?",
        "Wird die Skalierbarkeit der KI aktiv überwacht?"
    ]
}

RISIKO_GEWICHTUNG = {
    "datenschutz_sicherheit": 10,
    "einsatzbereich_risiko": 51,
    "technische_eigenschaft": 47,
    "transparenz_nachvollziehbarkeit": 2,
}

SCHWELLENWERTE = {
    "hoch": (60, 100),
    "mittel": (35, 59),
    "gering": (20, 34),
    "kein": (0, 19),
}
