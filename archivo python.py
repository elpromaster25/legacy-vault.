import streamlit as st
import pandas as pd
import time

# --- 1. SEGURIDAD Y PANTALLA DE ENTRADA (DISEÑO SIMÉTRICO) ---
if 'autenticado' not in st.session_state:
    st.session_state.autenticado = False
if 'mensajes' not in st.session_state:
    st.session_state.mensajes = []

if not st.session_state.autenticado:
    st.set_page_config(page_title="LEGACY | LOGIN", page_icon="🔐")
    st.markdown("<style>.stApp { background-color: #000000; } h1, h3 { color: #d4af37; text-align: center; font-family: 'serif'; }</style>", unsafe_allow_html=True)
    st.title("🔐 TERMINAL DE ACCESO PRIVADO")
    
    # Login Principal
    password = st.text_input("LLAVE MAESTRA / MASTER KEY:", type="password")
    if st.button("DESBLOQUEAR BÓVEDA"):
        if password == "LEGACY2026":
            st.session_state.autenticado = True
            st.rerun()
    
    st.write("---")
    st.subheader("📩 ¿No tiene una llave de acceso? / No access key?")
    
    # LAS 3 COLUMNAS: INFO IZQ | FORMULARIO | INFO DER
    col_info_izq, col_form, col_info_der = st.columns([1, 2, 1])
    
    with col_info_izq:
        st.markdown("<p style='color: #d4af37; font-size: 0.9rem; text-align: center;'>🛡️ PROTECCIÓN<br>Encriptación AES-256 para activos de alto valor en Puerto Madero y el mundo.</p>", unsafe_allow_html=True)

    with col_form:
        with st.form("contacto_vip"):
            perfil = st.radio("Perfil:", ["Empresario / CEO", "Inversor Independiente"])
            mail = st.text_input("Su Email:")
            if st.form_submit_button("SOLICITAR ACCESO VIP"):
                if mail:
                    st.session_state.mensajes.append({"perfil": perfil, "mail": mail, "hora": time.strftime('%H:%M')})
                    st.success("✅ SOLICITUD ENVIADA AL FOUNDER.")
                else:
                    st.warning("Ingrese su email.")

    with col_info_der:
        st.markdown("<p style='color: #d4af37; font-size: 0.9rem; text-align: center;'>📈 PROYECCIÓN<br>Algoritmos de IA para el análisis de riesgo y crecimiento patrimonial.</p>", unsafe_allow_html=True)
    
    st.stop()

# --- 2. CONFIGURACIÓN POST-LOGIN (DENTRO DE LA BÓVEDA) ---
st.set_page_config(page_title="LEGACY VAULT", page_icon="🏛️", layout="wide")
st.markdown("""
    <style>
    .stApp { background-color: #050505; border: 4px solid #d4af37; padding: 20px; }
    h1, h2, h3 { color: #d4af37 !important; font-family: 'serif'; text-align: center; }
    [data-testid="stMetricValue"] { color: #d4af37 !important; font-size: 2.2rem !important; font-weight: bold; }
    .pay-banner { background-color: rgba(212, 175, 55, 0.1); border: 2px solid #d4af37; color: #d4af37; padding: 10px; text-align: center; font-weight: bold; border-radius: 10px; margin-bottom: 10px; }
    </style>
    """, unsafe_allow_html=True)

# --- SIDEBAR (ADMIN & TRADUCCIÓN) ---
st.sidebar.title("🛂 DASHBOARD")
es_admin = st.sidebar.checkbox("🔓 MODO ADMIN (DYLAN)")
idioma = st.sidebar.selectbox("Region:", ["🇦🇷 Argentina", "🇺🇸 USA / International"]) if not es_admin else "Admin"

# Traducciones y Lógica de Negocio
if idioma == "Admin":
    st.title("👨‍💻 PANEL DE CONTROL: DYLAN GARCÍA")
    st.subheader("📬 SOLICITUDES DE ACCESO VIP")
    if st.session_state.mensajes:
        st.table(pd.DataFrame(st.session_state.mensajes))
    else:
        st.write("Esperando interesados de Puerto Madero...")
else:
    banner = "🇦🇷 Si sos de Argentina tenes que pagar 2 millones por mes." if "Argentina" in idioma else "🇺🇸 If you are from the USA etc, it costs 12 thousand per month."
    st.markdown(f"<div class='pay-banner'>{banner}</div>", unsafe_allow_html=True)
    st.title("🏛️ COMMAND CENTER LEGACY")
    
    # SIMULADOR
    años = st.slider("AÑOS / YEARS:", 1, 30, 10)
    ret = st.slider("RETORNO / RETURN %:", 5, 50, 15)
    fut_usd = 12450000 * ((1 + (ret/100))**años)
    fut_ars = fut_usd * 1500 # TC 2026
    
    st.markdown("---")
    r1, r2 = st.columns(2)
    r1.metric("FORTUNA USD", f"${fut_usd:,.0f}")
    r2.metric("FORTUNA ARS", f"${fut_ars:,.0f}")
    
    st.markdown("---")
    c1, c2 = st.columns(2)
    with c1:
        st.subheader("📊 DISTRIBUCIÓN")
        df = pd.DataFrame({"Activo": ["RE", "Stocks", "Crypto", "Art"], "Valor":})
        st.bar_chart(df.set_index("Activo"))
    with c2:
        st.subheader("🤖 IA ADVISOR")
        st.write("IA ESTRATÉGICA ACTIVA")

if st.sidebar.button("🔒 CERRAR"):
    st.session_state.autenticado = False
    st.rerun()
