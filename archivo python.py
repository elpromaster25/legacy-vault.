import streamlit as st
import time

# --- 1. RESET TOTAL DE MEMORIA ---
if 'auth' not in st.session_state: st.session_state.auth = False
if 'pago' not in st.session_state: st.session_state.pago = None

# --- 2. CONFIGURACIÓN CELULAR ---
CEL_PAPA = "5491100000000" # <--- PONELO ACÁ SIN ESPACIOS

# --- 3. DISEÑO IMPERIAL ---
st.set_page_config(page_title="LEGACY | VAULT", layout="wide")
st.markdown("""
    <style>
    .stApp { background-color: #000000; border: 5px solid #d4af37; padding: 20px; }
    h1, h2, h3 { color: #d4af37 !important; text-align: center; }
    .gold-card { border: 1px solid #d4af37; padding: 20px; border-radius: 15px; background: rgba(212, 175, 55, 0.05); text-align: center; color: #d4af37; }
    .payment-btn { background-color: #d4af37; color: black; padding: 12px; border-radius: 10px; font-weight: bold; text-decoration: none; display: block; text-align: center; margin-bottom: 10px; }
    div.stButton > button { background-color: #1a1a1a !important; color: #d4af37 !important; border: 1px solid #d4af37 !important; width: 100%; font-weight: bold; }
    </style>
    """, unsafe_allow_html=True)

# --- 4. PANTALLA DE ENTRADA (SISTEMA ANTI-BUG) ---
if not st.session_state.auth:
    st.title("🏛️ LEGACY QUANTUM VAULT")
    col_l, col_c, col_r = st.columns([1, 1.5, 1])
    
    with col_c:
        # SELECTOR CON LLAVE ÚNICA PARA QUE NO SE TRABE
        v_sel = st.selectbox("📂 SELECT VAULT:", ["ARGENTINA", "USA"], key="v_vault_99")
        st.markdown("<div class='gold-card'>💎 ADQUIRIR TERMINAL CORPORATIVA</div>", unsafe_allow_html=True)
        st.write("")

        # LÓGICA DE PAGOS
        if st.session_state.pago is None:
            if v_sel == "ARGENTINA":
                if st.button("💳 MERCADO PAGO", key="btn_mp"): st.session_state.pago = "Mercado Pago"; st.rerun()
                if st.button("🏦 CUENTA DNI", key="btn_dni"): st.session_state.pago = "Cuenta DNI"; st.rerun()
            else:
                if st.button("🔵 PAYPAL", key="btn_pp"): st.session_state.pago = "PayPal"; st.rerun()
        else:
            # CONTACTO SEGURO
            m = st.session_state.pago
            ws_url = f"https://api.whatsapp.com{CEL_PAPA}&text=Hola,%20solicito%20datos%20de%20pago%20para%20{m.replace(' ', '%20')}%20-%20Legacy."
            st.markdown(f'<a href="{ws_url}" target="_blank" class="payment-btn">🟢 HABLAR POR WHATSAPP</a>', unsafe_allow_html=True)
            if st.button("⬅️ CAMBIAR MÉTODO", key="btn_back"): st.session_state.pago = None; st.rerun()

        st.write("---")
        # --- ACÁ ESTÁ EL ARREGLO DEL BORRADO ---
        # Usamos 'key' dinámicas para que el navegador no "recuerde" el texto viejo
        emp = st.text_input("FIRMA / COMPANY:", key="input_empresa_total_1")
        pw = st.text_input("MASTER KEY:", type="password", key="input_pass_total_1")
        
        if st.button("🔓 ACCEDER", key="btn_final_access"):
            if pw == "LEGACY2026" and emp:
                st.session_state.emp_final = emp
                st.session_state.auth = True
                st.rerun()
            else:
                st.error("Identificación obligatoria.")
    st.stop()

# --- INTERIOR ---
st.title(f"🏛️ TERMINAL: {st.session_state.emp_final.upper()}")
if st.sidebar.button("🔒 SALIR", key="btn_logout"):
    st.session_state.auth = False
    st.session_state.pago = None
    st.rerun()
