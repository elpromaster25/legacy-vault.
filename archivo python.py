import streamlit as st
import pandas as pd
import time

# --- 1. ACCESO BIOMÉTRICO (James Bond Style) ---
if 'autenticado' not in st.session_state:
    st.session_state.autenticado = False

if not st.session_state.autenticado:
    st.set_page_config(page_title="LEGACY | SECURITY", page_icon="🔐")
    st.markdown("<style>.stApp { background-color: #000000; } h1 { color: #d4af37; text-align: center; font-family: 'Courier New'; }</style>", unsafe_allow_html=True)
    st.title("🔐 ENCRYPTED TERMINAL")
    password = st.text_input("MASTER KEY:", type="password")
    if st.button("AUTHORIZE"):
        if password == "LEGACY2026":
            with st.status("Initializing Quantum Tunnel...", expanded=True) as status:
                st.write("🔎 Verifying RSA-4096 signature...")
                time.sleep(1)
                st.write("🛰️ Satellite uplink established.")
                status.update(label="Access Granted", state="complete", expanded=False)
            st.session_state.autenticado = True
            st.rerun()
        else:
            st.error("ACCESS DENIED.")
    st.stop()

# --- 2. CONFIGURACIÓN DE COMANDO ---
st.set_page_config(page_title="LEGACY COMMAND", page_icon="🏛️", layout="wide")
st.markdown("""
    <style>
    .stApp { background-color: #050505; border: 2px solid #d4af37; padding: 10px; }
    h1, h2, h3 { color: #d4af37 !important; font-family: 'Courier New', monospace; text-align: center; }
    [data-testid="stMetricValue"] { color: #d4af37 !important; font-size: 3rem !important; font-weight: bold; text-align: center; }
    [data-testid="stMetricLabel"] { color: #ffffff !important; justify-content: center !important; }
    .stMarkdown p { color: #888; font-family: 'Courier New'; text-align: center; }
    div.stButton > button { background-color: #1a1a1a; color: #d4af37; border: 1px solid #d4af37; border-radius: 0px; width: 100%; }
    </style>
    """, unsafe_allow_html=True)

# --- 3. BARRA DE NOTICIAS ---
st.markdown("<marquee style='color: #d4af37; font-family: Courier New;'>● MERCADOS GLOBALES OPERANDO ● SEGURIDAD ACTIVA ● BITCOIN BULLISH TREND ●</marquee>", unsafe_allow_html=True)
st.title("🏛️ LEGACY COMMAND CENTER v2.0")

# 4. MONITOR DE ACTIVOS
m1, m2, m3, m4 = st.columns(4)
m1.metric("STATUS", "SECURE", "100%")
m2.metric("S&P 500", "5,026", "+0.4%")
m3.metric("BITCOIN", "$98,450", "+2.5%")
m4.metric("EQUITY TOTAL", "$12.45M", "+2.4%")

st.markdown("---")

# 5. CONSOLA TÉCNICA Y GRÁFICOS
col_c1, col_c2 = st.columns(2)
with col_c1:
    st.subheader("🛡️ SECURITY LOGS")
    st.code("> TRACE: ACTIVE\n> ENCRYPTION: AES-256\n> AUDIT: VERIFIED", language="bash")
    st.image("https://img.icons8.com", width=80)
    st.download_button("📥 DOWNLOAD AUDIT", "CERTIFIED: $12.45M USD", file_name="Audit_Legacy.txt")

with col_c2:
    st.subheader("📊 ASSET DISTRIBUTION")
    # GRÁFICO CORREGIDO
    df = pd.DataFrame({"Activo": ["Propiedades", "Stocks", "Crypto", "Arte"], "Valor": [60, 20, 10, 10]})
    st.bar_chart(df.set_index("Activo"))

# 6. IA ESTRATEGA
st.markdown("---")
st.subheader("🤖 STRATEGIC IA ADVISOR")
pregunta = st.text_input("COMMAND INPUT:")
if pregunta:
    with st.spinner('Analyzing...'):
        time.sleep(1)
        st.write(f"🕵️ **ANALISTA:** CEO Dylan Garcia, analysis for '{pregunta}': MANTENER POSICIÓN.")

if st.sidebar.button("🔒 LOGOUT"):
    st.session_state.autenticado = False
    st.rerun()
