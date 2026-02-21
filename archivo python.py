import streamlit as st
import time

# --- 1. LÓGICA DE SESIÓN ---
if 'auth' not in st.session_state: st.session_state.auth = False

# --- 2. DISEÑO IMPERIAL (CSS) ---
st.set_page_config(page_title="LEGACY | PREMIUM", layout="wide")
st.markdown("""
    <style>
    .stApp { background-color: #000000; border: 4px solid #d4af37; padding: 20px; }
    h1, h2, h3 { color: #d4af37 !important; text-align: center; }
    .gold-card { border: 1px solid #d4af37; padding: 15px; border-radius: 10px; background: rgba(212, 175, 55, 0.05); text-align: center; color: #d4af37; }
    .payment-badge { background: #1a1a1a; border: 1px solid #d4af37; padding: 10px; border-radius: 8px; font-size: 0.8rem; margin: 5px; display: inline-block; width: 100%; }
    div.stButton > button { background-color: #1a1a1a; color: #d4af37; border: 1px solid #d4af37; width: 100%; font-weight: bold; }
    .custom-btn { background-color: #d4af37 !important; color: black !important; font-weight: bold !important; width: 100%; border-radius: 10px; height: 45px; }
    </style>
    """, unsafe_allow_html=True)

# --- 3. PANTALLA DE ENTRADA (ESTRATEGIA DE COBRO) ---
if not st.session_state.auth:
    st.title("🏛️ LEGACY QUANTUM VAULT")
    col_l, col_c, col_r = st.columns([1, 1.5, 1])
    
    with col_c:
        # REGIÓN / VAULT
        v_sel = st.selectbox("📂 SELECT VAULT:", ["🇦🇷 ARGENTINA", "🇺🇸 USA"], key="v1")
        
        # --- SECCIÓN DE PAGOS ARRIBA DE LA CONTRA ---
        st.markdown("<div class='gold-card'>💎 ADQUIRIR TERMINAL CORPORATIVA</div>", unsafe_allow_html=True)
        
        p1, p2 = st.columns(2)
        if v_sel == "🇦🇷 ARGENTINA":
            with p1: st.markdown("<div class='payment-badge'>💳 MERCADO PAGO</div>", unsafe_allow_html=True)
            with p2: st.markdown("<div class='payment-badge'>🏦 CUENTA DNI</div>", unsafe_allow_html=True)
            st.markdown("<h3 style='font-size:1.2rem;'>SUSCRIPCIÓN: $2.000.000 ARS</h3>", unsafe_allow_html=True)
        else:
            with p1: st.markdown("<div class='payment-badge'>🔵 PAYPAL</div>", unsafe_allow_html=True)
            with p2: st.markdown("<div class='payment-badge'>🛡️ STRIPE</div>", unsafe_allow_html=True)
            st.markdown("<h3 style='font-size:1.2rem;'>SUBSCRIPTION: $12.000 USD</h3>", unsafe_allow_html=True)
        
        st.write("---")
        
        # IDENTIFICACIÓN Y LLAVE (GRATIS)
        st.markdown("<p style='text-align:center; font-size:0.8rem;'>IDENTIFIQUE SU FIRMA PARA USAR SU LLAVE DE CORTESÍA</p>", unsafe_allow_html=True)
        emp = st.text_input("FIRMA / COMPANY:", key="e1")
        pw = st.text_input("MASTER KEY:", type="password", key="p1")
        
        if st.button("🔓 ACCEDER A BÓVEDA"):
            if pw == "LEGACY2026" and emp:
                st.session_state.emp_final = emp
                st.session_state.auth = True; st.rerun()
            else: st.error("Firma y Llave obligatorias.")
            
    st.stop()

# --- 4. INTERIOR (COMMAND CENTER) ---
emp = st.session_state.emp_final
st.title(f"🏛️ TERMINAL: {emp.upper()}")

st.write("---")
# BOTÓN DE PERSONALIZACIÓN (EL NEGOCIO)
st.markdown("<div class='gold-card'><b>¿DESEA UNA TERMINAL PERSONALIZADA?</b><br>Desarrollamos su Bóveda Privada con sus activos reales.</div>", unsafe_allow_html=True)
asunto = f"CONSULTA%20TERMINAL%20-%20{emp}"
mail_link = f"mailto:dylanelpromaster25@://gmail.com{asunto}"
st.markdown(f'<a href="{mail_link}" target="_blank"><button class="custom-btn">📩 SOLICITAR DESARROLLO EXCLUSIVO (VIP)</button></a>', unsafe_allow_html=True)

st.write("---")
# ACTIVOS
c1, c2, c3 = st.columns(3)
with c1: st.metric("REAL ESTATE", "$85M")
with c2: st.metric("YACHTS", "$12.5M")
with c3: st.metric("JETS", "$24M")

if st.sidebar.button("🔒 SALIR"): st.session_state.auth = False; st.rerun()
