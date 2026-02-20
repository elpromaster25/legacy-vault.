import streamlit as st
import pandas as pd
import time

# --- 1. SEGURIDAD Y LOGIN GIGANTE ---
if 'autenticado' not in st.session_state:
    st.session_state.autenticado = False
if 'mensajes' not in st.session_state:
    st.session_state.mensajes = []

if not st.session_state.autenticado:
    st.set_page_config(page_title="LEGACY | LOGIN", page_icon="🔐", layout="wide")
    st.markdown("""
        <style>
        .stApp { background-color: #000000; }
        h1 { color: #d4af37 !important; text-align: center; font-family: 'serif'; font-size: 4.5rem !important; margin-top: 50px; }
        h3 { color: #d4af37 !important; text-align: center; font-size: 2rem !important; }
        .info-box {
            color: #d4af37; font-size: 1.4rem; text-align: center; border: 2px solid #d4af37;
            padding: 30px; border-radius: 15px; background-color: rgba(212, 175, 55, 0.05);
            min-height: 350px; display: flex; align-items: center; justify-content: center; flex-direction: column;
        }
        div.stButton > button {
            height: 3.5em; font-size: 1.2rem !important; font-weight: bold;
            background-color: #1a1a1a; color: #d4af37; border: 2px solid #d4af37; width: 100%;
        }
        </style>
        """, unsafe_allow_html=True)
    
    st.title("🏛️ LEGACY QUANTUM VAULT")
    
    col_l, col_c, col_r = st.columns([1, 1.5, 1])
    with col_c:
        password = st.text_input("LLAVE MAESTRA / MASTER KEY:", type="password")
        if st.button("DESBLOQUEAR TERMINAL"):
            if password == "LEGACY2026":
                st.session_state.autenticado = True
                st.rerun()
            else:
                st.error("LLAVE INCORRECTA")
    
    st.write("---")
    st.subheader("📩 SOLICITUD DE ACCESO VIP / ACCESS REQUEST")
    
    c_izq, c_mid, c_der = st.columns([1.5, 2, 1.5])
    with c_izq:
        st.markdown("<div class='info-box'>🛡️ PROTECCIÓN TOTAL<br><br>Cifrado de grado militar AES-256. Sus activos bajo custodia digital absoluta.</div>", unsafe_allow_html=True)
    with c_mid:
        with st.form("contacto_vip"):
            perfil = st.radio("Perfil:", ["💼 Empresario", "🦈 Inversor Independiente"])
            mail = st.text_input("Email de Contacto:")
            if st.form_submit_button("ENVIAR SOLICITUD"):
                if mail:
                    st.session_state.mensajes.append({"perfil": perfil, "mail": mail, "hora": time.strftime('%H:%M')})
                    st.success("✅ SOLICITUD ENVIADA.")
                else:
                    st.warning("Ingrese su email.")
    with c_der:
        st.markdown("<div class='info-box'>📈 CRECIMIENTO<br><br>IA de predicción macroeconómica. Optimización de rentabilidad en tiempo real.</div>", unsafe_allow_html=True)
    st.stop()

# --- 2. INTERIOR DE LA BÓVEDA ---
st.set_page_config(page_title="LEGACY COMMAND", page_icon="🏛️", layout="wide")
st.markdown("""
    <style>
    .stApp { background-color: #050505; border: 4px solid #d4af37; padding: 20px; }
    h1, h2, h3 { color: #d4af37 !important; font-family: 'serif'; text-align: center; }
    [data-testid="stMetricValue"] { color: #d4af37 !important; font-size: 2.5rem !important; font-weight: bold; }
    </style>
    """, unsafe_allow_html=True)

st.sidebar.title("🛂 DASHBOARD")
es_admin = st.sidebar.checkbox("🔓 MODO ADMIN (DYLAN)")
idioma = st.sidebar.selectbox("Region:", ["🇦🇷 Argentina", "🇺🇸 USA"]) if not es_admin else "Admin"

if idioma == "Admin":
    st.title("👨‍💻 PANEL CENTRAL")
    if st.session_state.mensajes:
        st.table(pd.DataFrame(st.session_state.mensajes))
    else:
        st.write("Sin solicitudes nuevas.")
else:
    banner = "🇦🇷 2 Millones ARS/mes" if "Argentina" in idioma else "🇺🇸 12k USD/month"
    st.markdown(f"<h3 style='border: 2px solid #d4af37; padding: 15px;'>{banner}</h3>", unsafe_allow_html=True)
    st.title("🏛️ COMMAND CENTER")
    
    años = st.slider("AÑOS:", 1, 30, 10)
    ret = st.slider("RETORNO %:", 5, 50, 15)
    fut_usd = 12450000 * ((1 + (ret/100))**años)
    
    col1, col2 = st.columns(2)
    col1.metric("FORTUNA USD", f"${fut_usd:,.0f}")
    col2.metric("FORTUNA ARS", f"${fut_usd * 1500:,.0f}")
    
    st.markdown("---")
    c1, c2 = st.columns(2)
    with c1:
        st.subheader("📊 DISTRIBUCIÓN")
        # ESTA ES LA LÍNEA QUE ARREGLA TODO:
        datos_graficos = pd.DataFrame({"Activo": ["Propiedades", "Stocks", "Crypto", "Art"], "Valor": [40, 30, 20, 10]})
        st.bar_chart(datos_graficos.set_index("Activo"))
    with c2:
        st.subheader("🤖 IA ADVISOR")
        st.write("ESTADO: ACTIVO. DYLAN GARCÍA: HOLD POSITIONS.")

if st.sidebar.button("🔒 CERRAR"):
    st.session_state.autenticado = False
    st.rerun()
