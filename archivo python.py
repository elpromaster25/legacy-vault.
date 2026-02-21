import streamlit as st
import time

# --- 1. CONFIGURACIÓN LIGERA ---
if 'auth' not in st.session_state: st.session_state.auth = False
if 'solicitudes' not in st.session_state: st.session_state.solicitudes = []

# --- 2. DISEÑO IMPERIAL LIVIANO (VELOCIDAD MÁXIMA) ---
st.set_page_config(page_title="LEGACY | FAST VAULT", layout="wide")
st.markdown("""
    <style>
    .stApp { background-color: #000000; border: 4px solid #d4af37; }
    h1, h2, h3 { color: #d4af37 !important; text-align: center; }
    .gold-card { border: 1px solid #d4af37; padding: 15px; border-radius: 10px; background: rgba(212, 175, 55, 0.05); text-align: center; color: #d4af37; }
    div.stButton > button { background-color: #1a1a1a; color: #d4af37; border: 1px solid #d4af37; width: 100%; font-weight: bold; }
    .warning-text { color: #ff4b4b; font-size: 0.8rem; text-align: center; margin-top: -15px; font-weight: bold; }
    </style>
    """, unsafe_allow_html=True)

# --- 3. PANTALLA DE ENTRADA OPTIMIZADA ---
if not st.session_state.auth:
    st.title("🏛️ LEGACY QUANTUM VAULT")
    col_iz, col_ce, col_de = st.columns([1, 1.5, 1])
    with col_ce:
        st.markdown("<div class='gold-card'>💎 IDENTIFICACIÓN CORPORATIVA</div>", unsafe_allow_html=True)
        # NOMBRE DE LA EMPRESA
        emp_name = st.text_input("FIRMA / COMPANY:", placeholder="Ej: REMAX PREMIUM", key="emp_99")
        
        st.write("")
        # CONTRASEÑA
        pw = st.text_input("MASTER KEY:", type="password", key="pw_99")
        
        # EL AVISO QUE PEDISTE (EN CHIQUITO)
        st.markdown("<p class='warning-text'>⚠️ DEBE INGRESAR EL NOMBRE DE SU EMPRESA PARA HABILITAR EL ACCESO</p>", unsafe_allow_html=True)
        
        if st.button("🔓 DESBLOQUEAR"):
            if pw == "LEGACY2026" and emp_name:
                st.session_state.empresa_actual = emp_name
                st.session_state.solicitudes.append(f"{emp_name} - {time.strftime('%H:%M')}")
                st.session_state.auth = True
                st.rerun()
            elif not emp_name:
                st.error("Identificación de firma obligatoria.")
            else:
                st.error("Llave incorrecta.")
    st.stop()

# --- 4. INTERIOR VELOZ ---
emp = st.session_state.empresa_actual
st.markdown(f"<h2>🏛️ TERMINAL ACTIVA: {emp.upper()}</h2>", unsafe_allow_html=True)

# ACTIVOS RESUMIDOS
c1, c2, c3 = st.columns(3)
with c1: st.markdown("<div class='gold-card'>🏰 REAL ESTATE<br>$85M</div>", unsafe_allow_html=True)
with c2: st.markdown("<div class='gold-card'>🛥️ YATES<br>$12.5M</div>", unsafe_allow_html=True)
with c3: st.markdown("<div class='gold-card'>🛩️ JETS<br>$24M</div>", unsafe_allow_html=True)

st.write("---")
st.subheader("🤖 IA ADVISOR")
st.info(f"Análisis de activos de **{emp}** completado. Estado: **SOLVENTE**.")

# MODO ADMIN (PARA VOS)
if st.sidebar.checkbox("🔓 ADMIN"):
    if st.sidebar.text_input("PIN:", type="password") == "DYLAN777":
        st.sidebar.write("📬 ÚLTIMOS ACCESOS:")
        for s in st.session_state.solicitudes: st.sidebar.write(f"🏢 {s}")

if st.sidebar.button("🔒 SALIR"): st.session_state.auth = False; st.rerun()
