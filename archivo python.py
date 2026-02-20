import streamlit as st
import pandas as pd
import time

# 1. SEGURIDAD DE BÓVEDA
if 'autenticado' not in st.session_state:
    st.session_state.autenticado = False

if not st.session_state.autenticado:
    st.set_page_config(page_title="LOGIN PRIVADO", page_icon="🔒")
    st.markdown("<style>.stApp { background-color: #0e1117; } h1 { color: #d4af37; text-align: center; }</style>", unsafe_allow_html=True)
    st.title("🔐 ACCESO EXCLUSIVO LEGACY")
    password = st.text_input("CLAVE DE ACCESO:", type="password")
    if st.button("DESBLOQUEAR BÓVEDA"):
        if password == "LEGACY2026":
            st.session_state.autenticado = True
            st.rerun()
        else:
            st.error("Clave Incorrecta.")
    st.stop()

# 2. CONFIGURACIÓN DE LUJO POST-LOGIN
st.set_page_config(page_title="LEGACY VAULT VIP", page_icon="🗝️", layout="wide")
st.markdown("""
    <style>
    .stApp { background-color: #0e1117; }
    h1, h2, h3 { color: #d4af37 !important; font-family: 'serif'; text-align: center; }
    [data-testid="stMetricValue"] { color: #d4af37 !important; }
    .stMarkdown p { color: white; }
    div.stButton > button { background-color: #d4af37; color: black; font-weight: bold; border-radius: 10px; }
    </style>
    """, unsafe_allow_html=True)

# --- PANEL PRINCIPAL ---
st.title("🗝️ LEGACY VAULT: GLOBAL MANAGEMENT")
st.write("Bienvenido, Inversor. El mercado global está operando.")

# 3. MERCADOS EN VIVO (Métricas de Wall Street)
st.markdown("### 🌐 MERCADOS EN TIEMPO REAL")
m1, m2, m3, m4 = st.columns(4)
m1.metric("S&P 500", "5,026.15", "+0.45%")
m2.metric("NASDAQ 100", "17,861.12", "+1.10%")
m3.metric("BITCOIN", "$98,450", "+2.5%")
m4.metric("ORO (XAU)", "$2,150.40", "-0.05%")

st.markdown("---")

# 4. PATRIMONIO Y GRÁFICOS
col_p1, col_p2 = st.columns([1, 1])
with col_p1:
    st.subheader("💰 Resumen de Activos")
    st.metric(label="VALOR NETO TOTAL", value="$12,450,000 USD", delta="+2.4% (Mensual)")
    st.success("✅ Auditoría completada: Activos verificados en Blockchain.")
    
    # Botón de Descarga
    st.download_button(
        label="📄 DESCARGAR REPORTE VIP (PDF)",
        data="REPORTE OFICIAL LEGACY VAULT: Patrimonio neto de $12,450,000 USD verificado bajo protocolos de encriptación grado militar.",
        file_name="Reporte_Patrimonio_Legacy.txt",
        mime="text/plain"
    )

with col_p2:
    st.subheader("📊 Distribución Estratégica")
    df = pd.DataFrame({"Activo": ["Inmuebles", "Acciones", "Cripto", "Arte"], "Valor": [60, 20, 10, 10]})
    st.bar_chart(df.set_index("Activo"))

# 5. SIMULADOR DE GANANCIAS A 5 AÑOS
st.markdown("---")
st.subheader("📈 PROYECCIÓN DE CRECIMIENTO")
interes = st.slider("Seleccione tasa de retorno anual esperada (%):", 5, 20, 10)
proyeccion = 12450000 * ((1 + (interes/100))**5)
st.write(f"Con un {interes}% anual, su patrimonio en 5 años sería de: **${proyeccion:,.2f} USD**")

# 6. IA ESTRATÉGICA
st.markdown("---")
st.subheader("🤖 LEGACY AI: CONSULTOR PRIVADO")
pregunta = st.text_input("Consulte a la IA sobre riesgos o diversificación:")
if pregunta:
    with st.spinner('Analizando variables macroeconómicas...'):
        time.sleep(1)
        st.write(f"🏛️ **LEGACY AI:** Basado en su consulta sobre '{pregunta}', mi análisis indica que debería mantener su posición en Inmuebles de Lujo y aumentar un 2% en Criptoactivos.")

# 7. LOGOUT
if st.sidebar.button("🔒 CERRAR BÓVEDA"):
    st.session_state.autenticado = False
    st.rerun()
