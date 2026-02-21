import streamlit as st
import time

# --- 1. SEGURIDAD ---
VIP = ["EMAAR", "GINEVRA", "REMAX", "THE AGENCY", "CARSO", "LEGACY", "DYLAN", "ADMIN", "SOTHEBYS", "HINES"]
if 'auth' not in st.session_state: st.session_state.auth = False

# --- 2. DISEÑO IMPERIAL ---
st.set_page_config(page_title="LEGACY GOLD VAULT", layout="wide")
st.markdown("""
    <style>
    .stApp { background-color: #000; border: 5px solid #d4af37; padding: 20px; }
    h1, h2, h3, p, label, .stMetric { color: #d4af37 !important; text-align: center !important; }
    .gold-card { border: 1px solid #d4af37; padding: 20px; border-radius: 15px; background: rgba(212, 175, 55, 0.05); text-align: center; margin-bottom: 20px; }
    .btn-paypal { background-color: #0070ba; color: white !important; padding: 14px; border-radius: 10px; font-weight: bold; text-decoration: none; display: block; text-align: center; margin-bottom: 10px; border: 1px solid #fff; font-size: 1.2rem; }
    .btn-mp { background-color: #009ee3; color: white !important; padding: 14px; border-radius: 10px; font-weight: bold; text-decoration: none; display: block; text-align: center; margin-bottom: 10px; border: 1px solid #fff; }
    div.stButton > button { background-color: #1a1a1a !important; color: #d4af37 !important; border: 1px solid #d4af37 !important; width: 100%; font-weight: bold; height: 3.5em; }
    </style>
    """, unsafe_allow_html=True)

# --- 3. PANTALLA DE ENTRADA ---
if not st.session_state.auth:
    st.title("🏛️ LEGACY QUANTUM VAULT")
    reg = st.selectbox("🌐 SELECT REGION / ELIJA REGIÓN:", ["USA / GLOBAL", "ARGENTINA"])
    _, col_c, _ = st.columns([1, 1.5, 1])
    with col_c:
        st.markdown("<div class='gold-card'>🔒 NODO PRIVADO AUTORIZADO</div>", unsafe_allow_html=True)
        
        if reg == "USA / GLOBAL":
            st.write("Subscription: **$12,000 USD**")
            # FIX: WhatsApp para el de afuera también (es más seguro que el mail)
            u_pp = "https://wa.me"
            st.markdown(f'<a href="{u_pp}" target="_blank" class="btn-paypal">🔵 PAY WITH PAYPAL (DIRECT)</a>', unsafe_allow_html=True)
            st.write("---")
        else:
            st.write("Suscripción: **$2.000.000 ARS**")
            st.markdown(f'<a href="https://wa.me" class="btn-mp">💳 MERCADO PAGO / CUENTA DNI</a>', unsafe_allow_html=True)
        
        emp_raw = st.text_input("FIRMA / COMPANY:").strip().upper()
        pw_in = st.text_input("MASTER KEY:", type="password")
        if st.button("🔓 UNLOCK VAULT"):
            if pw_in == "LEGACY2026" and emp_raw in VIP:
                st.session_state.emp_final = emp_raw
                st.session_state.auth = True; st.rerun()
            else: st.error("DENEGADO / DENIED")
    st.stop()

# --- 4. INTERIOR TOTAL ---
emp = st.session_state.emp_final
st.title(f"🏛️ TERMINAL: {emp}")
st.metric("REAL ESTATE", "$85,000,000")
st.subheader("🧬 SCANNER")
if st.button("🧬 SCAN"):
    with st.spinner("..."): time.sleep(1)
    st.success("VALUACIÓN: $42,500,000 USD")

if st.sidebar.button("🔒 LOGOUT"):
    st.session_state.auth = False; st.rerun()
