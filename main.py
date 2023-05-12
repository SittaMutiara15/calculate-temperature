# Library
import streamlit as st
from PIL import Image
# write


st.title (':blue[Perhitungan Kenaikan Titik Didih dan Penurunan Titik Beku]')
with st.sidebar :
    st.image(Image.open('pict 1.png'))
    st.image(Image.open('pict 2.png'))
    st.image(Image.open('pict 3.png'))
pilih = st.selectbox(':blue[Pilih jenis perhitungan]', ('Kenaikan Titik Didih', 'Penurunan Titik Beku'))

if pilih == 'Kenaikan Titik Didih' :
    st.header('Kenaikan Titik Didih')
          
else :
    st.header('Penurunan Titik Beku')
    
st.write("---")
    
molalitas = st.number_input(':blue[Nilai molalitas (m)]')
nilai_tetapan = st.number_input(':blue[Nilai tetapan Kb atau Kf (°C kg/mol)]') 
    

jenis_larutan = st.selectbox(':blue[Pilih jenis larutan]',('Larutan Elektrolit', 'Larutan non Elektrolit'))

if jenis_larutan == 'Larutan Elektrolit' :
    faktor_vant_hoff = st.number_input(':blue[Masukkan nilai faktor vant hoff]')
                                                    
else :
    faktor_vant_hoff = 1
    
st.write(f'faktor vant hoff adalah {faktor_vant_hoff}') 

nilai_perhitungan = molalitas*nilai_tetapan*faktor_vant_hoff
if st.button('Hitung nilai'):
    
    hasil = (f'{nilai_perhitungan}°C')
    
    st.success(f'nilai perhitungan adalah {hasil}') 
