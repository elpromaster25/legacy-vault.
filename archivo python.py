import streamlit as st
import pandas as pd
import time

# --- 1. SEGURIDAD DE ACCESO (EL SCANNER) ---
if 'autenticado' not in st.session_state:
    st.session_state.autenticado = False

if not st.session_state.autenticado:
    st.set_page_config(page_title="IDENTIFICACIÓN REQUERIDA", page_icon="🔐")
    st.markdown("<style>.stApp { background-color: #050505; } h1 { color: #d4af37; text-align: center; font-family: 'Garamond'; }</style>", unsafe_allow_html=True)
    st.title("🔐 ACCESO RESTRINGIDO: LEGACY QUANTUM")
    password = st.text_input("INGRESE LLAVE DE ENCRIPTACIÓN:", type="password")
    if st.button("DESBLOQUEAR TERMINAL"):
        if password == "LEGACY2026":
            # EFECTO SCANNER BIOMÉTRICO
            with st.status("Iniciando Protocolos de Seguridad...", expanded=True) as status:
                st.write("🧬 Escaneando Firma Digital Única...")
                time.sleep(1)
                st.write("🛰️ Verificando Localización Satelital...")
                time.sleep(1)
                st.write("🟢 Identidad Verificada: Dylan García.")
                status.update(label="Acceso Concedido", state="complete", expanded=False)
            st.session_state.autenticado = True
            st.rerun()
        else:
            st.error("ACCESO DENEGADO. INTENTO REPORTADO.")
    st.stop()

# --- 2. CONFIGURACIÓN DE ÉLITE ---
st.set_page_config(page_title="LEGACY COMMAND CENTER", page_icon="🏛️", layout="wide")
st.markdown("""
    <style>
    .stApp { background-color: #050505; }
    h1, h2, h3 { color: #d4af37 !important; font-family: 'Garamond', serif; text-align: center; }
    [data-testid="stMetricValue"] { color: #d4af37 !important; font-size: 2.8rem !important; }
    .stMarkdown p { color: #888; font-family: 'Courier New'; }
    div.stButton > button { background-color: #1a1a1a; color: #d4af37; border: 1px solid #d4af37; border-radius: 0px; width: 100%; }
    div.stButton > button:hover { background-color: #d4af37; color: black; }
    </style>
    """, unsafe_allow_html=True)

# --- 3. BARRA DE NOTICIAS ---
st.markdown("<marquee style='color: #d4af37; font-family: Courier New;'>● MERCADOS GLOBALES OPERANDO ● PROTECCIÓN PATRIMONIAL ACTIVA ● BITCOIN: BULLISH TREND ●</marquee>", unsafe_allow_html=True)

st.title("🏛️ LEGACY COMMAND CENTER")
st.markdown("<p style='text-align: center;'>CENTRAL DE INTELIGENCIA ESTRATÉGICA PARA ACTIVOS DE ALTO VALOR</p>", unsafe_allow_html=True)

# --- 4. MÉTRICAS DE SEGURIDAD Y MERCADO ---
t1, t2, t3, t4 = st.columns(4)
t1.metric("ESCUDO DE RED", "ACTIVO", "AES-256")
t2.metric("RIESGO SISTÉMICO", "BAJO", "SÓLIDO")
t3.metric("EQUITY TOTAL", "$12,450,000", "+2.4%")
t4.metric("BITCOIN", "$98,450", "+2.5%")

st.markdown("---")

# --- 5. BÓVEDA PRINCIPAL ---
c1, c2 = st.columns(2)
with c1:
    st.subheader("💰 RESUMEN DE ACTIVOS")
    st.info("ℹ️ Certificación: Sus activos están auditados bajo el estándar Legacy-Pro.")
    st.download_button("📄 EXPORTAR INFORME BANCARIO", "CERTIFICADO DE ACTIVOS: $12.45M", file_name="Legacy_Audit.txt")
    # Mini gráfico pro
    chart_data = pd.DataFrame({"Activo": ["Propiedades", "Acciones", "Cripto"], "Valor":})
    st.bar_chart(chart_data.set_index("Activo"))

with c2:
    st.subheader("🤖 LEGACY IA: ANALISTA PRIVADO")
    pregunta = st.text_input("CONSULTAR ESTRATEGIA A LA IA:")
    if pregunta:
        with st.spinner('Procesando algoritmos...'):
            time.sleep(1)
            st.write(f"🏛️ **ANALISTA:** Estimado Dylan García, basado en su consulta sobre '{pregunta}', la orden es: MANTENER Y REBALANCIAR.")

# --- 6. SIDEBAR ---
with st.sidebar:
    st.write("### 🔒 SISTEMA")
    if st.checkbox("🔑 MODO ADMIN"):
        st.write("---")
        st.metric(label="VISITAS HOY", value="ACTIVO")
    if st.button("CERRAR SESIÓN"):
        st.session_state.autenticado = False
        st.rerun()
