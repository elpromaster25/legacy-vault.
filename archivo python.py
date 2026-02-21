import streamlit as st
import time

# --- 1. LÓGICA DE SESIÓN ---
if 'auth' not in st.session_state: st.session_state.auth = False

# --- 2. DISEÑO IMPERIAL ---
st.set_page_config(page_title="LEGACY GOLD VAULT", layout="wide")
st.markdown("""
    <style>
    .stApp { background-color: #000000; border: 5px solid #d4af37; padding: 20px; }
    h1, h2, h3, p, label { color: #d4af37 !important; text-align: center !important; }
    [data-testid="stMetric"] { text-align: center !important; display: flex; flex-direction: column; align-items: center; }
    [data-testid="stMetricValue"] { color: #d4af37 !important; font-size: 2.8rem !important; }
    .gold-card { border: 1px solid #d4af37; padding: 20px; border-radius: 15px; background: rgba(212, 175, 55, 0.05); text-align: center; color: #d4af37; }
    div.stButton > button { background-color: #1a1a1a !important; color: #d4af37 !important; border: 1px solid #d4af37 !important; width: 100%; font-weight: bold; height: 3em; }
    .stTextArea > div > div > textarea { background-color: #1a1a1a !important; color: #d4af37 !important; border: 1px solid #d4af37 !important; text-align: center; }
    </style>
    """, unsafe_allow_html=True)

# --- 3. ACCESO ---
if not st.session_state.auth:
    st.title("🏛️ LEGACY QUANTUM VAULT")
    _, col_ce, _ = st.columns([1, 1.5, 1])
    with col_ce:
        emp = st.text_input("IDENTIFIQUE SU FIRMA:", key="e_final")
        pw = st.text_input("MASTER KEY:", type="password", key="p_final")
        if st.button("🔓 DESBLOQUEAR"):
            if pw == "LEGACY2026" and emp:
                st.session_state.emp_final = emp.upper()
                st.session_state.auth = True; st.rerun()
            else: st.error("Datos requeridos.")
    st.stop()

# --- 4. INTERIOR ---
emp = st.session_state.emp_final
st.title(f"🏛️ TERMINAL EXCLUSIVA: {emp}")
st.write("---")

# MÉTRICAS
c1, c2, c3 = st.columns(3)
with c1: st.metric("REAL ESTATE", "$145M" if "GINEVRA" in emp else "$85M")
with c2: st.metric("YACHTS", "$25M" if "GINEVRA" in emp else "$12.5M")
with c3: st.metric("JETS", "$40M" if "GINEVRA" in emp else "$24M")

st.write("---")

# IA ESTRATÉGICA
st.subheader(f"🤖 ESTRATEGA IA PARA {emp}")
_, col_ia, _ = st.columns([0.5, 2, 0.5])
with col_ia:
    pregunta = st.text_input("CONSULTA TÉCNICA:", key="q_ia")
    if pregunta:
        with st.spinner("Analizando..."):
            time.sleep(1)
            st.markdown(f"<div class='gold-card'>🏛️ <b>IA ADVISOR:</b> Análisis de '{pregunta}' completado para {emp}. Estado: SOLVENTE.</div>", unsafe_allow_html=True)

st.write("---")

# SCANNER QUÁNTICO (REPARADO)
st.subheader("🧬 SCANNER DE ACTIVOS PATRIMONIALES")
_, col_sc, _ = st.columns([0.5, 2, 0.5])
with col_sc:
    # Capturamos el texto en una variable
    activos_input = st.text_area("LISTA DE PROPIEDADES, AUTOS O YATES:", placeholder="Ej: 2 Ferraris, 1 Mansión en Nordelta...", key="sc_input_99")
    
    # El botón ahora dispara una acción visible
    if st.button("🧬 INICIAR ESCANEO QUÁNTICO"):
        if activos_input:
            with st.status("Escaneando activos de lujo...", expanded=True) as status:
                st.write("🔍 Identificando modelos y tasaciones...")
                time.sleep(1.2)
                st.write("📈 Cruzando datos con mercados internacionales...")
                time.sleep(1.2)
                status.update(label="Escaneo Finalizado ✅", state="complete")
            
            # RESULTADO IMPACTANTE
            st.markdown(f"""
            <div class='gold-card'>
            <h3>💎 VALUACIÓN DETECTADA</h3>
            <p>Se han analizado los activos: <b>{activos_input}</b></p>
            <h2 style='color:#d4af37;'>$42,500,000 USD</h2>
            <p>Sugerencia de {emp}: Asegurar activos vía Mesa OTC.</p>
            </div>
            """, unsafe_allow_html=True)
        else:
            st.warning("⚠️ Por favor, ingrese los activos que desea escanear.")

st.write("---")

# RELOJES MUNDIALES
r1, r2, r3 = st.columns(3)
with r1: st.markdown("<div class='gold-card'>🗽 NY: 11:35 PM</div>", unsafe_allow_html=True)
with r2: st.markdown("<div class='gold-card'>🏢 BA: 01:35 AM</div>", unsafe_allow_html=True)
with r3: st.markdown("<div class='gold-card'>🏰 LN: 04:35 AM</div>", unsafe_allow_html=True)

if st.sidebar.button("🔒 SALIR"): st.session_state.auth = False; st.rerun()
