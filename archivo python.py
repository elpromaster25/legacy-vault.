import streamlit as st
import pandas as pd 

# 1. Configuración de Lujo
st.set_page_config(page_title="LEGACY VAULT VIP", page_icon="🗝️", layout="wide")

# 2. Estética Black & Gold (EL SECRETO)
st.markdown("""
    <style>
    .stApp { background-color: #0e1117; }
    h1, h2, h3 { color: #d4af37 !important; font-family: 'serif'; text-align: center; }
    [data-testid="stMetricValue"] { color: #d4af37 !important; }
    [data-testid="stMetricLabel"] { color: #ffffff !important; }
    .stMarkdown p { color: #ffffff; }
    </style>
    """, unsafe_allow_html=True)

st.title("🗝️ LEGACY VAULT: Gestión de Patrimonio Familiar")
st.markdown("<h3 style='text-align: center; color: white;'>Panel de Control de Activos de Alto Nivel</h3>", unsafe_allow_html=True)
st.markdown("---")

# 3. Métricas de los Millones
col1, col2 = st.columns(2)
with col1:
    st.metric(label="VALOR NETO TOTAL", value="$12,450,000 USD", delta="+2.4% (Mensual)")
    st.info("💡 Sugerencia IA: El mercado inmobiliario está subiendo. Mantener activos.")

with col2:
    st.subheader("📊 Composición de la Fortuna")
    data = {"Activo": ["Inmuebles", "Acciones", "Cripto", "Arte"], "Valor": [60, 20, 10, 10]}
    df = pd.DataFrame(data)
    st.bar_chart(df.set_index("Activo"))

# 4. ASISTENTE IA VIP
st.markdown("---")
st.subheader("🤖 LEGACY AI: Tu Estratega Privado")
pregunta = st.text_input("Consultar a la IA sobre inversiones o riesgos:")

if pregunta:
    with st.spinner('Analizando...'):
        if "mendoza" in pregunta.lower():
            st.write("🏛️ **LEGACY AI:** Un campo en Mendoza es gran reserva de valor.")
        else:
            st.write(f"🏛️ **LEGACY AI:** He analizado '{pregunta}'. Mi recomendación es mantener liquidez.")

st.success("🔒 Conexión encriptada con grado militar (AES-256).")

# 5. Pie de Página
st.markdown("<div style='text-align: center; color: #555; font-size: 0.8rem; border-top: 1px solid #d4af37; padding-top: 20px;'>© 2026 LEGACY VAULT S.A. | Private Wealth Management</div>", unsafe_allow_html=True)
