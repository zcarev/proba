import streamlit as st
import numpy as np


# Funkcija za generiranje zadataka
def generiraj_zadatke():
    zadaci = []
    dekadske_jedinice = [10, 100, 1000, 10000]
    for _ in range(10):
        broj = np.round(np.random.uniform(0.1, 10), 3)
        dekadska_jedinica = np.random.choice(dekadske_jedinice)
        zadaci.append((broj, dekadska_jedinica))
    return zadaci

# Provjera je li zadaci već postoje u session_state
if 'zadaci' not in st.session_state:
    st.session_state.zadaci = generiraj_zadatke()

# Funkcija za provjeru odgovora
def provjeri_odgovore(zadaci, odgovori):
    tocan = 0
    for (broj, dekadska_jedinica), odgovor in zip(zadaci, odgovori):
        try:
            if np.round(broj * dekadska_jedinica, 3) == np.round(float(odgovor.replace(',', '.')), 3):
                tocan += 1
        except ValueError:
            pass
    return tocan

st.title("Provjera znanja množenja decimalnih brojeva s dekadskim jedinicama")

ime = st.text_input("Unesite svoje ime:")
odgovori = []
for i, (broj, dekadska_jedinica) in enumerate(st.session_state.zadaci):
    odgovor = st.text_input(f"Zadatak {i+1}: {broj} * {dekadska_jedinica} =", "")
    odgovori.append(odgovor)

if st.button("Provjeri odgovore"):
    tocan = provjeri_odgovore(st.session_state.zadaci, odgovori)
    st.write(f"Točno ste riješili {tocan} od 10 zadataka.")
    if ime:
        st.write("Rezultati su spremljeni.")

if st.button("Novi zadaci"):
    st.session_state.zadaci = generiraj_zadatke()
