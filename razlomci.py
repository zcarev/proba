import streamlit as st

ss = r'''\frac{1}{2}+\frac{2}{3}=\frac{x}{y}'''

st.header('Rješite razlomak:')

cols = st.columns(2)

cols1 = st.columns(2)
with cols[1]:
    with cols1[0]:
        rjx = st.number_input('Unesite brojnik', value=None, step=1)
        if rjx == 1:
            st.write('Bravo! - Točan brojnik')
        else:
            st.write('Unesite točan odgovor za brojnik')

with cols[1]:
    with cols1[1]:
        rjy = st.number_input('Unesite rješenje za y', value=None, step=1)
        if rjy == 2:
            st.write('Bravo! - Točan odgovor za y')
        else:
            st.write('Unesite točan odgovor za y')


ss = ss.replace('x', str(rjx))
ss = ss.replace('y', str(rjy))

#with cols[0]:
st.latex(ss)
