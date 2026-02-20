import streamlit as st
import pandas as pd
import time

# --- 1. ACCESO BIOMÉTRICO (James Bond en Español) ---
if 'autenticado' not in st.session_state:
    st.session_state.autenticado = False

if not st.session_state.autenticado:
    st.set_page_config(page_title="LEGACY | SEGURIDAD", page_icon="🔐")
    st.markdown("<style>.stApp { background-color: #000000; } h1 { color: #d4af37; text-align: center; font-family: 'Times New Roman'; }</style>", unsafe_allow_html=True)
    st.title("🔐 TERMINAL DE ACCESO PRIVADO")
    password = st.text_input("LLAVE MAESTRA:", type="password")
    if st.button("DESBLOQUEAR BÓVEDA"):
        if password == "LEGACY2026":
            with st.status("Iniciando Protocolos de Seguridad...", expanded=True) as status:
                st.write("🔎 Escaneando firma digital única...")
                time.sleep(1)
                st.write("🛰️ Sincronizando con satélites financieros...")
                time.sleep(1)
                st.write("🟢 Identidad Verificada: Dylan García.")
                status.update(label="Acceso Concedido", state="complete", expanded=False)
            st.session_state.autenticado = True
            st.rerun()
        else:
            st.error("ACCESO DENEGADO.")
    st.stop()

# --- 2. CONFIGURACIÓN DE ÉLITE (DISEÑO DORADO Y NEGRO) ---
st.set_page_config(page_title="LEGACY COMMAND", page_icon="🏛️", layout="wide")
st.markdown("""
    <style>
    .stApp { 
        background-color: #050505; 
        border: 4px solid #d4af37; 
        padding: 20px; 
    }
    h1, h2, h3 { color: #d4af37 !important; font-family: 'serif'; text-align: center; text-transform: uppercase; letter-spacing: 3px; }
    
    /* MÉTRICAS GIGANTES Y DORADAS */
    [data-testid="stMetricValue"] { 
        color: #d4af37 !important; 
        font-size: 4rem !important; 
        font-weight: bold !important; 
        text-align: center !important;
        justify-content: center !important;
    }
    [data-testid="stMetricLabel"] { 
        color: #ffffff !important; 
        font-size: 1.2rem !important;
        text-align: center !important;
        justify-content: center !important;
    }
    [data-testid="stMetric"] {
        text-align: center;
        border: 1px solid rgba(212, 175, 55, 0.3);
        padding: 20px;
        background-color: rgba(212, 175, 55, 0.05);
    }
    
    .stMarkdown p { color: #cccccc; text-align: center; font-size: 1.1rem; }
    div.stButton > button { background-color: #1a1a1a; color: #d4af37; border: 2px solid #d4af37; font-weight: bold; width: 100%; height: 3em; }
    </style>
    """, unsafe_allow_html=True)

# --- 3. INTERFAZ PRINCIPAL ---
st.markdown("<marquee style='color: #d4af37; font-size: 1.2rem;'>● MERCADOS GLOBALES OPERANDO ● SEGURIDAD ACTIVA ● BITCOIN EN TENDENCIA ALCISTA ● ACTIVOS AUDITADOS ●</marquee>", unsafe_allow_html=True)
st.title("🏛️ CENTRO DE MANDO LEGACY")
st.markdown(f"<p style='color: #00ff00;'>● SISTEMA ENCRIPTADO | NIVEL DE SEGURIDAD: MÁXIMO | {time.strftime('%H:%M:%S')}</p>", unsafe_allow_html=True)

# 4. MONITOR DE CAPITAL (GIGANTE)
m1, m2, m3 = st.columns(3)
m1.metric("VALOR NETO", "$12.45M", "+2.4%")
m2.metric("BITCOIN", "$98,450", "+2.5%")
m3.metric("RIESGO", "BAJO", "PROTEGIDO")

st.markdown("---")

# 5. CONSOLA Y GRÁFICOS
col_izq, col_der = st.columns(2)
with col_izq:
    st.subheader("🛡️ REGISTRO DE SEGURIDAD")
    st.code("> RASTREO: ACTIVO\n> CIFRADO: AES-256\n> AUDITORÍA: VERIFICADA", language="bash")
    st.write("---")
    st.subheader("📊 DISTRIBUCIÓN DE ACTIVOS")
    df = pd.DataFrame({"Activo": ["Propiedades", "Acciones", "Cripto", "Arte"], "Valor": [60, 20, 10, 10]})
    st.bar_chart(df.set_index("Activo"))

with col_der:
    st.subheader("🤖 ESTRATEGA IA VIP")
    st.image("https://img.icons8.com", width=100)
    pregunta = st.text_input("CONSULTA TÉCNICA PARA LA IA:")
    if pregunta:
        with st.spinner('Analizando variables...'):
            time.sleep(1)
            st.write(f"🏛️ **IA:** Estimado Dylan García, basado en su consulta sobre '{pregunta}', la orden es: MANTENER POSICIÓN Y DIVERSIFICAR.")
    st.write("---")
    st.download_button("📥 DESCARGAR REPORTE DE AUDITORÍA", "CERTIFICADO DE ACTIVOS: $12.45M USD", file_name="Reporte_Legacy.txt")

if st.sidebar.button("🔒 CERRAR BÓVEDA"):
    st.session_state.autenticado = False
    st.rerun()
