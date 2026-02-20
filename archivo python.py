import streamlit as st
import pandas as pd
import time

# --- 1. SEGURIDAD BIOMÉTRICA ---
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

# --- 2. CONFIGURACIÓN DE ÉLITE (DISEÑO DORADO) ---
st.set_page_config(page_title="LEGACY VAULT", page_icon="🏛️", layout="wide")
st.markdown("""
    <style>
    .stApp { background-color: #050505; border: 4px solid #d4af37; padding: 20px; }
    h1, h2, h3 { color: #d4af37 !important; font-family: 'serif'; text-align: center; }
    [data-testid="stMetricValue"] { color: #d4af37 !important; font-size: 2.8rem !important; font-weight: bold; text-align: center; }
    [data-testid="stMetricLabel"] { color: #ffffff !important; font-size: 1.1rem !important; text-align: center; }
    div.stButton > button { background-color: #1a1a1a; color: #d4af37; border: 1px solid #d4af37; width: 100%; font-weight: bold; }
    /* Estilo para el aviso de pago en la sidebar */
    .pay-notice { color: #d4af37; font-weight: bold; border: 1px solid #d4af37; padding: 10px; border-radius: 5px; background-color: rgba(212, 175, 55, 0.1); }
    </style>
    """, unsafe_allow_html=True)

# --- 3. BARRA LATERAL (PAGO Y MEMBRESÍA) ---
with st.sidebar:
    st.image("https://img.icons8.com", width=80)
    st.write("### 💎 MEMBRESÍA PREMIUM")
    
    # Cartel en Español
    st.markdown("""<div class='pay-notice'>
    🇦🇷 Para poder usar la app/pagina mas de 1 mes tenes que pagar 2 millones.
    </div>""", unsafe_allow_html=True)
    
    st.write("") # Espacio
    
    # Cartel en Inglés (Precio Internacional)
    st.markdown("""<div class='pay-notice'>
    🇺🇸 To use this app/page for more than 1 month you have to pay 12 thousand dollars.
    </div>""", unsafe_allow_html=True)
    
    st.write("---")
    if st.button("🔒 CERRAR SESIÓN"):
        st.session_state.autenticado = False
        st.rerun()

# --- 4. PANEL PRINCIPAL ---
st.title("🏛️ CENTRO DE MANDO LEGACY")
st.markdown("<marquee style='color: #d4af37;'>● MERCADOS GLOBALES OPERANDO ● SEGURIDAD ACTIVA ● BITCOIN BULLISH ●</marquee>", unsafe_allow_html=True)

# 5. SIMULADOR DINÁMICO
st.subheader("🚀 PROYECCIÓN DE FORTUNA DINÁMICA")
col_s1, col_s2 = st.columns(2)
with col_s1:
    años = st.slider("AÑOS DE INVERSIÓN:", 1, 30, 10)
with col_s2:
    ret = st.slider("RENDIMIENTO ANUAL (%)", 5, 50, 15)

tc = 1500 
futuro_usd = 12450000 * ((1 + (ret/100))**años)
futuro_ars = futuro_usd * tc

st.markdown("---")
res1, res2 = st.columns(2)
res1.metric("FORTUNA EN USD", f"${futuro_usd:,.0f}")
res2.metric("FORTUNA EN ARS", f"${futuro_ars:,.0f}")

st.markdown("---")

# 6. BITCOIN Y GRÁFICOS
c1, c2 = st.columns(2)
with c1:
    st.subheader("📊 DISTRIBUCIÓN")
    df_data = pd.DataFrame({"Activo": ["Casas", "Bolsa", "Cripto", "Arte"], "Valor": [60, 20, 10, 10]})
    st.bar_chart(df_data.set_index("Activo"))
with c2:
    st.subheader("🤖 ESTRATEGA IA")
    pregunta = st.text_input("CONSULTA TÉCNICA:")
    if pregunta:
        st.write(f"🏛️ **IA:** Dylan García, para '{pregunta}' la orden es MANTENER.")
    st.download_button("📥 DESCARGAR AUDITORÍA", f"VALOR: {futuro_usd} USD", file_name="Legacy_Audit.txt")
