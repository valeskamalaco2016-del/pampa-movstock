import streamlit as st
import pandas as pd

st.set_page_config(
    page_title="PAMPA MOVSTOCK",
    layout="wide"
)

st.title("PAMPA MOVSTOCK")
st.subheader("Inteligência Comercial Agro")

arquivo = st.file_uploader(
    "Envie a planilha",
    type=["xlsx"]
)

if arquivo:

    xls = pd.ExcelFile(arquivo)

    aplicacoes = pd.read_excel(xls, sheet_name=0)
    clientes = pd.read_excel(xls, sheet_name=1)

    busca = st.text_input(
        "Buscar código, modelo ou grupo"
    )

    resultado = aplicacoes.copy()

    if busca:
        resultado = resultado[
            resultado.astype(str)
            .apply(
                lambda x: x.str.contains(
                    busca,
                    case=False,
                    na=False
                )
            )
            .any(axis=1)
        ]

    st.dataframe(resultado)

    st.subheader("Clientes")
    st.dataframe(clientes)
