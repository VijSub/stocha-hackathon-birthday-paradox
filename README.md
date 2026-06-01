# Geburtstagsparadoxon Simulator

Ein interaktives Python/Streamlit-Projekt für den StochaHackathon.

## Idee

Das Programm visualisiert das Geburtstagsparadoxon: Ab wie vielen Personen ist es wahrscheinlich, dass mindestens zwei Personen denselben Geburtstag haben?

Die App kombiniert:

- eine theoretische Berechnung,
- eine Monte-Carlo-Simulation,
- interaktive Parameter,
- Diagramme,
- und eine zufällige Beispielgruppe.

## Stochastischer Hintergrund

Gesucht ist die Wahrscheinlichkeit

```text
P(mindestens zwei gleiche Geburtstage)
```

Es ist einfacher, zuerst das Gegenereignis zu berechnen:

```text
P(alle Geburtstage verschieden)
```

Für n Personen und 365 mögliche Geburtstage gilt:

```text
P(alle verschieden) = 365/365 * 364/365 * 363/365 * ... * (365-n+1)/365
```

Daher:

```text
P(mindestens eine Übereinstimmung) = 1 - P(alle verschieden)
```

Bei 23 Personen ergibt sich bereits eine Wahrscheinlichkeit von ungefähr 50,7 %.

## Installation

Voraussetzung: Python 3.10 oder neuer.

1. Repository herunterladen oder klonen.
2. In den Projektordner wechseln.
3. Abhängigkeiten installieren:

```bash
pip install -r requirements.txt
```

4. App starten:

```bash
streamlit run app.py
```

Danach öffnet sich die App im Browser.

## Dateien

- `app.py`: Hauptprogramm
- `requirements.txt`: kostenlose Python-Abhängigkeiten
- `README.md`: Installationsanleitung und Erklärung
- `LICENSE`: Open-Source-Lizenz