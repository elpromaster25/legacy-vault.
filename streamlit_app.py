import streamlit as st
import time

# --- 1. WHITELIST REAL (Los únicos autorizados) ---
VIP = ["EMAAR", "DAMAC", "NEOM", "GINEVRA", "REMAX", "SOTHEBYS", "THE AGENCY", "HINES", "JLL", "CARSO", "BARNES", "FEAU", "ZINGRAF", "GARCIN", "JUNOT", "KRETZ", "KNIGHT FRANK", "SAVILLS", "CBRE", "COLLIERS", "LEGACY", "DYLAN", "ADMIN", "TZIPINE"]

# MEMORIA BLINDADA
if 'auth' not in st.session_state: st.session_state.auth = False
if 'reg' not in st.session_state: st.session_state.reg = []
if 'es_dylan' not in st.session_state: st.session_state.es_dylan = False

# --- 2. DISEÑO SIN SIDEBAR (NO MÁS FLECHITA) ---
st.set_page_config(page_title="LEGACY VAULT", layout="wide", initial_sidebar_state="collapsed")
st.markdown("""
    <style>
    /* ELIMINA LA FLECHA Y EL MENU LATERAL POR COMPLETO */
    [data-testid="stSidebar"], [data-testid="stSidebarNav"], .st-emotion-cache-16idsys { display: none !important; }
    .stApp { background-color: #000; border: 2px solid #d4af37; }
    h1, h2, h3, p, label, .stMetric { color: #d4af37 !important; text-align: center !important; }
    .gold-card { border: 1px solid #d4af37; padding: 15px; border-radius: 10px; background: rgba(212, 175, 55, 0.05); text-align: center; margin-bottom: 10px; }
    .btn-pay { background-color: #1a1a1a; color: #fff !important; padding: 12px; border-radius: 8px; font-weight: bold; text-decoration: none; display: block; text-align: center; margin-bottom: 8px; border: 1px solid #d4af37; }
    div.stButton > button { background-color: #d4af37 !important; color: #000 !important; width: 100%; font-weight: bold; }
    </style>
    """, unsafe_allow_html=True)

# --- 3. LOGIN CON DOBLE CANDADO ---
if not st.session_state.auth:
    st.title("🏛️ LEGACY QUANTUM VAULT")
    reg_sel = st.selectbox("🌐 REGION:", ["USA / GLOBAL", "ARGENTINA"])
    _, col_c, _ = st.columns([1, 1.5, 1])
    with col_c:
        st.markdown("<div class='gold-card'>🔒 NODO PRIVADO</div>", unsafe_allow_html=True)
        if reg_sel == "USA / GLOBAL":
            st.markdown(f'<a href="mailto:dylanelpromaster25@://gmail.com" class="btn-pay">🔵 PAY WITH PAYPAL (EMAIL)</a>', unsafe_allow_html=True)
        else:
            st.markdown(f'<a href="mailto:dylanelpromaster25@://gmail.com" class="btn-pay">💳 PAGAR CON MERCADO PAGO (EMAIL)</a>', unsafe_allow_html=True)
        
        st.write("---")
        emp = st.text_input("COMPANY:").strip().upper()
        pw = st.text_input("KEY:", type="password")
        
        if st.button("🔓 UNLOCK"):
            # ENTRADA MAESTRA (DYLAN)
            if emp == "DYLAN777" and pw == "LEGACY2026":
                st.session_state.es_dylan = True
                st.session_state.emp_final = "FOUNDER CONTROL"
                st.session_state.auth = True; st.rerun()
            # ENTRADA CLIENTES (VALIDA EMPRESA Y CLAVE)
            elif pw == "LEGACY2026" and emp in VIP:
                st.session_state.emp_final = emp
                st.session_state.reg.append(f"🟢 {emp} - {time.strftime('%H:%M')}")
                st.session_state.auth = True; st.rerun()
            elif emp != "":
                st.error("🚫 ACCESO DENEGADO. FIRMA NO AUTORIZADA.")
                st.session_state.reg.append(f"🔴 ERROR: {emp} - {time.strftime('%H:%M')}")
    st.stop()

# --- 4. INTERIOR DEL IMPERIO ---
st.title(f"🏛️ TERMINAL: {st.session_state.emp_final}")
c1, c2, c3 = st.columns(3)
with c1: st.metric("REAL ESTATE", "$85M")
with c2: st.metric("YACHTS", "$12.5M")
with c3: st.metric("PRIVATE JETS", "$24M")

st.write("---")
# IA ADVISOR (RESTABLECIDA)
st.subheader("🤖 IA STRATEGIC ADVISOR")
p = st.text_input("CONSULTA TÉCNICA:")
if p:
    with st.spinner("Analizando..."):
        time.sleep(1); st.success(f"Análisis completado para {st.session_state.emp_final}. Liquidez Óptima.")

st.write("---")
# SCANNER
st.subheader("🧬 QUANTUM ASSET SCANNER")
if st.button("🧬 INICIAR ESCANEO"):
    with st.spinner("..."):
        time.sleep(1.5); st.markdown(f"<div class='gold-card'><h2>VALUACIÓN: $42,500,000 USD</h2></div>", unsafe_allow_html=True)

# --- 5. EL RADAR FANTASMA (SOLO PARA DYLAN) ---
if st.session_state.es_dylan:
    st.write("---")
    with st.expander("🕵️‍♂️ RADAR DE IMPACTOS (SECRET FOUNDER MODE)"):
        for r in st.session_state.reg: st.info(r)

if st.button("🔒 LOGOUT"):
    st.session_state.auth = False
    st.session_state.es_dylan = False
    st.rerun()
