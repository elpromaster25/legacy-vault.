import streamlit as st
import pandas as pd
import time

# --- 1. RESET Y SEGURIDAD ---
if 'auth' not in st.session_state: st.session_state.auth = False
if 'demo' not in st.session_state: st.session_state.demo = False

# --- 2. DISEÑO IMPERIAL ---
st.set_page_config(page_title="LEGACY | VAULT", layout="wide")
st.markdown("""
    <style>
    .stApp { background-color: #000000; border: 6px solid #d4af37; padding: 20px; }
    h1, h2, h3 { color: #d4af37 !important; text-align: center; font-family: 'serif'; }
    .gold-card { border: 2px solid #d4af37; padding: 20px; border-radius: 15px; background: rgba(212, 175, 55, 0.05); text-align: center; color: #d4af37; }
    div.stButton > button { background-color: #1a1a1a; color: #d4af37; border: 2px solid #d4af37; width: 100%; font-weight: bold; }
    </style>
    """, unsafe_allow_html=True)

# --- 3. PANTALLA DE ENTRADA (SISTEMA ANTI-BUG) ---
if not st.session_state.auth and not st.session_state.demo:
    st.title("🏛️ LEGACY QUANTUM VAULT")
    col_l, col_c, col_r = st.columns([1, 1.5, 1])
    
    with col_c:
        # CONTENEDOR 1: SELECCIÓN (ID ÚNICO)
        st.markdown("### 🌎 SELECT VAULT")
        v_sel = st.selectbox("CHOOSE REGION:", ["ARGENTINA", "USA"], key="v_final_secure_777")
        
        st.write("---")
        
        # CONTENEDOR 2: ACCESO
        st.markdown("<div class='gold-card'>🚀 AUDITORÍA GRATUITA (5 MIN)</div>", unsafe_allow_html=True)
        if st.button("🚀 INICIAR DEMO", key="btn_demo_777"):
            st.session_state.demo = True
            st.session_state.reg_final = v_sel
            st.session_state.start_time = time.time()
            st.rerun()
            
        st.write("---")
        st.markdown("<div class='gold-card'>🔑 LLAVE MAESTRA</div>", unsafe_allow_html=True)
        pw = st.text_input("MASTER KEY:", type="password", key="pw_final_secure_777")
        
        if st.button("🔓 DESBLOQUEAR", key="btn_unlock_777"):
            if pw == "LEGACY2026":
                st.session_state.auth = True
                st.session_state.reg_final = v_sel
                st.rerun()
            else: st.error("DENEGADO")
    st.stop()

# --- 4. MURO DE PAGO (SOLO SI EXPIRA) ---
if st.session_state.demo and not st.session_state.auth:
    transcurrido = time.time() - st.session_state.start_time
    if transcurrido > 300:
        st.title("⌛ DEMO FINALIZADA")
        st.markdown(f"<div class='gold-card'>ADQUIERA SU LLAVE: {'2.000.000 ARS' if 'ARG' in st.session_state.reg_final else '12.000 USD'}</div>", unsafe_allow_html=True)
        st.info("📩 Envíe comprobante a: dylanelpromaster25@gmail.com")
        if st.button("⬅️ VOLVER"):
            st.session_state.demo = False
            st.rerun()
        st.stop()

# --- 5. INTERIOR (EL IMPERIO) ---
st.title(f"🏛️ COMMAND CENTER - {st.session_state.reg_final}")
st.write("---")

# Métricas Principales
c1, c2 = st.columns(2)
c1.metric("PATRIMONIO USD", "$12,450,000")
if "ARG" in st.session_state.reg_final:
    c2.metric("PATRIMONIO ARS", "$18.799.500.000")

st.write("---")
# Simulador de Inversión
años = st.slider("PROYECCIÓN (AÑOS):", 1, 30, 10)
ret = st.slider("RENTABILIDAD (%):", 5, 50, 15)
st.write(f"Resultado estimado: **${12450000 * ((1 + (ret/100))**años):,.0f} USD**")

st.write("---")
# IA Estratégica
st.subheader("🤖 ESTRATEGA IA")
q = st.text_input("CONSULTA:", key="ia_777")
if q: st.write("🏛️ **IA:** Dylan García, la orden es MANTENER POSICIONES.")

if st.sidebar.button("🔒 SALIR", key="exit_777"):
    st.session_state.auth = False
    st.session_state.demo = False
    st.rerun()
