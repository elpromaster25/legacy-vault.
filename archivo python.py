import streamlit as st
import pandas as pd
import time

# --- 1. SEGURIDAD DE ACCESO (EL SCANNER) ---
if 'autenticado' not in st.session_state:
    st.session_state.autenticado = False

if not st.session_state.autenticado:
    st.set_page_config(page_title="IDENTIFICACIÓN REQUERIDA", page_icon="🔐")
    st.markdown("<style>.stApp { background-color: #050505; } h1 { color: #d4af37; text-align: center; font-family: 'Garamond'; }</style>", unsafe_allow_html=True)
    st.title("Acceso Restringido: Legacy Quantum")
    password = st.text_input("Ingrese Llave de Encriptación:", type="password")
    if st.button("Desbloquear Terminal"):
        if password == "LEGACY2026":
            with st.status("Iniciando Protocolos...", expanded=True) as status:
                st.write("🧬 Escaneando Firma Digital...")
                time.sleep(1)
                st.write("🟢 Identidad Verificada: Dylan García.")
                status.update(label="Acceso Concedido", state="complete", expanded=False)
            st.session_state.autenticado = True
            st.rerun()
        else:
            st.error("Acceso Denegado.")
    st.stop()

# --- 2. CONFIGURACIÓN DE ÉLITE ---
st.set_page_config(page_title="LEGACY COMMAND CENTER", page_icon="🏛️", layout="wide")
st.markdown("""
    <style>
    .stApp { background-color: #050505; }
    h1, h2, h3 { color: #d4af37 !important; font-family: 'Garamond', serif; text-align: center; }
    [data-testid="stMetricValue"] { color: #d4af37 !important; font-size: 2.8rem !important; }
    .stMarkdown p { color: #888; font-family: 'Courier New'; }
    div.stButton > button { background-color: #1a1a1a; color: #d4af37; border: 1px solid #d4af37; border-radius: 0px; width: 100%; }
    </style>
    """, unsafe_allow_html=True)

# --- 3. BARRA DE NOTICIAS ---
st.markdown("<marquee style='color: #d4af37; font-family: Courier New;'>● MERCADOS GLOBALES OPERANDO ● PROTECCIÓN PATRIMONIAL ACTIVA ●</marquee>", unsafe_allow_html=True)

st.title("🏛️ LEGACY COMMAND CENTER")

# --- 4. MÉTRICAS ---
t1, t2, t3, t4 = st.columns(4)
t1.metric("ESCUDO DE RED", "ACTIVO", "AES-256")
t2.metric("RIESGO", "BAJO", "SÓLIDO")
t3.metric("EQUITY TOTAL", "$12.45M", "+2.4%")
t4.metric("BITCOIN", "$98,450", "+2.5%")

st.markdown("---")

# --- 5. BÓVEDA ---
c1, c2 = st.columns(2)
with c1:
    st.subheader("💰 Resumen de Activos")
    st.download_button("📄 Exportar Informe", "PATRIMONIO: $12.45M", file_name="Legacy_Audit.txt")
    # Gráfico corregido
    df_data = pd.DataFrame({"Activo": ["Propiedades", "Acciones", "Cripto"], "Valor": [60, 25, 15]})
    st.bar_chart(df_data.set_index("Activo"))

with c2:
    st.subheader("🤖 Analista IA")
    pregunta = st.text_input("Consulta para la IA:")
    if pregunta:
        with st.spinner('Analizando...'):
            time.sleep(1)
            st.write(f"🏛️ **IA:** Dylan García, la recomendación es mantener.")

# --- 6. SIDEBAR ---
with st.sidebar:
    if st.button("🔒 Cerrar Sesión"):
        st.session_state.autenticado = False
        st.rerun()
