import streamlit as st
import time

# --- 1. CONFIGURACIÓN ---
if 'auth' not in st.session_state: st.session_state.auth = False

# --- 2. DISEÑO IMPERIAL (DORADO Y NEGRO TOTAL) ---
st.set_page_config(page_title="LEGACY GOLD EMPIRE", layout="wide")
st.markdown("""
    <style>
    .stApp { background-color: #000000; border: 5px solid #d4af37; padding: 20px; }
    h1, h2, h3, h4, p, label, .stMetric { color: #d4af37 !important; text-align: center; font-family: 'serif'; }
    .gold-card { border: 2px solid #d4af37; padding: 20px; border-radius: 15px; background: rgba(212, 175, 55, 0.1); text-align: center; color: #d4af37; }
    .ticker { background: #1a1a1a; color: #d4af37; padding: 10px; border-bottom: 2px solid #d4af37; font-weight: bold; text-align: center; font-size: 0.8rem; }
    div.stButton > button { background-color: #1a1a1a !important; color: #d4af37 !important; border: 1px solid #d4af37 !important; width: 100%; font-weight: bold; height: 3em; }
    .stTextInput > div > div > input { background-color: #1a1a1a !important; color: #d4af37 !important; border: 1px solid #d4af37 !important; }
    </style>
    """, unsafe_allow_html=True)

# --- 3. TICKER DE MERCADO VIVO ---
st.markdown("<div class='ticker'>🏦 LIVE: USDT/ARS: 1.515 | BTC/USD: 96.850 | PROTOCOLO AES-256: ACTIVO</div>", unsafe_allow_html=True)

# --- 4. PANTALLA DE ACCESO ---
if not st.session_state.auth:
    st.title("🏛️ LEGACY QUANTUM VAULT")
    col_l, col_c, col_r = st.columns([1, 1.5, 1])
    with col_c:
        v_sel = st.selectbox("📂 SELECT VAULT:", ["ARGENTINA", "USA"], key="v_sel_99")
        st.markdown("<div class='gold-card'>💎 ADQUIRIR TERMINAL CORPORATIVA</div>", unsafe_allow_html=True)
        st.write("---")
        emp = st.text_input("FIRMA / COMPANY:", key="e_sel_99")
        pw = st.text_input("MASTER KEY:", type="password", key="p_sel_99")
        if st.button("🔓 DESBLOQUEAR BÓVEDA"):
            if pw == "LEGACY2026" and emp:
                st.session_state.emp_final = emp
                st.session_state.auth = True; st.rerun()
            else: st.error("Identificación obligatoria.")
    st.stop()

# --- 5. INTERIOR (EL IMPERIO) ---
st.title(f"🏛️ TERMINAL: {st.session_state.emp_final.upper()}")

# MÉTRICAS
c1, c2, c3 = st.columns(3)
with c1: st.metric("REAL ESTATE", "$85,000,000")
with c2: st.metric("YACHTS", "$12,500,000")
with c3: st.metric("JETS", "$24,000,000")

st.write("---")
# IA SCANNER
st.subheader("🤖 ESTRATEGA IA & SCANNER")
lista = st.text_area("LISTA DE ACTIVOS (Dptos, Campos, Autos):", key="sc_99")
if st.button("🧬 ANALIZAR PATRIMONIO"):
    with st.spinner("Analizando..."):
        time.sleep(1)
        st.success(f"Análisis para {st.session_state.emp_final} completado: Patrimonio Sólido.")

st.write("---")
# RELOJES MUNDIALES
r1, r2, r3 = st.columns(3)
with r1: st.markdown("<div class='gold-card'>🗽 NY: 11:40 PM</div>", unsafe_allow_html=True)
with r2: st.markdown("<div class='gold-card'>🏢 BA: 01:40 AM</div>", unsafe_allow_html=True)
with r3: st.markdown("<div class='gold-card'>🏰 LN: 04:40 AM</div>", unsafe_allow_html=True)

st.write("---")
# OPCIÓN PERSONALIZADA (TU IDEA)
st.markdown("<div class='gold-card'><b>¿DESEA UNA TERMINAL PERSONALIZADA?</b><br>Desarrollamos su Bóveda Privada. Envíe comprobante de pago vía MP o PayPal.</div>", unsafe_allow_html=True)
st.markdown(f'<a href="mailto:dylanelpromaster25@://gmail.com{st.session_state.emp_final}"><button style="width:100%; height:40px; background:#d4af37; color:black; font-weight:bold; border:none; border-radius:5px; cursor:pointer; margin-top:10px;">📩 SOLICITAR DESARROLLO EXCLUSIVO</button></a>', unsafe_allow_html=True)

if st.sidebar.button("🔒 SALIR"): st.session_state.auth = False; st.rerun()
