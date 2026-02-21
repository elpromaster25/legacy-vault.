import streamlit as st
import time

# --- 1. SEGURIDAD ---
VIP = ["EMAAR", "GINEVRA", "REMAX", "THE AGENCY", "CARSO", "LEGACY", "DYLAN", "ADMIN", "SOTHEBYS", "HINES"]
if 'auth' not in st.session_state: st.session_state.auth = False

# --- 2. DISEÑO IMPERIAL (CONTRASTE MÁXIMO) ---
st.set_page_config(page_title="LEGACY GOLD VAULT", layout="wide")
st.markdown("""
    <style>
    .stApp { background-color: #000; border: 5px solid #d4af37; padding: 20px; }
    h1, h2, h3, p, label, .stMetric { color: #d4af37 !important; text-align: center !important; }
    .gold-card { border: 1px solid #d4af37; padding: 20px; border-radius: 15px; background: rgba(212, 175, 55, 0.05); text-align: center; margin-bottom: 15px; }
    
    /* BOTONES DE PAGO CON TEXTO BLANCO PARA QUE SE VEAN */
    .btn-paypal { background-color: #0070ba; color: #ffffff !important; padding: 14px; border-radius: 10px; font-weight: bold; text-decoration: none; display: block; text-align: center; margin-bottom: 10px; border: 1px solid #ffffff; }
    .btn-mp { background-color: #009ee3; color: #ffffff !important; padding: 14px; border-radius: 10px; font-weight: bold; text-decoration: none; display: block; text-align: center; margin-bottom: 10px; border: 1px solid #ffffff; }
    .btn-dni { background-color: #004d40; color: #ffffff !important; padding: 14px; border-radius: 10px; font-weight: bold; text-decoration: none; display: block; text-align: center; margin-bottom: 10px; border: 1px solid #ffffff; }
    .btn-gold { background-color: #d4af37; color: #000000 !important; padding: 14px; border-radius: 10px; font-weight: bold; text-decoration: none; display: block; text-align: center; margin-bottom: 10px; }

    div.stButton > button { background-color: #1a1a1a !important; color: #d4af37 !important; border: 1px solid #d4af37 !important; width: 100%; font-weight: bold; height: 3.5em; }
    </style>
    """, unsafe_allow_html=True)

# --- 3. PANTALLA DE ENTRADA ---
if not st.session_state.auth:
    st.title("🏛️ LEGACY QUANTUM VAULT")
    region = st.selectbox("🌐 SELECT REGION / ELIJA REGIÓN:", ["USA / GLOBAL", "ARGENTINA"])
    
    _, col_c, _ = st.columns([1, 1.5, 1])
    with col_c:
        st.markdown("<div class='gold-card'>🔒 NODO PRIVADO AUTORIZADO</div>", unsafe_allow_html=True)
        
        if region == "USA / GLOBAL":
            st.write("Subscription: **$12,000 USD**")
            # BOTONES USA
            st.markdown(f'<a href="mailto:dylanelpromaster25@://gmail.com" class="btn-paypal">🔵 PAY WITH PAYPAL (USD)</a>', unsafe_allow_html=True)
            st.markdown(f'<a href="mailto:dylanelpromaster25@://gmail.com" class="btn-gold">📩 REQUEST VIP ACCESS (EMAIL)</a>', unsafe_allow_html=True)
        else:
            st.write("Suscripción: **$2.000.000 ARS**")
            # BOTONES ARGENTINA CON TEXTO BLANCO
            st.markdown(f'<a href="https://wa.me" class="btn-mp">💳 PAGAR CON MERCADO PAGO</a>', unsafe_allow_html=True)
            st.markdown(f'<a href="https://wa.me" class="btn-dni">🏦 PAGAR CON CUENTA DNI</a>', unsafe_allow_html=True)

        st.write("---")
        emp_raw = st.text_input("FIRMA / COMPANY:").strip().upper()
        pw_in = st.text_input("MASTER KEY:", type="password")
        if st.button("🔓 UNLOCK VAULT"):
            if pw_in == "LEGACY2026" and emp_raw in VIP:
                st.session_state.emp_final = emp_raw
                st.session_state.auth = True; st.rerun()
            else: st.error("ACCESO DENEGADO / ACCESS DENIED")
    st.stop()

# --- 4. INTERIOR ---
st.title(f"🏛️ TERMINAL: {st.session_state.emp_final}")
st.metric("REAL ESTATE ASSETS", "$85,000,000")
st.subheader("🧬 SCANNER")
act = st.text_area("LISTA DE ACTIVOS:")
if st.button("🧬 SCAN"):
    with st.spinner("Escaneando..."):
        time.sleep(1); st.success("VALUACIÓN: $42,500,000 USD")

if st.sidebar.button("🔒 EXIT"):
    st.session_state.auth = False; st.rerun()
