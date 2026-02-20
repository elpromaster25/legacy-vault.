import streamlit as st
import pandas as pd
import time

# --- 1. LÓGICA DE SESIÓN Y DEMO ---
if 'autenticado' not in st.session_state:
    st.session_state.autenticado = False
if 'inicio_demo' not in st.session_state:
    st.session_state.inicio_demo = None
if 'demo_terminada' not in st.session_state:
    st.session_state.demo_terminada = False
if 'mensajes' not in st.session_state:
    st.session_state.mensajes = []

# --- 2. PANTALLA DE ENTRADA / LOGIN / DEMO ---
if not st.session_state.autenticado and not st.session_state.inicio_demo:
    st.set_page_config(page_title="LEGACY | ACCESO", page_icon="🔐", layout="wide")
    st.markdown("<style>.stApp { background-color: #000000; } h1, h2, h3 { color: #d4af37; text-align: center; font-family: 'serif'; }</style>", unsafe_allow_html=True)
    st.title("🏛️ LEGACY QUANTUM VAULT")
    
    col_l, col_c, col_r = st.columns([1, 1.5, 1])
    with col_c:
        st.subheader("Seleccione su vía de acceso:")
        if st.button("🔑 INGRESAR CON LLAVE MAESTRA"):
            st.session_state.autenticado = "form_login"
            st.rerun()
        
        st.write("---")
        if st.button("🚀 INICIAR DEMO GRATUITA (5 MIN)"):
            st.session_state.inicio_demo = time.time()
            st.rerun()
    st.stop()

# --- 3. FORMULARIO DE LOGIN ---
if st.session_state.autenticado == "form_login":
    st.set_page_config(page_title="LOGIN", page_icon="🔐")
    st.markdown("<style>.stApp { background-color: #000000; } h2 { color: #d4af37; text-align: center; }</style>", unsafe_allow_html=True)
    st.subheader("🔐 INGRESE SU LLAVE")
    pass_input = st.text_input("PASSWORD:", type="password")
    if st.button("DESBLOQUEAR"):
        if pass_input == "LEGACY2026":
            st.session_state.autenticado = True
            st.session_state.inicio_demo = None
            st.rerun()
        else:
            st.error("LLAVE INVÁLIDA")
    st.stop()

# --- 4. CONTROL DE TIEMPO (DEMO) ---
if st.session_state.inicio_demo and not st.session_state.autenticado:
    transcurrido = time.time() - st.session_state.inicio_demo
    if transcurrido > 300: # 5 minutos
        st.session_state.demo_terminada = True

# --- 5. MURO DE PAGO (PAYWALL) ---
if st.session_state.demo_terminada and not st.session_state.autenticado:
    st.set_page_config(page_title="TIEMPO EXPIRADO", page_icon="🚫")
    st.markdown("<style>.stApp { background-color: #000000; } h1, h3 { color: #d4af37; text-align: center; border: 2px solid #d4af37; padding: 10px; }</style>", unsafe_allow_html=True)
    st.title("⌛ SU TIEMPO DE DEMO HA EXPIRADO")
    st.write("---")
    c1, c2 = st.columns(2)
    with c1: st.markdown("<h3>🇦🇷 ARGENTINA:<br>2 MILLONES ARS / MES</h3>", unsafe_allow_html=True)
    with col_r: st.markdown("<h3>🇺🇸 USA / INT:<br>12 THOUSAND USD / MONTH</h3>", unsafe_allow_html=True)
    st.write("---")
    if st.button("⬅️ VOLVER AL INICIO"):
        st.session_state.inicio_demo = None
        st.session_state.demo_terminada = False
        st.rerun()
    st.stop()

# --- 6. INTERFAZ PRINCIPAL (EL PRODUCTO) ---
st.set_page_config(page_title="LEGACY COMMAND", layout="wide")
st.markdown("<style>.stApp { background-color: #050505; border: 4px solid #d4af37; padding: 20px; } h1, h2, h3 { color: #d4af37 !important; text-align: center; } [data-testid='stMetricValue'] { color: #d4af37 !important; font-size: 2.2rem !important; }</style>", unsafe_allow_html=True)

# SIDEBAR
st.sidebar.title("🛂 DASHBOARD")
es_admin = st.sidebar.checkbox("🔓 MODO ADMIN (DYLAN)")
idioma = st.sidebar.selectbox("Region:", ["🇦🇷 Argentina", "🇺🇸 USA"]) if not es_admin else "Admin"

if idioma == "Admin":
    st.title("👨‍💻 PANEL DE DYLAN")
    if st.session_state.mensajes: st.table(pd.DataFrame(st.session_state.mensajes))
    else: st.write("Aún no hay mensajes.")
else:
    if st.session_state.inicio_demo:
        st.warning(f"⚠️ MODO DEMO ACTIVO. Tiempo restante: {int(300 - (time.time() - st.session_state.inicio_demo))} seg.")
    st.title("🏛️ COMMAND CENTER LEGACY")
    
    # SIMULADOR
    años = st.slider("AÑOS / YEARS:", 1, 30, 10); ret = st.slider("RETORNO %:", 5, 50, 15)
    fut_usd = 12450000 * ((1 + (ret/100))**años)
    r1, r2 = st.columns(2)
    r1.metric("FORTUNA USD", f"${fut_usd:,.0f}"); r2.metric("FORTUNA ARS", f"${fut_usd * 1500:,.0f}")
    
    st.markdown("---")
    # GRÁFICOS (ARREGLADO CON NÚMEROS REALES)
    c1, c2 = st.columns(2)
    with c1:
        st.subheader("📊 DISTRIBUCIÓN")
        # Números de activos puestos para evitar error
        df_f = pd.DataFrame({"Activo": ["RE", "Stocks", "Crypto", "Art"], "Valor":})
        st.bar_chart(df_f.set_index("Activo"))
    with c2:
        st.subheader("🤖 IA ADVISOR")
        user_q = st.text_input("Consulta técnica:")
        if user_q: st.write("🏛️ **IA:** Dylan García, la orden estratégica es MANTENER POSICIONES.")

if st.sidebar.button("🔒 SALIR"):
    st.session_state.autenticado = False
    st.session_state.inicio_demo = None
    st.rerun()
