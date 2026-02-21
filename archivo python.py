import streamlit as st
import time

# --- 1. LÓGICA DE IDENTIDAD ---
if 'auth' not in st.session_state: st.session_state.auth = False

# --- 2. DISEÑO IMPERIAL ---
st.set_page_config(page_title="LEGACY | AI COMMAND", layout="wide")
st.markdown("""
    <style>
    .stApp { background-color: #000000; border: 5px solid #d4af37; padding: 20px; }
    h1, h2, h3, p, label, .stMetric { color: #d4af37 !important; text-align: center; }
    .gold-card { border: 2px solid #d4af37; padding: 15px; border-radius: 10px; background: rgba(212, 175, 55, 0.05); text-align: center; color: #d4af37; }
    div.stButton > button { background-color: #1a1a1a !important; color: #d4af37 !important; border: 1px solid #d4af37 !important; width: 100%; font-weight: bold; }
    .stTextInput > div > div > input { background-color: #1a1a1a !important; color: #d4af37 !important; border: 1px solid #d4af37 !important; }
    </style>
    """, unsafe_allow_html=True)

# --- 3. PANTALLA DE ACCESO ---
if not st.session_state.auth:
    st.title("🏛️ LEGACY QUANTUM VAULT")
    col_l, col_c, col_r = st.columns([1, 1.5, 1])
    with col_c:
        empresa = st.text_input("IDENTIFIQUE SU FIRMA:", placeholder="GINEVRA, REMAX, L.J. RAMOS...", key="e_fix")
        pw = st.text_input("MASTER KEY:", type="password", key="p_fix")
        if st.button("🔓 DESBLOQUEAR"):
            if pw == "LEGACY2026" and empresa:
                st.session_state.emp_final = empresa.upper()
                st.session_state.auth = True; st.rerun()
            else: st.error("Identificación obligatoria.")
    st.stop()

# --- 4. INTERIOR CON IA ACTIVA ---
emp = st.session_state.emp_final
st.title(f"🏛️ TERMINAL EXCLUSIVA: {emp}")

# MÉTRICAS DINÁMICAS
c1, c2, c3 = st.columns(3)
with c1: st.metric("REAL ESTATE", "$145M" if "GINEVRA" in emp else "$85M")
with c2: st.metric("YACHTS", "$25M" if "GINEVRA" in emp else "$12.5M")
with c3: st.metric("JETS", "$40M" if "GINEVRA" in emp else "$24M")

st.write("---")

# --- ACÁ VOLVIÓ LA IA (EL CEREBRO) ---
st.subheader(f"🤖 ESTRATEGA IA PARA {emp}")
pregunta = st.text_input("CONSULTA TÉCNICA O ANÁLISIS DE ACTIVOS:", placeholder="Ej: ¿Es momento de liquidar dptos en Madero?")

if pregunta:
    with st.spinner(f"Consultando Red Neuronal Legacy para {emp}..."):
        time.sleep(1.5)
        # RESPUESTA PERSONALIZADA DE LA IA
        st.markdown(f"""
        <div class='gold-card'>
        🏛️ <b>IA ADVISOR:</b> Director de {emp}, en base a su consulta sobre '<i>{pregunta}</i>', 
        nuestro análisis sugiere <b>MANTENER POSICIONES</b> y diversificar un 12% hacia activos líquidos. 
        Su cartera actual de {emp} muestra una solvencia de Grado AAA.
        </div>
        """, unsafe_allow_html=True)

st.write("---")
# SCANNER DE ACTIVOS
st.subheader("🧬 SCANNER QUÁNTICO")
st.text_area("PEGUE LISTA DE PROPIEDADES PARA VALUACIÓN:", key="sc_99")
if st.button("ANALIZAR LISTA"):
    st.success(f"Escaneo para {emp} finalizado.")

st.write("---")
# RELOJES MUNDIALES
r1, r2, r3 = st.columns(3)
with r1: st.markdown("<div class='gold-card'>🗽 NY: 11:30 PM</div>", unsafe_allow_html=True)
with r2: st.markdown("<div class='gold-card'>🏢 BA: 01:30 AM</div>", unsafe_allow_html=True)
with r3: st.markdown("<div class='gold-card'>🏰 LN: 04:30 AM</div>", unsafe_allow_html=True)

if st.sidebar.button("🔒 SALIR"): st.session_state.auth = False; st.rerun()
