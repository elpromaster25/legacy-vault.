import streamlit as st
import time

# --- 1. RESET Y SEGURIDAD ---
if 'auth' not in st.session_state: st.session_state.auth = False
if 'pago' not in st.session_state: st.session_state.pago = None

# --- 2. CONFIGURACIÓN ---
CEL_PAPA = "5491100000000" # <--- TU CELU ACÁ
MI_MAIL = "dylanelpromaster25@gmail.com"

# --- 3. DISEÑO IMPERIAL ---
st.set_page_config(page_title="LEGACY | VAULT", layout="wide")
st.markdown("""
    <style>
    .stApp { background-color: #000000; border: 5px solid #d4af37; padding: 20px; }
    h1, h2, h3 { color: #d4af37 !important; text-align: center; }
    .gold-card { border: 1px solid #d4af37; padding: 20px; border-radius: 15px; background: rgba(212, 175, 55, 0.05); text-align: center; color: #d4af37; }
    .btn-ws { background-color: #25d366; color: white; padding: 12px; border-radius: 10px; font-weight: bold; text-decoration: none; display: block; text-align: center; margin-bottom: 10px; }
    .btn-ml { background-color: #d4af37; color: black; padding: 12px; border-radius: 10px; font-weight: bold; text-decoration: none; display: block; text-align: center; margin-bottom: 10px; }
    div.stButton > button { background-color: #1a1a1a !important; color: #d4af37 !important; border: 1px solid #d4af37 !important; width: 100%; font-weight: bold; height: 3em; }
    </style>
    """, unsafe_allow_html=True)

# --- 4. PANTALLA DE ENTRADA (SISTEMA ANTI-BUG) ---
if not st.session_state.auth:
    st.title("🏛️ LEGACY QUANTUM VAULT")
    col_l, col_c, col_r = st.columns([1, 1.5, 1])
    
    with col_c:
        v_sel = st.selectbox("📂 SELECT VAULT:", ["ARGENTINA", "USA"], key="v_vault_final")
        st.markdown("<div class='gold-card'>💎 ADQUIRIR TERMINAL CORPORATIVA</div>", unsafe_allow_html=True)
        st.write("")

        # LÓGICA DE PAGOS
        if st.session_state.pago is None:
            if v_sel == "ARGENTINA":
                if st.button("💳 MERCADO PAGO"): st.session_state.pago = "Mercado Pago"; st.rerun()
                if st.button("🏦 CUENTA DNI"): st.session_state.pago = "Cuenta DNI"; st.rerun()
            else:
                if st.button("🔵 PAYPAL"): st.session_state.pago = "PayPal"; st.rerun()
        else:
            m = st.session_state.pago
            st.info(f"Seleccionó: **{m}**. ¿Cómo desea recibir los datos?")
            
            # --- LINKS DE CONTACTO ---
            t_ws = f"Hola, solicito datos de pago para {m} - Legacy Vault."
            u_ws = f"https://api.whatsapp.com{CEL_PAPA}&text={t_ws.replace(' ', '%20')}"
            
            t_ml = f"Solicitud%20de%20pago%20v%C3%ADa%20{m.replace(' ', '%20')}"
            c_ml = f"Hola%20Dylan,%20solicito%20instrucciones%20para%20liquidar%20la%20suscripci%C3%B3n."
            u_ml = f"mailto:{MI_MAIL}?subject={t_ml}&body={c_ml}"
            
            # BOTONES DUALES
            st.markdown(f'<a href="{u_ws}" target="_blank" class="btn-ws">🟢 SOLICITAR POR WHATSAPP</a>', unsafe_allow_html=True)
            st.markdown(f'<a href="{u_ml}" class="btn-ml">📩 SOLICITAR POR EMAIL</a>', unsafe_allow_html=True)
            
            if st.button("⬅️ CAMBIAR MÉTODO"): st.session_state.pago = None; st.rerun()

        st.write("---")
        # INPUTS CON LLAVES ÚNICAS (ANTI-BUG)
        emp = st.text_input("FIRMA / COMPANY:", key="input_emp_final")
        pw = st.text_input("MASTER KEY:", type="password", key="input_pw_final")
        
        if st.button("🔓 ACCEDER", key="btn_acc_final"):
            if pw == "LEGACY2026" and emp:
                st.session_state.emp_final = emp
                st.session_state.auth = True; st.rerun()
            else: st.error("Identificación obligatoria.")
    st.stop()

# --- INTERIOR ---
st.title(f"🏛️ TERMINAL: {st.session_state.emp_final.upper()}")
if st.sidebar.button("🔒 SALIR"):
    st.session_state.auth = False
    st.session_state.pago = None
    st.rerun()
