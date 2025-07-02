import streamlit as st

if "file" not in st.session_state:
    st.session_state["files"] = list()
listFiles = st.session_state["files"]


with st.expander("Arquivos", expanded=False):
    st.write("Nenhum arquivo encontrado")

with st.expander("Dados de input", expanded=True):

    st.divider()

    nomeCliente = st.text_input("Nome do cliente")

    st.divider()

    idadeCronologica = st.text_input("Idade cronológica")
    idadeCelular = st.text_input("Idade celular")

    st.divider()

    anguloFaseResultado = st.text_input("Resultado do ângulo de fase")

    st.divider()

    indiceHidratacao = st.text_input("Índice de hidratação")
    aguaCorporalTotal = st.number_input("Água corporal total, em litros")
    aguaMassaMagra = st.number_input("Água na massa magra")
    aguaIntracelular = st.number_input("Água intracelular")
    aguaExtracelular = st.number_input("Água extracelular")

    st.divider()

    imc = st.number_input("IMC")
    gordura = st.number_input("Gordura (massa gorda)")
    percGordura = st.number_input("Percentual de gordura")
    massaMagraEMuscular = st.number_input("Massa magra e muscular")
    razaoMusculoGordura = st.number_input("Razão músculo-gordura")

    st.divider()

    razaoCinturaEstatura = st.number_input("Razão cintura-estatura")
    cinturaPerimetroAbdominal = st.number_input("Cintura/perímetro abdominal")

    st.divider()

    st.text_area("Campo taxa metabólica basal")


