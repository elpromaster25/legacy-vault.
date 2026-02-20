import streamlit as st
import pandas as pd
import time

# --- 1. BASE DE DATOS Y ESTADOS ---
if 'auth' not in st.session_state: st.session_state.auth = False
if 'solicitudes' not in st.session_state: st.session_state.solicitudes = []

# --- 2. DISEÑO DE ALTA GAMA (CSS) ---
st.set_page_config(page_title="LEGACY GOLD", layout="wide")
st.markdown("""
    <style>
    .stApp { background-color: #000000; border: 5px solid #d4af37; padding: 30px; }
    h1, h2, h3 { color: #d4af37 !important; text-align: center; font-family: 'serif'; }
    .gold-card { border: 1px solid #d4af37; padding: 25px; border-radius: 15px; background: rgba(212, 175, 55, 0.05); text-align: center; color: #d4af37; }
    div.stButton > button { background-color: #1a1a1a; color: #d4af37; border: 1px solid #d4af37; width: 100%; height: 3em; font-weight: bold; }
    .stTextInput > div > div > input { background-color: #1a1a1a; color: #d4af37; border: 1px solid #d4af37; }
    </style>
    """, unsafe_allow_html=True)

# --- 3. PANTALLA DE ENTRADA ORGANIZADA ---
if not st.session_state.auth:
    st.title("🏛️ LEGACY QUANTUM VAULT")
    
    col_l, col_c, col_r = st.columns([1, 1.5, 1])
    
    with col_c:
        # SECCIÓN 1: SELECCIÓN DE REGIÓN
        region = st.selectbox("🌎 SELECCIONE REGIÓN / REGION:", ["🇦🇷 Argentina", "🇺🇸 USA"], key="reg_fix")
        st.write("---")
        
        # SECCIÓN 2: ACCESO CON CLAVE (BIEN LIMPIO)
        st.markdown(f"<div class='gold-card'>🔑 LLAVE MAESTRA REQUERIDA<br>{'2.000.000 ARS' if 'Arg' in region else '12.000 USD'}</div>", unsafe_allow_html=True)
        st.write("")
        pw = st.text_input("PASSWORD:", type="password", key="pw_fix")
        if st.button("DESBLOQUEAR / UNLOCK"):
            if pw == "LEGACY2026":
                st.session_state.auth = True
                st.session_state.reg_final = region
                st.rerun()
            else: st.error("DENEGADO")
            
        st.write("---")
        
        # SECCIÓN 3: BUZÓN PARA EMPRESARIOS (DISCRETO)
        with st.expander("📩 ¿NO TIENE ACCESO? SOLICITAR AQUÍ"):
            with st.form("solicitud"):
                email = st.text_input("Email Corporativo:")
                nota = st.text_area("Propuesta:")
                if st.form_submit_button("ENVIAR SOLICITUD VIP"):
                    if email:
                        st.session_state.solicitudes.append({"Empresa": email, "Nota": nota, "Hora": time.strftime('%H:%M')})
                        st.success("✅ Solicitud enviada a Dylan García.")
    st.stop()

# --- 4. INTERFAZ INTERNA (EL PRODUCTO) ---
t = st.session_state.reg_final
st.title(f"🏛️ COMMAND CENTER - {t}")
st.write("---")

m1, m2 = st.columns(2)
m1.metric("USD VALUE", "$12,450,000")
if "Arg" in t: m2.metric("ARS VALUE", "$18,799,500,000")

st.write("---")
st.subheader("💹 EXCHANGE & IA ADVISOR")
st.info("Utilice la barra lateral para cerrar sesión o entrar al Modo Admin.")

# MODO ADMIN EN SIDEBAR
if st.sidebar.checkbox("🔓 MODO ADMIN (DYLAN)"):
    if st.sidebar.text_input("CLAVE:", type="password") == "DYLAN777":
        st.sidebar.write("📬 SOLICITUDES EN VIVO:")
        if st.session_state.solicitudes: st.sidebar.table(pd.DataFrame(st.session_state.solicitudes))
        else: st.sidebar.info("Sin mensajes nuevos.")

if st.sidebar.button("🔒 SALIR"):
    st.session_state.auth = False
    st.rerun()
