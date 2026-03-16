import streamlit as st
import os
import sys
import traceback

st.set_page_config(page_title="Teste", layout="wide")
st.title("Teste de inicializacao")

def _get_base_dir() -> str:
    for caminho in [
        "/mount/src/carteiras_cvm",
        os.getcwd(),
    ]:
        if os.path.exists(os.path.join(caminho, "01_baixar_dados.py")):
            return caminho
    return os.getcwd()

st.write(f"Base dir: {_get_base_dir()}")
st.write(f"Arquivos: {os.listdir(_get_base_dir())}")

try:
    import importlib.util
    base_dir = _get_base_dir()
    caminho = os.path.join(base_dir, "01_baixar_dados.py")
    spec = importlib.util.spec_from_file_location("baixar", caminho)
    modulo = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(modulo)
    st.success("01 importado!")
except Exception as e:
    st.error(f"Erro: {e}")
    st.code(traceback.format_exc())

st.write("Parquet existe?", os.path.exists(os.path.join(_get_base_dir(), "dados_processados", "carteiras_consolidadas.parquet")))
