import streamlit as st

st.header('aplikasi penjumlahan bilangan numerik', divider='rainbow')

angka_pertama = st.number_input('masukkan angka pertama')
st.write('The current number is', angka_pertama)

angka_kedua = st.number_input('masukkan angka kedua')
st.write('The current number is', angka_kedua)

operasi_matematika = angka_pertama + angka_kedua
st.write(f"Angka pertama {angka_pertama} x Angka kedua {angka_kedua} = {operasi_matematika}")
