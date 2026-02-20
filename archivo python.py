import streamlit as st
import pandas as pd
import time

# --- 1. SEGURIDAD ---
if 'autenticado' not in st.session_state:
    st.session_state.autenticado = False

if not st.session_state.autenticado:
    st.set_page_config(page_title="ACCESO PRIVADO", page_icon="🔐")
    st.markdown("<style>.stApp { background-color: #000000; } h1 { color: #d4af37; text-align: center; }</style>", unsafe_allow_html=True)
    st.title("🔐 TERMINAL DE ACCESO PRIVADO")
    password = st.text_input("LLAVE MAESTRA:", type="password")
    if st.button("DESBLOQUEAR BÓVEDA"):
        if password == "LEGACY2026":
            st.session_state.autenticado = True
            st.rerun()
        else:
            st.error("CLAVE INCORRECTA")
    st.stop()

# --- 2. CONFIGURACIÓN DE LUJO ---
st.set_page_config(page_title="LEGACY VAULT", page_icon="🏛️", layout="wide")
st.markdown("""
    <style>
    .stApp { background-color: #050505; border: 4px solid #d4af37; padding: 20px; }
    h1, h2, h3 { color: #d4af37 !important; font-family: 'serif'; text-align: center; }
    [data-testid="stMetricValue"] { color: #d4af37 !important; font-size: 2.5rem !important; font-weight: bold; }
    [data-testid="stMetricLabel"] { color: #ffffff !important; }
    div.stButton > button { background-color: #1a1a1a; color: #d4af37; border: 1px solid #d4af37; }
    </style>
    """, unsafe_allow_html=True)

st.title("🏛️ CENTRO DE MANDO LEGACY")
st.markdown("<p style='text-align: center; color: #00ff00;'>● MONITOREO MULTIDIVISA ACTIVO ● 20 FEB 2026 ●</p>", unsafe_allow_html=True)

# --- 3. SENSOR DE DÓLARES (USD) ---
st.subheader("🇺🇸 ACTIVOS EN DÓLARES (USD)")
u1, u2, u3 = st.columns(3)
u1.metric("VALOR NETO USD", "$12,450,000", "+2.4%")
u2.metric("BITCOIN USD", "$98,450", "+2.5%")
u3.metric("RENTABILIDAD USD", "$298.8K", "ESTABLE")

# --- 4. SENSOR DE PESOS (ARS) ---
# Usamos un tipo de cambio estimado para Feb 2026 (Ej: 1500 ARS/USD)
tc = 1500 
st.subheader("🇦🇷 ACTIVOS EN PESOS (ARS)")
a1, a2, a3 = st.columns(3)
a1.metric("VALOR NETO ARS", f"${12450000 * tc:,.0f}", "OFICIAL/MEP")
a2.metric("BITCOIN ARS", f"${98450 * tc:,.0f}", "BLOCKCHAIN")
a3.metric("LIQUIDEZ ARS", f"${300000 * tc:,.0f}", "DISPONIBLE")

st.markdown("---")

# --- 5. BITCOIN Y SIMULADOR ---
col_b1, col_b2, col_b3 = st.columns()
with col_b2:
    st.image("https://img.icons8.com", width=100)
    st.subheader("🚀 PROYECCIÓN DE FORTUNA")
    años = st.slider("AÑOS:", 1, 30, 10)
    ret = st.slider("RETORNO (%):", 5, 50, 15)
    futuro = 12450000 * ((1 + (ret/100))**años)
    st.metric("VALOR FUTURO (USD)", f"${futuro:,.0f}")

# --- 6. GRÁFICO Y IA ---
c1, c2 = st.columns(2)
with c1:
    st.subheader("📊 DISTRIBUCIÓN")
    df = pd.DataFrame({"Activo": ["Casas", "Bolsa", "Cripto", "Arte"], "Valor":})
    st.bar_chart(df.set_index("Activo"))
with c2:
    st.subheader("🤖 ESTRATEGA IA")
    pregunta = st.text_input("CONSULTA:")
    if pregunta:
        st.write(f"🏛️ **IA:** Dylan García, para '{pregunta}' la orden es: MANTENER.")

if st.sidebar.button("🔒 CERRAR"):
    st.session_state.autenticado = False
    st.rerun()
