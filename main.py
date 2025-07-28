import streamlit as st
from generatePDF import gerarHTML

if "file" not in st.session_state:
    st.session_state["files"] = list()
listFiles = st.session_state["files"]


# with st.expander("Arquivos", expanded=False):
#     st.write("Nenhum arquivo encontrado")

with st.expander("Dados de input", expanded=True):

    if True: # dados input

        st.divider()

        nomeCliente = st.text_input("Nome do cliente", value="Ciclano da silva")

        if nomeCliente.strip() == "":
            st.error("Nome não pode estar vazio")
            st.stop()

        st.divider()

        idadeCronologica = st.text_input("Idade cronológica")
        idadeCelular = st.text_input("Idade celular")

        st.divider()

        resultadoAnguloFase = st.text_input("Resultado do ângulo de fase")

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

        inputMedicoTaxaMetabolicaBasal = st.text_area("Campo taxa metabólica basal")


    if st.button("Gerar arquivo"):
        
        dictSubs = {
            "[NOMECLIENTE]": nomeCliente,
            "[IDADE_CRONOLOGICA]": idadeCronologica,
            "[IDADE_CELULAR]": idadeCelular,
            "[RESULTADO_ANGULO_FASE]": resultadoAnguloFase,
            "[INDICE_HIDRATACAO]": indiceHidratacao,
            "[AGUA_TOTAL]": aguaCorporalTotal,
            "[AGUA_MASSA_MAGRA]": aguaMassaMagra,
            "[AGUA_INTRA]": aguaIntracelular,
            "[AGUA_EXTRA]": aguaExtracelular,
            "[RESULTADO_IMC]": imc,
            "[RESULTADO_GORDURA]": gordura,
            "[PERCENTUAL_GORDURA]": percGordura,
            "[MASSA_MAGRA_MUSCULAR]": massaMagraEMuscular,
            "[RAZAO_MUSC_GORD]": razaoMusculoGordura,
            "[RAZAO_CINTURA_ESTATURA]": razaoCinturaEstatura,
            "[CINTURA_PERIMETRO_ABDOMINAL]": cinturaPerimetroAbdominal,
            "[INPUT_MEDICO_TAXA_METABOLICA_BASAL]": inputMedicoTaxaMetabolicaBasal
        }
        for key in dictSubs:
            dictSubs[key] = str(dictSubs[key])

        # st.write(dictSubs)

        outputName = f"{nomeCliente}.pdf"

        st.write(outputName)

        gerarHTML(output=outputName, substitutions=dictSubs)
        with open(outputName, "rb") as file:
            st.download_button("Baixar arquivo gerado", data=file, file_name=outputName)

 

