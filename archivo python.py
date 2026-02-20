import streamlit as st
import pandas as pd
import time

# --- 1. RESET Y BASE DE DATOS INTERNA ---
if 'auth' not in st.session_state: st.session_state.auth = False
if 'reg_final' not in st.session_state: st.session_state.reg_final = None
if 'solicitudes' not in st.session_state: st.session_state.solicitudes = []

# --- 2. DISEÑO IMPERIAL ---
st.set_page_config(page_title="LEGACY GOLD", layout="wide")
st.markdown("""
    <style>
    .stApp { background-color: #000000; border: 6px solid #d4af37; padding: 20px; }
    h1, h2, h3 { color: #d4af37 !important; text-align: center; font-family: 'serif'; }
    .gold-card { border: 2px solid #d4af37; padding: 20px; border-radius: 15px; background: rgba(212, 175, 55, 0.05); text-align: center; color: #d4af37; }
    div.stButton > button { background-color: #1a1a1a; color: #d4af37; border: 2px solid #d4af37; width: 100%; font-weight: bold; }
    </style>
    """, unsafe_allow_html=True)

# --- 3. PANTALLA DE ENTRADA CON BUZÓN PARA EMPRESAS ---
if not st.session_state.auth:
    st.title("🏛️ LEGACY QUANTUM VAULT")
    col_iz, col_ce, col_de = st.columns([1, 1.5, 1])
    
    with col_ce:
        st.markdown("<div class='gold-card'>💎 ACCESO RESTRINGIDO | 12.000 USD</div>", unsafe_allow_html=True)
        st.write("")
        
        # SELECTOR POR BOTONES (ANTI-ERROR)
        st.subheader("Seleccione Región / Select Region:")
        c1, c2 = st.columns(2)
        if c1.button("🇦🇷 ARGENTINA"): st.session_state.reg_final = "Argentina"
        if c2.button("🇺🇸 USA"): st.session_state.reg_final = "USA"
        
        if st.session_state.reg_final:
            pw = st.text_input(f"PASSWORD ({st.session_state.reg_final}):", type="password", key="pass_final_99")
            if st.button("DESBLOQUEAR / UNLOCK"):
                if pw == "LEGACY2026":
                    st.session_state.auth = True
                    st.rerun()
                else: st.error("DENEGADO / DENIED")
        
        st.write("---")
        # EL RADAR: BUZÓN PARA LOS QUE NO TIENEN CLAVE
        st.subheader("📩 ¿NO TIENE LLAVE MAESTRA?")
        st.write("Deje su contacto corporativo para solicitar acceso VIP.")
        with st.form("solicitud_acceso"):
            email_corp = st.text_input("Email de la Empresa:")
            nota_corp = st.text_area("Motivo de la consulta:")
            if st.form_submit_button("SOLICITAR ACCESO DIRECTO"):
                if email_corp:
                    # Se guarda en tu Modo Admin
                    st.session_state.solicitudes.append({"Empresa": email_corp, "Nota": nota_corp, "Hora": time.strftime('%H:%M')})
                    st.success("✅ Solicitud enviada al Founder Dylan García.")
                else: st.warning("Ingrese un email válido.")

    st.stop()

# --- 4. INTERFAZ INTERNA (SOLO CON CLAVE) ---
reg = st.session_state.reg_final
st.title(f"🏛️ COMMAND CENTER - {reg}")

# SIMULADOR Y EXCHANGE (Lo que ya tenías)
m1, m2 = st.columns(2)
m1.metric("USD VALUE", "$12,450,000")
st.write("---")
st.subheader("💹 EXCHANGE VIP")
if st.button("📩 SOLICITAR COTIZACIÓN POR EMAIL"):
    st.markdown(f'<a href="mailto:dylanelpromaster25@gmail.com">Click aquí</a>', unsafe_allow_html=True)

# --- 5. MODO ADMIN (SOLO PARA VOS) ---
if st.sidebar.checkbox("🔓 MODO ADMIN (DYLAN)"):
    if st.sidebar.text_input("CLAVE ESPÍA:", type="password") == "DYLAN777":
        st.sidebar.write("📬 EMPRESAS QUE PIDIERON ENTRAR:")
        if st.session_state.solicitudes:
            st.sidebar.table(pd.DataFrame(st.session_state.solicitudes))
        else: st.sidebar.info("Nadie pidió entrar todavía.")

if st.sidebar.button("🔒 SALIR"):
    st.session_state.auth = False
    st.rerun()
