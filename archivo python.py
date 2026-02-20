import streamlit as st
import pandas as pd
import time

# --- 1. SEGURIDAD Y PANTALLA DE ENTRADA (TU IDEA) ---
if 'autenticado' not in st.session_state:
    st.session_state.autenticado = False

if not st.session_state.autenticado:
    st.set_page_config(page_title="LEGACY | LOGIN", page_icon="🔐")
    st.markdown("<style>.stApp { background-color: #000000; } h1, h3 { color: #d4af37; text-align: center; font-family: 'serif'; }</style>", unsafe_allow_html=True)
    st.title("🔐 ACCESO PRIVADO: LEGACY VAULT")
    
    password = st.text_input("LLAVE MAESTRA / MASTER KEY:", type="password")
    if st.button("DESBLOQUEAR BÓVEDA / UNLOCK"):
        if password == "LEGACY2026":
            st.session_state.autenticado = True
            st.rerun()
        else:
            st.error("LLAVE INVÁLIDA / INVALID KEY.")
    
    st.write("---")
    st.subheader("¿No tiene una llave? / No key?")
    perfil = st.radio("Perfil Profesional:", ["💼 Soy Empresario / CEO", "🦈 Soy Inversor Independiente (High-Net-Worth)"])
    email_solicitud = st.text_input("Email para contacto / Email for contact:")
    
    if st.button("ENVIAR SOLICITUD / SEND REQUEST"):
        if email_solicitud:
            with st.spinner("Procesando solicitud..."):
                time.sleep(1.5)
                st.success(f"NOTIFICACIÓN ENVIADA: El departamento de Legacy Vault revisará su perfil.")
        else:
            st.warning("Ingrese un email válido.")
    st.stop()

# --- 2. CONFIGURACIÓN POST-LOGIN ---
st.set_page_config(page_title="LEGACY VAULT", page_icon="🏛️", layout="wide")
st.markdown("""
    <style>
    .stApp { background-color: #050505; border: 4px solid #d4af37; padding: 20px; }
    h1, h2, h3 { color: #d4af37 !important; font-family: 'serif'; text-align: center; }
    [data-testid="stMetricValue"] { color: #d4af37 !important; font-size: 2.2rem !important; font-weight: bold; }
    .pay-banner { background-color: rgba(212, 175, 55, 0.1); border: 2px solid #d4af37; color: #d4af37; padding: 15px; text-align: center; font-weight: bold; border-radius: 10px; margin-bottom: 10px; }
    </style>
    """, unsafe_allow_html=True)

# --- 3. PANEL DE CONTROL (IDIOMA) ---
st.sidebar.title("🛂 DASHBOARD")
es_admin = st.sidebar.checkbox("🔓 MODO ADMIN (DYLAN)")
idioma = st.sidebar.selectbox("Region:", ["🇦🇷 Argentina", "🇺🇸 USA / International"]) if not es_admin else "Admin"

# Traducciones
texts = {
    "🇦🇷 Argentina": {"banner": "🇦🇷 Pago: 2 millones/mes.", "titulo": "🏛️ CENTRO DE MANDO", "res1": "PESOS (ARS)", "res2": "DÓLARES (USD)"},
    "🇺🇸 USA / International": {"banner": "🇺🇸 Cost: 12 thousand/month.", "titulo": "🏛️ COMMAND CENTER", "res1": "DOLLARS (USD)", "res2": "PESOS (ARS)"},
    "Admin": {"banner": "💎 ADMIN: 2M ARS / 12K USD", "titulo": "🏛️ MASTER TERMINAL", "res1": "USD TOTAL", "res2": "ARS TOTAL"}
}
t = texts[idioma]

# --- 4. INTERFAZ ---
st.markdown(f"<div class='pay-banner'>{t['banner']}</div>", unsafe_allow_html=True)
st.title(t["titulo"])

# SIMULADOR
años = st.slider("AÑOS / YEARS:", 1, 30, 10)
ret = st.slider("RETORNO / RETURN %:", 5, 50, 15)

tc = 1500 # Dólar 2026
fut_usd = 12450000 * ((1 + (ret/100))**años)
fut_ars = fut_usd * tc 

st.markdown("---")
r1, r2 = st.columns(2)
if "PESOS" in t["res1"] or "ARS" in t["res1"]:
    r1.metric(t["res1"], f"${fut_ars:,.0f}")
    r2.metric(t["res2"], f"${fut_usd:,.0f}")
else:
    r1.metric(t["res1"], f"${fut_usd:,.0f}")
    r2.metric(t["res2"], f"${fut_ars:,.0f}")

st.markdown("---")
# GRÁFICOS Y IA
c1, c2 = st.columns(2)
with c1:
    st.subheader("📊 DISTRIBUCIÓN")
    df = pd.DataFrame({"Activo": ["RE", "Stocks", "Crypto", "Art"], "Valor": [40, 30, 20, 10]})
    st.bar_chart(df.set_index("Activo"))
with c2:
    st.subheader("🤖 IA ADVISOR")
    preg = st.text_input("Consulta / Query:")
    if preg: st.write("🏛️ **IA:** Dylan García, la orden es MANTENER / HOLD.")

if st.sidebar.button("🔒 LOGOUT"):
    st.session_state.autenticado = False
    st.rerun()
