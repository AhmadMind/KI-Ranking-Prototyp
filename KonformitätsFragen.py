# KonformitätsFragen.py

KONFORMITAETS_FRAGEN = {
    "transparenzgrad": [
        "Sind die Entscheidungsprozesse der KI nachvollziehbar dokumentiert?",
        "Können die Entscheidungen der KI durch Explainable AI-Mechanismen erklärt werden?",
        "Sind die verwendeten Algorithmen öffentlich oder internen Prüfern zugänglich gemacht?",
        "Gibt es visuelle Darstellungen oder Berichte, die die Entscheidungsprozesse für Nutzer verständlich machen?",
        "Wird klar offengelegt, dass Nutzer mit einer KI interagieren?",
        "Werden generierte Inhalte, wie Texte oder Bilder, eindeutig als KI-generiert gekennzeichnet?",
        "Gibt es regelmäßige Schulungen für interne Mitarbeiter, um die Transparenzanforderungen zu verstehen?",
        "Sind die Datenquellen der KI nachvollziehbar und transparent dokumentiert?",
        "Gibt es Mechanismen, die es Nutzern ermöglichen, Entscheidungen der KI in Frage zu stellen oder überprüfen zu lassen?",
        "Wird transparent gemacht, wie Entscheidungen durch Daten beeinflusst werden?"
    ],
    "systemrobustheit_sicherheit": [
        "Wurde das System auf Sicherheitslücken durch Penetrationstests überprüft?",
        "Gibt es Maßnahmen, die Adversarial Attacks (gezielte Manipulationen) verhindern können?",
        "Ist das System robust gegenüber fehlerhaften oder unvollständigen Eingaben?",
        "Werden Sicherheitsrisiken regelmäßig dokumentiert und bewertet?",
        "Sind Schutzmaßnahmen gegen unbefugte Zugriffe oder Datenmanipulation implementiert?",
        "Gibt es Mechanismen zur Erkennung und Abwehr von externen Angriffen auf das System?",
        "Ist das System in der Lage, bei einem Sicherheitsvorfall schnell wiederhergestellt zu werden?",
        "Werden Sicherheitsprotokolle nach jedem Update oder jeder neuen Version aktualisiert und getestet?",
        "Gibt es ein Monitoring-System, das potenzielle Sicherheitsvorfälle in Echtzeit erkennen kann?",
        "Wurden Maßnahmen getroffen, um den Zugriff auf sicherheitskritische Funktionen des Systems zu beschränken?"
    ],
    "ethik": [
        "Werden Bias-Analysen durchgeführt, um algorithmische Verzerrungen zu minimieren?",
        "Gibt es Prozesse, die sicherstellen, dass das System diskriminierungsfrei arbeitet?",
        "Werden unterschiedliche Nutzergruppen berücksichtigt?",
        "Gibt es Mechanismen, die unfaire Entscheidungen automatisch erkennen und melden können?",
        "Wurde die Ethik der KI-Entscheidungen durch externe Experten geprüft?",
        "Gibt es Richtlinien für den ethischen Umgang mit den Daten, die im System verwendet werden?",
        "Werden Nutzer über potenzielle Risiken oder Auswirkungen der KI auf ihr Leben informiert?",
        "Werden ethische Überprüfungen während des gesamten Lebenszyklus der KI regelmäßig durchgeführt?",
        "Gibt es Mechanismen, die sicherstellen, dass Entscheidungen der KI nicht zu unbeabsichtigten Konsequenzen führen?",
        "Werden alle ethischen Vorfälle dokumentiert und analysiert?"
    ],
    "dokumentation": [
        "Sind alle verwendeten Algorithmen und ihre Implementierung umfassend dokumentiert?",
        "Wurden die Datenquellen und ihre Qualität in der Dokumentation beschrieben?",
        "Gibt es eine Versionierung der Dokumentation, die Änderungen über die Zeit nachvollziehbar macht?",
        "Sind die Testergebnisse und Prüfprotokolle des Systems vollständig dokumentiert?",
        "Wurden die technischen Spezifikationen und die Systemarchitektur klar beschrieben?",
        "Werden die Konformitätsprüfungen und ihre Ergebnisse regelmäßig dokumentiert?",
        "Ist die Dokumentation für externe Prüfer oder Regulierungsbehörden leicht zugänglich und verständlich?",
        "Gibt es klare Verantwortlichkeiten für die Pflege und Aktualisierung der Dokumentation?",
        "Werden die Auswirkungen von Updates oder Änderungen am System in der Dokumentation vermerkt?",
        "Ist die Dokumentation so gestaltet, dass sie als Nachweis für Audits und Zertifizierungen dient?"
    ],
    "datenqualitaet": [
        "Werden die verarbeiteten Daten auf Vollständigkeit und Konsistenz überprüft?",
        "Gibt es Mechanismen zur Identifizierung und Korrektur fehlerhafter oder ungenauer Daten?",
        "Wird sichergestellt, dass die Daten aktuell und nicht veraltet sind?",
        "Werden Datenquellen regelmäßig auf ihre Vertrauenswürdigkeit geprüft?",
        "Gibt es Maßnahmen zur Reduzierung von Verzerrungen oder Bias in den Daten?",
        "Werden fehlende oder unzureichende Daten durch robuste Methoden behandelt?",
        "Gibt es ein definiertes Verfahren zur Prüfung und Validierung von Daten vor der Verarbeitung durch die KI?",
        "Wird die Herkunft und Verarbeitungsweise der Daten lückenlos dokumentiert?",
        "Sind Mechanismen vorhanden, um Dubletten oder redundante Daten zu vermeiden?",
        "Werden regelmäßige Audits oder Qualitätstests durchgeführt, um die Integrität der Daten sicherzustellen?"
    ]
}

KONFORMITAETS_GEWICHTUNG = {
    "transparenzgrad": 24,
    "systemrobustheit_sicherheit": 29,
    "ethik": 14,
    "dokumentation": 18,
    "datenqualitaet": 15
}
