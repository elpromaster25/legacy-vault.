import streamlit as st
import pandas as pd
import time

# --- 1. SEGURIDAD DE ENTRADA (EL SCANNER) ---
if 'autenticado' not in st.session_state:
    st.session_state.autenticado = False

if not st.session_state.autenticado:
    st.set_page_config(page_title="IDENTIFICACIÓN REQUERIDA", page_icon="🔐")
    st.markdown("<style>.stApp { background-color: #050505; } h1 { color: #d4af37; text-align: center; font-family: 'Courier New'; }</style>", unsafe_allow_html=True)
    st.title("🔐 ACCESO RESTRINGIDO: LEGACY QUANTUM")
    password = st.text_input("INGRESE LLAVE DE ENCRIPTACIÓN:", type="password")
    if st.button("DESBLOQUEAR TERMINAL"):
        if password == "LEGACY2026":
            with st.status("Iniciando Protocolos...", expanded=True) as status:
                st.write("🧬 Escaneando Firma Digital...")
                time.sleep(1)
                st.write("🟢 Identidad Verificada: Dylan García.")
                status.update(label="Acceso Concedido", state="complete", expanded=False)
            st.session_state.autenticado = True
            st.rerun()
        else:
            st.error("ACCESO DENEGADO.")
    st.stop()

# --- 2. CONFIGURACIÓN DE ÉLITE (DISEÑO PENTÁGONO) ---
st.set_page_config(page_title="LEGACY COMMAND CENTER", page_icon="🏛️", layout="wide")
st.markdown("""
    <style>
    .stApp { background-color: #050505; }
    h1, h2, h3 { color: #d4af37 !important; font-family: 'Courier New'; text-align: center; letter-spacing: 2px; }
    [data-testid="stMetricValue"] { color: #d4af37 !important; font-size: 2.5rem !important; font-weight: bold; text-align: center; }
    [data-testid="stMetricLabel"] { color: #ffffff !important; justify-content: center !important; }
    .security-log { background-color: #111; border-left: 3px solid #d4af37; padding: 10px; font-family: 'Courier New'; font-size: 0.8rem; color: #00ff00; }
    .stMarkdown p { color: #888; font-family: 'Courier New'; text-align: center; }
    div.stButton > button { background-color: #1a1a1a; color: #d4af37; border: 1px solid #d4af37; border-radius: 0px; width: 100%; }
    </style>
    """, unsafe_allow_html=True)

# --- 3. BARRA DE NOTICIAS ---
st.markdown("<marquee style='color: #d4af37; font-family: Courier New;'>● MERCADOS GLOBALES OPERANDO ● SEGURIDAD ACTIVA ● BITCOIN BULLISH TREND ●</marquee>", unsafe_allow_html=True)
st.title("🏛️ LEGACY COMMAND CENTER")

# --- 4. MÉTRICAS SUPERIORES ---
t1, t2, t3, t4 = st.columns(4)
t1.metric("ESTADO RED", "PROTEGIDA", "100%")
t2.metric("S&P 500", "5,026", "+0.4%")
t3.metric("BITCOIN", "$98,450", "+2.5%")
t4.metric("EQUITY TOTAL", "$12.45M", "+2.4%")

st.markdown("---")

# --- 5. BÓVEDA Y SEGURIDAD ---
c1, c2 = st.columns(2)
with c1:
    st.subheader("🛡️ REPORTE DE SEGURIDAD")
    st.markdown("<div class='security-log'>> Iniciando escaneo...<br>> Encriptación AES-256: OK<br>> Sincronización Blockchain: OK</div>", unsafe_allow_html=True)
    st.write("")
    st.image("https://img.icons8.com", width=80)
    st.download_button("📄 EXPORTAR CERTIFICADO", "VALOR: $12.45M USD", file_name="Certificado_Legacy.txt")

with c2:
    st.subheader("📊 DISTRIBUCIÓN DE ACTIVOS")
    chart_data = pd.DataFrame({"Activo": ["Propiedades", "Acciones", "Cripto", "Arte"], "Valor": [60, 20, 10, 10]})
    st.bar_chart(chart_data.set_index("Activo"))

# --- 6. SIMULADOR Y IA ---
st.markdown("---")
st.subheader("🚀 ESTRATEGIA IA & PROYECCIÓN")
col_ia1, col_ia2 = st.columns(2)
with col_ia1:
    interes = st.slider("Retorno Anual esperado (%):", 5, 40, 15)
    st.write(f"Proyección a 10 años: **${12450000 * ((1 + (interes/100))**10):,.0f} USD**")
with col_ia2:
    pregunta = st.text_input("Consulta a la IA:")
    if pregunta:
        st.write(f"🕵️ **IA:** Dylan García, para '{pregunta}' la orden es: MANTENER.")

if st.sidebar.button("🔒 CERRAR BÓVEDA"):
    st.session_state.autenticado = False
    st.rerun()

