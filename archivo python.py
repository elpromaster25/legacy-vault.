import streamlit as st
import time

# --- 1. CONFIGURACIÓN ---
if 'auth' not in st.session_state: st.session_state.auth = False
if 'payment_step' not in st.session_state: st.session_state.payment_step = None
CEL_PAPA = "5491100000000" # <--- TU CELULAR ACÁ

# --- 2. DISEÑO IMPERIAL ---
st.set_page_config(page_title="LEGACY | SECURE PAY", layout="wide")
st.markdown("""
    <style>
    .stApp { background-color: #000000; border: 4px solid #d4af37; padding: 20px; }
    h1, h2, h3 { color: #d4af37 !important; text-align: center; }
    .gold-card { border: 1px solid #d4af37; padding: 15px; border-radius: 10px; background: rgba(212, 175, 55, 0.05); text-align: center; color: #d4af37; }
    .payment-option { background-color: #1a1a1a; color: #d4af37; border: 1px solid #d4af37; width: 100%; padding: 10px; border-radius: 8px; font-weight: bold; cursor: pointer; text-align: center; display: block; text-decoration: none; margin-bottom: 10px; }
    .payment-option:hover { background-color: #d4af37; color: black; }
    div.stButton > button { background-color: #1a1a1a; color: #d4af37; border: 1px solid #d4af37; width: 100%; font-weight: bold; }
    </style>
    """, unsafe_allow_html=True)

# --- 3. PANTALLA DE ENTRADA CON FILTRO ---
if not st.session_state.auth:
    st.title("🏛️ LEGACY QUANTUM VAULT")
    col_l, col_c, col_r = st.columns([1, 1.5, 1])
    
    with col_c:
        v_sel = st.selectbox("📂 SELECT VAULT:", ["🇦🇷 ARGENTINA", "🇺🇸 USA"], key="v_sel")
        st.markdown("<div class='gold-card'>💎 ADQUIRIR TERMINAL CORPORATIVA</div>", unsafe_allow_html=True)
        st.write("")

        # PASO 1: ELEGIR EL MÉTODO (SIN CONTACTO TODAVÍA)
        if st.session_state.payment_step is None:
            if v_sel == "🇦🇷 ARGENTINA":
                if st.button("💳 MERCADO PAGO"): st.session_state.payment_step = "MP"; st.rerun()
                if st.button("🏦 CUENTA DNI"): st.session_state.payment_step = "DNI"; st.rerun()
            else:
                if st.button("🔵 PAYPAL / STRIPE"): st.session_state.payment_step = "USA"; st.rerun()
        
        # PASO 2: ELEGIR EL CANAL (SOLO SI TOCÓ EL MÉTODO)
        else:
            metodo = st.session_state.payment_step
            st.info(f"Ha seleccionado: **{metodo}**. ¿Cómo desea recibir los datos de transferencia?")
            c1, c2 = st.columns(2)
            
            # LINKS DE CONTACTO DINÁMICOS
            msg_ws = f"https://wa.me{CEL_PAPA}?text=Hola,%20solicito%20datos%20de%20pago%20para%20{metodo}%20-%20Legacy%20Vault."
            msg_ml = f"mailto:dylanelpromaster25@://gmail.com{metodo}"
            
            with c1: st.markdown(f'<a href="{msg_ws}" class="payment-option">🟢 WHATSAPP</a>', unsafe_allow_html=True)
            with c2: st.markdown(f'<a href="{msg_ml}" class="payment-option">📩 EMAIL</a>', unsafe_allow_html=True)
            
            if st.button("⬅️ CAMBIAR MÉTODO"): st.session_state.payment_step = None; st.rerun()

        st.write("---")
        # ACCESO CON LLAVE
        emp = st.text_input("FIRMA / COMPANY:", key="e_fix")
        pw = st.text_input("MASTER KEY:", type="password", key="p_fix")
        if st.button("🔓 ACCEDER"):
            if pw == "LEGACY2026" and emp:
                st.session_state.emp_final = emp
                st.session_state.auth = True; st.rerun()
            else: st.error("Identificación obligatoria.")
    st.stop()

# --- 4. INTERIOR ---
st.title(f"🏛️ TERMINAL: {st.session_state.emp_final.upper()}")
if st.sidebar.button("🔒 SALIR"): st.session_state.auth = False; st.rerun()
