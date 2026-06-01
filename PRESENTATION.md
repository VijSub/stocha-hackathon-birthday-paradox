# Präsentation / Erklärung für die Abgabe

## Titel
Geburtstagsparadoxon – Warum 23 Personen schon reichen

## Problem
Viele Menschen glauben intuitiv, dass man sehr viele Personen braucht, bis zwei Personen denselben Geburtstag haben. Das Geburtstagsparadoxon zeigt aber: Schon bei 23 Personen liegt die Wahrscheinlichkeit bei ungefähr 50 Prozent.

## Idee
Das Programm berechnet und simuliert die Wahrscheinlichkeit, dass in einer Gruppe mindestens zwei Personen denselben Geburtstag haben.

## Mathematischer Ansatz
Direkt zu berechnen, dass mindestens zwei Personen denselben Geburtstag haben, ist unübersichtlich. Deshalb berechnet man zuerst das Gegenereignis: Alle Personen haben verschiedene Geburtstage.

Für n Personen gilt:

P(mindestens eine Übereinstimmung) = 1 - P(alle Geburtstage verschieden)

Für 365 Tage:

P(alle verschieden) = 365/365 · 364/365 · 363/365 · ... · (365-n+1)/365

## Simulation
Zusätzlich zur Formel verwendet die App eine Monte-Carlo-Simulation:

1. Es werden zufällige Geburtstage für n Personen erzeugt.
2. Das Programm prüft, ob mindestens ein Geburtstag doppelt vorkommt.
3. Dieser Vorgang wird viele Male wiederholt.
4. Der Anteil der Treffer approximiert die gesuchte Wahrscheinlichkeit.

## Ergebnis
Die App zeigt, dass die Wahrscheinlichkeit sehr schnell steigt. Bei 23 Personen beträgt sie ungefähr 50,7 Prozent. Der Grund ist, dass bei n Personen sehr viele Paare verglichen werden: n·(n−1)/2.

## Warum ist das interessant?
Das Beispiel zeigt sehr anschaulich, dass menschliche Intuition bei Wahrscheinlichkeiten oft falsch liegt. Gleichzeitig verbindet es Theorie, Simulation und Visualisierung.
