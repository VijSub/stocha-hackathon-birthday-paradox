import math
import random
from collections import Counter

import pandas as pd
import streamlit as st
import matplotlib.pyplot as plt


st.set_page_config(
    page_title="Geburtstagsparadoxon Simulator",
    page_icon="🎂",
    layout="wide",
)


def theoretical_probability(n: int, days: int = 365) -> float:
    """Probability that at least two people share a birthday among n people."""
    if n <= 1:
        return 0.0
    if n > days:
        return 1.0

    prob_no_match = 1.0
    for k in range(n):
        prob_no_match *= (days - k) / days
    return 1.0 - prob_no_match


def simulate_probability(n: int, trials: int, days: int = 365) -> float:
    """Monte Carlo estimate for at least one birthday collision."""
    matches = 0
    for _ in range(trials):
        birthdays = [random.randint(1, days) for _ in range(n)]
        if len(set(birthdays)) < n:
            matches += 1
    return matches / trials


def one_random_group(n: int, days: int = 365):
    birthdays = [random.randint(1, days) for _ in range(n)]
    counts = Counter(birthdays)
    duplicate_days = {day: count for day, count in counts.items() if count >= 2}
    return birthdays, duplicate_days


st.title("🎂 Geburtstagsparadoxon – interaktive Stochastik-Visualisierung")
st.write(
    "Diese App zeigt, warum die Wahrscheinlichkeit für mindestens zwei gleiche Geburtstage "
    "in einer Gruppe viel schneller steigt, als man intuitiv erwartet."
)

with st.sidebar:
    st.header("Einstellungen")
    max_people = st.slider("Maximale Gruppengröße für die Kurve", 10, 100, 60)
    selected_people = st.slider("Gruppengröße für die Simulation", 2, max_people, 23)
    trials = st.slider("Anzahl der Simulationen", 100, 20000, 5000, step=100)
    days = st.selectbox("Anzahl möglicher Geburtstage", [365, 366], index=0)
    st.caption("365 ignoriert Schaltjahre; 366 modelliert sie vereinfacht.")

st.header("1. Die zentrale Frage")
st.latex(r"P(\text{mindestens zwei gleiche Geburtstage})")
st.write(
    "Statt direkt diese Wahrscheinlichkeit zu berechnen, betrachtet man zuerst das Gegenereignis: "
    "Alle Personen haben verschiedene Geburtstage."
)

st.latex(
    r"P(\text{mindestens eine Übereinstimmung}) = 1 - "
    r"\frac{365}{365}\cdot\frac{364}{365}\cdot\frac{363}{365}\cdots"
)

# Main selected result
p_theory = theoretical_probability(selected_people, days)
p_sim = simulate_probability(selected_people, trials, days)

col1, col2, col3 = st.columns(3)
col1.metric("Gruppengröße", selected_people)
col2.metric("Theoretische Wahrscheinlichkeit", f"{p_theory * 100:.2f} %")
col3.metric("Simulierte Wahrscheinlichkeit", f"{p_sim * 100:.2f} %")

st.header("2. Theoretische Kurve")
people_values = list(range(2, max_people + 1))
prob_values = [theoretical_probability(n, days) for n in people_values]

df = pd.DataFrame(
    {
        "Personen": people_values,
        "Wahrscheinlichkeit": prob_values,
        "Wahrscheinlichkeit (%)": [p * 100 for p in prob_values],
    }
)

fig, ax = plt.subplots(figsize=(9, 5))
ax.plot(df["Personen"], df["Wahrscheinlichkeit (%)"], marker="o", markersize=3)
ax.axhline(50, linestyle="--", linewidth=1)
ax.axvline(23, linestyle="--", linewidth=1)
ax.set_xlabel("Anzahl Personen")
ax.set_ylabel("Wahrscheinlichkeit in %")
ax.set_title("Wahrscheinlichkeit für mindestens zwei gleiche Geburtstage")
ax.grid(True, alpha=0.3)
st.pyplot(fig)

st.write(
    "Schon bei **23 Personen** liegt die Wahrscheinlichkeit bei ungefähr **50,7 %**. "
    "Das wirkt überraschend, weil nicht gefragt wird, ob jemand denselben Geburtstag wie eine bestimmte Person hat, "
    "sondern ob irgendein Paar in der Gruppe übereinstimmt."
)

st.header("3. Monte-Carlo-Simulation")
st.write(
    "Die Simulation erzeugt viele zufällige Gruppen und zählt, wie oft mindestens zwei Personen denselben Geburtstag haben. "
    "Je mehr Durchläufe verwendet werden, desto näher kommt das Ergebnis meistens an den theoretischen Wert."
)

sim_rows = []
for n in people_values:
    sim_rows.append(
        {
            "Personen": n,
            "Theorie (%)": theoretical_probability(n, days) * 100,
            "Simulation (%)": simulate_probability(n, max(200, trials // 10), days) * 100,
        }
    )

sim_df = pd.DataFrame(sim_rows)
fig2, ax2 = plt.subplots(figsize=(9, 5))
ax2.plot(sim_df["Personen"], sim_df["Theorie (%)"], label="Theorie")
ax2.scatter(sim_df["Personen"], sim_df["Simulation (%)"], s=12, label="Simulation")
ax2.set_xlabel("Anzahl Personen")
ax2.set_ylabel("Wahrscheinlichkeit in %")
ax2.set_title("Theorie vs. Simulation")
ax2.grid(True, alpha=0.3)
ax2.legend()
st.pyplot(fig2)

st.header("4. Eine zufällige Beispielgruppe")
birthdays, duplicates = one_random_group(selected_people, days)
example_df = pd.DataFrame(
    {
        "Person": [f"Person {i + 1}" for i in range(selected_people)],
        "Geburtstag als Tag im Jahr": birthdays,
    }
)
st.dataframe(example_df, use_container_width=True)

if duplicates:
    st.success(
        "In dieser zufälligen Gruppe gibt es gleiche Geburtstage: "
        + ", ".join([f"Tag {day}: {count} Personen" for day, count in duplicates.items()])
    )
else:
    st.info("In dieser zufälligen Gruppe gibt es keine gleichen Geburtstage.")

st.header("5. Fazit")
st.write(
    "Das Geburtstagsparadoxon zeigt, dass unsere Intuition bei Wahrscheinlichkeiten oft täuscht. "
    "Der Grund ist die große Anzahl möglicher Paare in einer Gruppe: Bei n Personen gibt es n·(n−1)/2 Paarvergleiche. "
    "Dadurch wird eine Übereinstimmung viel schneller wahrscheinlich, als man zunächst denkt."
)

st.caption("Erstellt für den StochaHackathon – Open Source, kostenlos nutzbar und leicht lokal ausführbar.")
