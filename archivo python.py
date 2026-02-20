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
    st.stop()

# --- 2. CONFIGURACIÓN DE LUJO ---
st.set_page_config(page_title="LEGACY VAULT", page_icon="🏛️", layout="wide")
st.markdown("""
    <style>
    .stApp { background-color: #050505; border: 4px solid #d4af37; padding: 20px; }
    h1, h2, h3 { color: #d4af37 !important; font-family: 'serif'; text-align: center; }
    [data-testid="stMetricValue"] { color: #d4af37 !important; font-size: 3rem !important; font-weight: bold; }
    .pay-notice { color: #d4af37; font-weight: bold; border: 2px solid #d4af37; padding: 15px; border-radius: 10px; background-color: rgba(212, 175, 55, 0.1); text-align: center; margin-bottom: 20px; }
    </style>
    """, unsafe_allow_html=True)

# --- 3. EL CARTEL DE PAGO (LADO IZQUIERDO / SIDEBAR) ---
with st.sidebar:
    st.markdown("### 💎 MEMBRESÍA")
    st.markdown("<div class='pay-notice'>🇦🇷 Para usar la app más de 1 mes tenés que pagar 2 millones.</div>", unsafe_allow_html=True)
    st.markdown("<div class='pay-notice'>🇺🇸 To use this app for more than 1 month you have to pay 12 thousand dollars.</div>", unsafe_allow_html=True)
    st.write("---")
    if st.button("🔒 CERRAR"):
        st.session_state.autenticado = False
        st.rerun()

# --- 4. PANEL DE CONTROL ---
st.title("🏛️ CENTRO DE MANDO LEGACY")

# SIMULADOR
col_s1, col_s2 = st.columns(2)
with col_s1:
    años = st.slider("AÑOS DE INVERSIÓN:", 1, 30, 10)
with col_s2:
    ret = st.slider("RETORNO ANUAL (%)", 5, 50, 15)

# CÁLCULOS DINÁMICOS
tc = 1500 
capital_inicial = 12450000
futuro_usd = capital_inicial * ((1 + (ret/100))**años)
futuro_ars = futuro_usd * tc

# FUNCIÓN PARA ACORTAR NÚMEROS (Para que no se vean 16 dígitos)
def formato_moneda(numero):
    if numero >= 1_000_000_000_000: return f"{numero/1_000_000_000_000:.2f} Billones"
    if numero >= 1_000_000_000: return f"{numero/1_000_000_000:.2f} Mil Millones"
    if numero >= 1_000_000: return f"{numero/1_000_000:.2f} Millones"
    return f"{numero:,.0f}"

st.markdown("---")
res1, res2 = st.columns(2)
res1.metric("PROYECCIÓN USD", formato_moneda(futuro_usd))
res2.metric("PROYECCIÓN ARS", formato_moneda(futuro_ars))

st.markdown("---")
# GRÁFICO (CON NÚMEROS FIJOS PARA EVITAR ERROR ROJO)
df_data = pd.DataFrame({"Activo": ["Propiedades", "Acciones", "Cripto", "Arte"], "Valor": [60, 20, 10, 10]})
st.bar_chart(df_data.set_index("Activo"))

st.subheader("🤖 IA ESTRATÉGICA")
pregunta = st.text_input("CONSULTA:")
if pregunta:
    st.write(f"🏛️ **IA:** Dylan García, para '{pregunta}' la orden es MANTENER.")
