import streamlit as st

def zbroj_razlomaka(zamjene:dict):
    aa = r'''\frac{\text{x1}}{\text{x2}}+\frac{\text{x3}}{\text{x4}}=\frac{\text{x5}}{\text{x6}}'''
    for ii in zamjene.keys():
        aa = aa.replace(ii, zamjene[ii])
    return aa

rj_brojnik = st.number_input('Unesite brojnik', value=None, step=1)
rj_nazivnik = st.number_input('Unesite nazivnik', value=None, step=1)

keys = ['x1', 'x2', 'x3', 'x4', 'x5', 'x6', '+']
values = ['1','2','3','4', str(rj_brojnik), str(rj_nazivnik), '-']
zamjene = dict(map(lambda i,j : (i,j) , keys,values))



st.latex(zbroj_razlomaka(zamjene))
