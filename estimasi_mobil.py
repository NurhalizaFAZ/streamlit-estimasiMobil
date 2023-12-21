import pickle
import streamlit as st

model = pickle.load(open('Estimasi_mobil.sav',  'rb'))

st.title('Estimasi Harga Mobil bekas')

year = st.number_input('Input Tahun Mobil')
mileage = st.number_input('Input Jarak Tempuh Mobil')
tax = st.number_input('Input Pajak Mobil')
mpg = st.number_input('Input Konsumsi BBM Mobil')
engineSize = st.number_input('Input Ukuran Mesin')

predict = ''

if st.button('Estimasi Harga'):
    predict = model.predict(    
        [[year, mileage, tax, mpg, engineSize]]
    )
    st.write ('Estimasi harga mobil bekas dalam ponds: ', predict)
    st.write ('Estimasi harga mobil bekas dalam IDR (Juta) :', predict* 19000)