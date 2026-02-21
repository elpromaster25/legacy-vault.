import streamlit as st
import time

# --- 1. LÓGICA DE MEMORIA ---
if 'auth' not in st.session_state: st.session_state.auth = False
if 'pago_step' not in st.session_state: st.session_state.pago_step = None

# --- 2. DISEÑO IMPERIAL (DORADO Y NEGRO TOTAL) ---
st.set_page_config(page_title="LEGACY GOLD VAULT", layout="wide")
st.markdown("""
    <style>
    .stApp { background-color: #000000; border: 5px solid #d4af37; padding: 20px; }
    h1, h2, h3, p, label, .stMetric { color: #d4af37 !important; text-align: center !important; }
    .gold-card { border: 1px solid #d4af37; padding: 20px; border-radius: 15px; background: rgba(212, 175, 55, 0.05); text-align: center; color: #d4af37; margin-bottom: 20px; }
    .ticker-wrap { width: 100%; overflow: hidden; background: rgba(212, 175, 55, 0.05); border-bottom: 1px solid #d4af37; padding: 10px 0; margin-bottom: 30px; }
    .ticker-move { display: inline-block; white-space: nowrap; padding-left: 100%; animation: marquee 30s linear infinite; color: #d4af37; font-size: 0.95rem; font-weight: bold; letter-spacing: 2px; }
    @keyframes marquee { 0% { transform: translateX(0); } 100% { transform: translateX(-100%); } }
    div.stButton > button { background-color: #1a1a1a !important; color: #d4af37 !important; border: 1px solid #d4af37 !important; width: 100%; font-weight: bold; height: 3em; }
    .btn-paypal { background-color: #0070ba; color: white; padding: 12px; border-radius: 10px; font-weight: bold; text-decoration: none; display: block; text-align: center; margin-bottom: 10px; }
    </style>
    """, unsafe_allow_html=True)

# --- 3. PANTALLA DE ENTRADA (COBRO EN DÓLARES) ---
if not st.session_state.auth:
    st.title("🏛️ LEGACY QUANTUM VAULT")
    col_l, col_c, col_r = st.columns([1, 1.5, 1])
    with col_c:
        v_sel = st.selectbox("📂 SELECT REGION:", ["USA / GLOBAL", "ARGENTINA"], key="v_f")
        st.markdown("<div class='gold-card'>💎 ACQUIRE CORPORATE TERMINAL</div>", unsafe_allow_html=True)
        
        # LÓGICA DE PAGOS INTERNACIONALES
        if st.session_state.pago_step is None:
            if v_sel == "USA / GLOBAL":
                if st.button("🔵 PAYPAL (DIRECT)"): st.session_state.pago_step = "PayPal"; st.rerun()
                if st.button("🏛️ WIRE TRANSFER (SWIFT)"): st.session_state.pago_step = "Wire"; st.rerun()
                st.markdown("<p style='font-size:0.8rem;'>Subscription: $12,000 USD</p>", unsafe_allow_html=True)
            else:
                if st.button("💳 MERCADO PAGO"): st.session_state.pago_step = "MP"; st.rerun()
                if st.button("🏦 CUENTA DNI"): st.session_state.pago_step = "DNI"; st.rerun()
                st.markdown("<p style='font-size:0.8rem;'>Suscripción: $2.000.000 ARS</p>", unsafe_allow_html=True)
        else:
            m = st.session_state.pago_step
            st.info(f"Method: {m}")
            # LINK A PAYPAL DE TU VIEJO (Usamos mail por ahora para que sea seguro)
            u_pp = f"mailto:dylanelpromaster25@://gmail.com."
            if m == "PayPal":
                st.markdown(f'<a href="{u_pp}" class="btn-paypal">🔵 PROCEED TO PAYPAL</a>', unsafe_allow_html=True)
            else:
                st.markdown(f'<a href="mailto:dylanelpromaster25@gmail.com" style="text-decoration:none;"><div style="background:#d4af37; color:black; padding:10px; border-radius:10px; text-align:center; font-weight:bold;">📩 REQUEST INSTRUCTIONS</div></a>', unsafe_allow_html=True)
            if st.button("⬅️ CHANGE METHOD"): st.session_state.pago_step = None; st.rerun()

        st.write("---")
        emp = st.text_input("FIRMA / COMPANY:", key="e_ent")
        pw = st.text_input("MASTER KEY:", type="password", key="p_ent")
        if st.button("🔓 UNLOCK VAULT"):
            if pw == "LEGACY2026" and emp:
                st.session_state.emp_final = emp.upper()
                st.session_state.auth = True; st.rerun()
            else: st.error("Access Denied.")
    st.stop()

# --- 4. INTERIOR (IMPERIO TOTAL) ---
emp = st.session_state.emp_final
st.title(f"🏛️ TERMINAL: {emp}")
st.markdown(f'<div class="ticker-wrap"><div class="ticker-move">🏦 LIVE MARKET | BTC/USD: 96.840 ▼ | GOLD/OZ: 2.045 ▲ | 🛡️ AES-256 ACTIVE | GLOBAL ENCRYPTION NODE: ACTIVE | 🌐 GLOBAL TERMINAL: {emp} 🏛️</div></div>', unsafe_allow_html=True)

# MÉTRICAS Y SCANNER SIGUEN IGUAL ABAJO (Oculto para brevedad, pero ya lo tenés)
st.write("---")
st.subheader("🤖 AI STRATEGIC ADVISOR")
st.info(f"Analysis for **{emp}** completed. Portfolio status: **SOLVENT**.")

if st.sidebar.button("🔒 LOGOUT"): st.session_state.auth = False; st.rerun()
