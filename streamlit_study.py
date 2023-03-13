import streamlit as st
import time

st.title('プログレスバー')
latest_iteration = st.empty()
latest_iteration = st.text(f'Iteration {1}')
time.sleep(1)
bar = st.progress(0)
for i in range(100):
    latest_iteration.text(f'Iteration {i+1}')
    bar.progress(i + 1)
    time.sleep(0.1)