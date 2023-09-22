import streamlit as st
import pandas as pd
import numpy as np
import pickle
from functions.predict import predict

# make center
st.markdown("""
<style>
.center {
    text-align: center;

}
</style>
""", unsafe_allow_html=True)
st.markdown('<h1 class="center">Aplikasi Prediksi Kanker Payudara Menggunakan Support Vector Machine (SVM)</h1>', unsafe_allow_html=True)

# write html
st.markdown("""
<br><h4 class="center">Nama Pembuat:</h4>
<p class="center">1. Puspita Kartikasari, S.Si., M.Si.</p>
<p class="center">2. Iut Tri Utami, S.Si., M.Si.</p>
<p class="center">3. Dra. Suparti, M.Si.</p>
<p class="center">4. Syair Dafiq Faizur Rahman</p>
""", unsafe_allow_html=True)

st.markdown("""
<br> <h3 class="center">DEPARTEMEN STATISTIKA <br> FAKULTAS SAINS DAN MATEMATIKA <br> UNIVERISTAS DIPONEGORO </h3>
""", unsafe_allow_html=True)
