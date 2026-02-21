import streamlit as st
import pandas as pd
import time

# --- 1. BASE DE DATOS Y ESTADOS ---
if 'auth' not in st.session_state: st.session_state.auth = False
if 'solicitudes' not in st.session_state: st.session_state.solicitudes = []

# --- 2. DISEÑO IMPERIAL ---
st.set_page_config(page_title="LEGACY | CORPORATE", layout="wide")
st.markdown("""
    <style>
    .stApp { background-color: #000000; border: 6px solid #d4af37; padding: 25px; }
    h1, h2, h3 { color: #d4af37 !important; text-align: center; font-family: 'serif'; }
    .gold-card { border: 2px solid #d4af37; padding: 20px; border-radius: 15px; background: rgba(212, 175, 55, 0.1); text-align: center; color: #d4af37; }
    div.stButton > button { background-color: #1a1a1a; color: #d4af37; border: 2px solid #d4af37; width: 100%; height: 3em; font-weight: bold; }
    </style>
    """, unsafe_allow_html=True)

# --- 3. PANTALLA DE ENTRADA (EL RADAR) ---
if not st.session_state.auth:
    st.title("🏛️ LEGACY QUANTUM VAULT")
    col_iz, col_ce, col_de = st.columns([1, 1.5, 1])
    with col_ce:
        st.markdown("<div class='gold-card'>💎 IDENTIFICACIÓN CORPORATIVA REQUERIDA</div>", unsafe_allow_html=True)
        # ACÁ ESTÁ TU IDEA: EL NOMBRE DE LA EMPRESA
        empresa_name = st.text_input("NOMBRE DE SU FIRMA / COMPANY NAME:", placeholder="Ej: L.J. Ramos, Remax, Ginevra...")
        
        st.write("---")
        pw = st.text_input("MASTER KEY / LLAVE MAESTRA:", type="password")
        
        if st.button("🔓 DESBLOQUEAR BÓVEDA"):
            if pw == "LEGACY2026" and empresa_name:
                # GUARDAMOS EL NOMBRE PARA EL RADAR
                st.session_state.empresa_actual = empresa_name
                st.session_state.solicitudes.append({"Empresa": empresa_name, "Hora": time.strftime('%H:%M')})
                st.session_state.auth = True
                st.rerun()
            elif not empresa_name:
                st.warning("Por favor, identifique su firma para proceder.")
            else:
                st.error("DENEGADO")
    st.stop()

# --- 4. INTERIOR PERSONALIZADO ---
emp = st.session_state.empresa_actual
st.markdown(f"<h2 style='text-align: center;'>🏛️ BIENVENIDO DIRECTOR DE {emp.upper()}</h2>", unsafe_allow_html=True)

# SECCIÓN DE ACTIVOS DE LUJO (YATES, MANSIONES, ETC)
st.write("---")
st.subheader("🛥️ VALUACIÓN DE ACTIVOS CORPORATIVOS VIP")
c1, c2, c3 = st.columns(3)
with c1: st.markdown("<div class='gold-card'>🏰 MANSIONES / REAL ESTATE<br><b>$85,000,000 USD</b></div>", unsafe_allow_html=True)
with c2: st.markdown("<div class='gold-card'>🛥️ YATES & EMBARCACIONES<br><b>$12,500,000 USD</b></div>", unsafe_allow_html=True)
with c3: st.markdown("<div class='gold-card'>🛩️ FLOTA DE JETS PRIVADOS<br><b>$24,000,000 USD</b></div>", unsafe_allow_html=True)

st.write("---")
# IA ADVISOR HABLANDO CON EL NOMBRE DE LA EMPRESA
st.subheader("🤖 ESTRATEGA IA: ANÁLISIS CORPORATIVO")
st.write(f"🏛️ **IA:** Analizando activos de **{emp}**. Se detecta una alta concentración en Real Estate. Sugerimos liquidar vía nuestra Mesa OTC.")

# --- 5. MODO ADMIN (PARA VOS EN PLATANOS) ---
if st.sidebar.checkbox("🔓 MODO ESPÍA (DYLAN)"):
    if st.sidebar.text_input("CLAVE:", type="password") == "DYLAN777":
        st.sidebar.write("📬 EMPRESAS ACTIVAS EN LA BÓVEDA:")
        if st.session_state.solicitudes:
            st.sidebar.table(pd.DataFrame(st.session_state.solicitudes))

if st.sidebar.button("🔒 SALIR"): st.session_state.auth = False; st.rerun()
