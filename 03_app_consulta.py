import streamlit as st
import os

st.title("Teste 2")

try:
    import importlib.util
    base_dir = os.path.dirname(os.path.abspath(__file__))
    caminho = os.path.join(base_dir, "01_baixar_dados.py")
    spec = importlib.util.spec_from_file_location("baixar", caminho)
    modulo = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(modulo)
    st.success("01_baixar_dados.py importado com sucesso!")
except Exception as e:
    st.error(f"Erro ao importar 01: {e}")

try:
    caminho2 = os.path.join(base_dir, "02_processar_dados.py")
    spec2 = importlib.util.spec_from_file_location("processar", caminho2)
    modulo2 = importlib.util.module_from_spec(spec2)
    spec2.loader.exec_module(modulo2)
    st.success("02_processar_dados.py importado com sucesso!")
except Exception as e:
    st.error(f"Erro ao importar 02: {e}")
