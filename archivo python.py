import streamlit as st
import pandas as pd
import time

# --- 1. SEGURIDAD Y PANTALLA DE ENTRADA CON PRECIOS EN ORO ---
if 'autenticado' not in st.session_state:
    st.session_state.autenticado = False
if 'mensajes' not in st.session_state:
    st.session_state.mensajes = []

if not st.session_state.autenticado:
    st.set_page_config(page_title="LEGACY | LOGIN", page_icon="🔐", layout="wide")
    st.markdown("""
        <style>
        .stApp { background-color: #000000; }
        h1 { color: #d4af37 !important; text-align: center; font-family: 'serif'; font-size: 4rem !important; }
        
        /* PRECIOS EN ORO ARRIBA DE LA CONTRASEÑA */
        .gold-price {
            color: #d4af37;
            font-size: 1.5rem;
            text-align: center;
            font-weight: bold;
            text-transform: uppercase;
            letter-spacing: 2px;
            margin-bottom: 10px;
            font-family: 'serif';
        }
        
        .info-box {
            color: #d4af37; font-size: 1.2rem; text-align: center; border: 1px solid #d4af37;
            padding: 20px; border-radius: 15px; background-color: rgba(212, 175, 55, 0.05);
            min-height: 250px; display: flex; align-items: center; justify-content: center; flex-direction: column;
        }
        div.stButton > button {
            background-color: #1a1a1a; color: #d4af37; border: 2px solid #d4af37; width: 100%; font-weight: bold;
        }
        </style>
        """, unsafe_allow_html=True)
    
    st.title("🏛️ LEGACY QUANTUM VAULT")
    
    # SECCIÓN DE PRECIOS Y LOGIN
    col_l, col_c, col_r = st.columns([1, 1.5, 1])
    with col_c:
        # LOS CARTELES EN ORO QUE PEDISTE
        st.markdown("<div class='gold-price'>🇦🇷 ARGENTINA: 2 MILLONES / MES</div>", unsafe_allow_html=True)
        st.markdown("<div class='gold-price'>🇺🇸 USA: 12 THOUSAND USD / MONTH</div>", unsafe_allow_html=True)
        
        password = st.text_input("LLAVE MAESTRA / MASTER KEY:", type="password")
        if st.button("DESBLOQUEAR TERMINAL"):
            if password == "LEGACY2026":
                st.session_state.autenticado = True
                st.rerun()
            else:
                st.error("ACCESO DENEGADO")
    
    st.write("---")
    st.subheader("📩 SOLICITUD DE ACCESO VIP")
    
    c_izq, c_mid, c_der = st.columns([1.5, 2, 1.5])
    with c_izq: st.markdown("<div class='info-box'>🛡️ PROTECCIÓN<br><br>Cifrado AES-256. Activos bajo custodia digital absoluta.</div>", unsafe_allow_html=True)
    with c_mid:
        with st.form("contacto_vip"):
            perfil = st.radio("Perfil:", ["💼 Empresario", "🦈 Inversor"])
            mail = st.text_input("Email:")
            if st.form_submit_button("ENVIAR SOLICITUD"):
                if mail:
                    st.session_state.mensajes.append({"perfil": perfil, "mail": mail, "hora": time.strftime('%H:%M')})
                    st.success("✅ ENVIADO.")
    with c_der: st.markdown("<div class='info-box'>📈 CRECIMIENTO<br><br>IA de predicción macroeconómica en tiempo real.</div>", unsafe_allow_html=True)
    st.stop()

# --- 2. INTERIOR DE LA BÓVEDA ---
st.set_page_config(page_title="LEGACY COMMAND", page_icon="🏛️", layout="wide")
st.markdown("<style>.stApp { background-color: #050505; border: 4px solid #d4af37; padding: 20px; } h1, h2, h3 { color: #d4af37 !important; text-align: center; } [data-testid='stMetricValue'] { color: #d4af37 !important; font-size: 2.5rem !important; font-weight: bold; }</style>", unsafe_allow_html=True)

st.sidebar.title("🛂 DASHBOARD")
es_admin = st.sidebar.checkbox("🔓 MODO ADMIN (DYLAN)")
idioma = st.sidebar.selectbox("Region:", ["🇦🇷 Argentina", "🇺🇸 USA"]) if not es_admin else "Admin"

# TRADUCCIONES IA
ia_conf = {
    "🇦🇷 Argentina": {"preg": "CONSULTA PARA LA IA:", "resp": "IA: Dylan García, analizando... La orden es MANTENER."},
    "🇺🇸 USA": {"preg": "QUERY FOR AI:", "resp": "AI: Dylan Garcia, analyzing... The order is to HOLD."},
    "Admin": {"preg": "SYSTEM COMMAND:", "resp": "MASTER IA: Systems online. Capital secured."}
}
iat = ia_conf[idioma]

if idioma == "Admin":
    st.title("👨‍💻 PANEL CENTRAL")
    if st.session_state.mensajes: st.table(pd.DataFrame(st.session_state.mensajes))
    else: st.write("Sin solicitudes.")
else:
    st.title("🏛️ COMMAND CENTER")
    años = st.slider("AÑOS:", 1, 30, 10); ret = st.slider("RETORNO %:", 5, 50, 15)
    fut_usd = 12450000 * ((1 + (ret/100))**años)
    col1, col2 = st.columns(2)
    col1.metric("FORTUNA USD", f"${fut_usd:,.0f}"); col2.metric("FORTUNA ARS", f"${fut_usd * 1500:,.0f}")
    st.markdown("---")
    c1, c2 = st.columns(2)
    with c1:
        st.subheader("📊 DISTRIBUCIÓN")
        df_f = pd.DataFrame({"Activo": ["RE", "Stocks", "Crypto", "Art"], "Valor":})
        st.bar_chart(df_f.set_index("Activo"))
    with c2:
        st.subheader("🤖 IA ADVISOR")
        # --- IA FUNCIONANDO ---
        pregunta_ia = st.text_input(iat["preg"])
        if pregunta_ia:
            with st.spinner('Analizando...'):
                time.sleep(1)
                st.write(f"🏛️ **{iat['resp']}**")

if st.sidebar.button("🔒 CERRAR"):
    st.session_state.autenticado = False
    st.rerun()
