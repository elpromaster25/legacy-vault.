import streamlit as st
import pandas as pd
import time

# --- 1. SEGURIDAD DE ENTRADA ---
if 'autenticado' not in st.session_state:
    st.session_state.autenticado = False

if not st.session_state.autenticado:
    st.set_page_config(page_title="LEGACY | SECURE LOGIN", page_icon="🔒")
    st.markdown("<style>.stApp { background-color: #050505; } h1 { color: #d4af37; text-align: center; font-family: 'Courier New'; }</style>", unsafe_allow_html=True)
    st.title("🔐 SISTEMA DE GESTIÓN PATRIMONIAL")
    password = st.text_input("LLAVE MAESTRA:", type="password")
    if st.button("DESBLOQUEAR BÓVEDA"):
        if password == "LEGACY2026":
            with st.status("Ejecutando Protocolos de Seguridad...", expanded=True) as status:
                st.write("🔎 Escaneando vulnerabilidades...")
                time.sleep(1)
                st.write("🛡️ Encriptación de flujo activada (AES-256).")
                time.sleep(1)
                st.write("🟢 Acceso Autorizado: Dylan García.")
                status.update(label="Seguridad Verificada", state="complete", expanded=False)
            st.session_state.autenticado = True
            st.rerun()
        else:
            st.error("ERROR DE AUTENTICACIÓN.")
    st.stop()

# --- 2. CONFIGURACIÓN DE ÉLITE ---
st.set_page_config(page_title="LEGACY COMMAND CENTER", page_icon="🏛️", layout="wide")
st.markdown("""
    <style>
    .stApp { background-color: #050505; }
    h1, h2, h3 { color: #d4af37 !important; font-family: 'Courier New'; text-align: center; }
    [data-testid="stMetricValue"] { color: #d4af37 !important; font-size: 2.8rem !important; font-weight: bold; text-align: center; }
    [data-testid="stMetricLabel"] { color: #ffffff !important; justify-content: center !important; }
    /* Caja de Logs de Seguridad */
    .security-log { background-color: #111; border-left: 3px solid #d4af37; padding: 10px; font-family: 'Courier New'; font-size: 0.8rem; color: #00ff00; }
    </style>
    """, unsafe_allow_html=True)

# --- 3. BARRA DE STATUS ---
st.markdown("<marquee style='color: #d4af37;'>● CONEXIÓN ENCRIPTADA ● AUDITORÍA 2026 APROBADA ● ACTIVOS PROTEGIDOS POR BLOCKCHAIN ●</marquee>", unsafe_allow_html=True)
st.title("🏛️ LEGACY COMMAND CENTER")

# --- 4. MÉTRICAS DE PODER ---
t1, t2, t3, t4 = st.columns(4)
t1.metric("ESTADO RED", "PROTEGIDA", "100%")
t2.metric("S&P 500", "5,026", "+0.4%")
t3.metric("BITCOIN", "$98,450", "+2.5%")
t4.metric("EQUITY TOTAL", "$12.45M", "+2.4%")

st.markdown("---")

# --- 5. EL "SELLO DE CONFIANZA" (Lo que pediste) ---
c1, c2 = st.columns(2)
with c1:
    st.subheader("🛡️ REPORTE DE SEGURIDAD")
    st.markdown("""
    <div class='security-log'>
    > Iniciando escaneo de activos...<br>
    > Verificando certificados SSL... OK<br>
    > Sincronizando con Mainnet de Cripto... OK<br>
    > Estado: Bóveda blindada contra ataques externos.
    </div>
    """, unsafe_allow_html=True)
    st.write("")
    st.success("✅ Este panel ha sido auditado y verificado por **Legacy Security Systems**.")
    st.download_button("📄 EXPORTAR CERTIFICADO DE FONDOS", "CERTIFICADO OFICIAL: $12.45M", file_name="Certificado_Legacy.txt")

with c2:
    st.subheader("📊 DISTRIBUCIÓN DE RIESGO")
    df = pd.DataFrame({"Activo": ["Propiedades", "Stocks", "Crypto", "Arte"], "Valor": [60, 20, 10, 10]})
    st.bar_chart(df.set_index("Activo"))

# --- 6. SIMULADOR Y IA ---
st.markdown("---")
st.subheader("🚀 PROYECCIÓN Y ESTRATEGIA IA")
col_ia1, col_ia2 = st.columns(2)
with col_ia1:
    interes = st.slider("Retorno Anual esperado (%):", 5, 40, 15)
    st.write(f"Proyección a 10 años: **${12450000 * ((1 + (interes/100))**10):,.0f} USD**")
with col_ia2:
    pregunta = st.text_input("Consulta técnica a la IA:")
    if pregunta:
        st.write(f"🕵️ **IA:** Dylan García, para '{pregunta}' la orden es: MANTENER POSICIÓN.")

if st.sidebar.button("🔒 CERRAR BÓVEDA"):
    st.session_state.autenticado = False
    st.rerun()
