import streamlit as st
import time

# --- 1. WHITELIST DE ELITE ---
VIP = ["EMAAR", "DAMAC", "NEOM", "GINEVRA", "REMAX", "SOTHEBYS", "THE AGENCY", "HINES", "JLL", "CARSO", "LEGACY", "DYLAN", "ADMIN", "TZIPINE"]

# MEMORIA DEL NODO
if 'auth' not in st.session_state: st.session_state.auth = False
if 'reg' not in st.session_state: st.session_state.reg = []
if 'is_admin' not in st.session_state: st.session_state.is_admin = False

# --- 2. DISEÑO IMPERIAL LIGHTSPEED ---
st.set_page_config(page_title="LEGACY VAULT", layout="wide")
st.markdown("""
    <style>
    .stApp { background-color: #000; border: 2px solid #d4af37; }
    h1, h2, h3, p, label, .stMetric { color: #d4af37 !important; text-align: center !important; }
    .gold-card { border: 1px solid #d4af37; padding: 15px; border-radius: 10px; background: rgba(212, 175, 55, 0.03); text-align: center; margin-bottom: 10px; }
    .btn-pay { background-color: #1a1a1a; color: #fff !important; padding: 12px; border-radius: 8px; font-weight: bold; text-decoration: none; display: block; text-align: center; margin-bottom: 8px; border: 1px solid #d4af37; }
    div.stButton > button { background-color: #d4af37 !important; color: #000 !important; width: 100%; font-weight: bold; border-radius: 5px; }
    </style>
    """, unsafe_allow_html=True)

# --- 3. LOGIN BLINDADO (LA PUERTA) ---
if not st.session_state.auth:
    st.title("🏛️ LEGACY QUANTUM VAULT")
    reg = st.selectbox("🌐 REGION:", ["USA / GLOBAL", "ARGENTINA"])
    
    _, col_c, _ = st.columns([1, 1.5, 1])
    with col_c:
        st.markdown("<div class='gold-card'>🔒 NODO PRIVADO</div>", unsafe_allow_html=True)
        
        # BOTONES DE EMAIL (DIRECTOS)
        if reg == "USA / GLOBAL":
            m_pp = "mailto:dylanelpromaster25@://gmail.com"
            st.markdown(f'<a href="{m_pp}" class="btn-pay">🔵 REQUEST PAYPAL LINK (EMAIL)</a>', unsafe_allow_html=True)
        else:
            m_mp = "mailto:dylanelpromaster25@://gmail.com"
            st.markdown(f'<a href="{m_mp}" class="btn-pay">💳 PAGAR CON MERCADO PAGO (EMAIL)</a>', unsafe_allow_html=True)

        st.write("---")
        emp = st.text_input("COMPANY:").strip().upper()
        pw = st.text_input("KEY:", type="password")
        
        if st.button("🔓 UNLOCK"):
            # 🕵️‍♂️ TU ENTRADA SECRETA DE ADMIN (Invisble para el resto)
            if emp == "DYLAN777" and pw == "LEGACY2026":
                st.session_state.is_admin = True
                st.session_state.emp_final = "FOUNDER CONTROL"
                st.session_state.auth = True; st.rerun()
            # Entrada de Clientes
            elif pw == "LEGACY2026" and emp in VIP:
                st.session_state.emp_final = emp
                st.session_state.reg.append(f"🟢 {emp} - {time.strftime('%H:%M')}")
                st.session_state.auth = True; st.rerun()
            elif emp != "":
                st.error(f"🚫 FIRMA '{emp}' NO RECONOCIDA.")
                st.warning("Support: dylanelpromaster25@gmail.com")
                st.session_state.reg.append(f"🔴 ERROR: {emp} - {time.strftime('%H:%M')}")
    st.stop()

# --- 4. INTERIOR ---
st.title(f"🏛️ TERMINAL: {st.session_state.emp_final}")

# SI SOS VOS, APARECE EL RADAR. SI ES UN CLIENTE, NO VE NADA.
if st.session_state.is_admin:
    with st.expander("🕵️‍♂️ RADAR DE IMPACTOS (MODO FOUNDER)"):
        for r in st.session_state.reg: st.info(r)

c1, c2, c3 = st.columns(3)
with c1: st.metric("REAL ESTATE", "$85M")
with c2: st.metric("YACHTS", "$12.5M")
with c3: st.metric("PRIVATE JETS", "$24M")

st.write("---")
st.subheader("🧬 SCANNER")
if st.button("🧬 SCAN"):
    with st.spinner("..."): time.sleep(1); st.success("VALUACIÓN: $42,500,000 USD")

if st.sidebar.button("🔒 LOGOUT"):
    st.session_state.auth = False
    st.session_state.is_admin = False
    st.rerun()
