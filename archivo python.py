import streamlit as st
import pandas as pd
import time

# --- 1. SEGURIDAD ---
if 'autenticado' not in st.session_state:
    st.session_state.autenticado = False

if not st.session_state.autenticado:
    st.set_page_config(page_title="ACCESO PRIVADO", page_icon="🔐")
    st.markdown("<style>.stApp { background-color: #000000; } h1 { color: #d4af37; text-align: center; }</style>", unsafe_allow_html=True)
    st.title("🔐 TERMINAL DE ACCESO PRIVADO")
    password = st.text_input("LLAVE MAESTRA:", type="password")
    if st.button("DESBLOQUEAR BÓVEDA"):
        if password == "LEGACY2026":
            st.session_state.autenticado = True
            st.rerun()
    st.stop()

# --- 2. CONFIGURACIÓN DE LUJO ---
st.set_page_config(page_title="LEGACY VAULT", page_icon="🏛️", layout="wide")
st.markdown("""
    <style>
    .stApp { background-color: #050505; border: 4px solid #d4af37; padding: 20px; }
    h1, h2, h3 { color: #d4af37 !important; font-family: 'serif'; text-align: center; }
    [data-testid="stMetricValue"] { color: #d4af37 !important; font-size: 2rem !important; font-weight: bold; }
    .pay-banner {
        background-color: rgba(212, 175, 55, 0.15);
        border: 2px solid #d4af37;
        color: #d4af37;
        padding: 20px;
        text-align: center;
        font-weight: bold;
        border-radius: 10px;
        margin-bottom: 30px;
        font-size: 1.2rem;
    }
    </style>
    """, unsafe_allow_html=True)

# --- 3. EL CARTEL DE VENTA (LO QUE PEDISTE) ---
st.markdown("""
<div class='pay-banner'>
    🇦🇷 Para poder usar la app/pagina mas de 1 mes tenes que pagar 2 millones.<br>
    🇺🇸 To use this app/page for more than 1 month you have to pay 12 thousand dollars.
</div>
""", unsafe_allow_html=True)

st.title("🏛️ CENTRO DE MANDO LEGACY")

# 4. SIMULADOR
años = st.slider("AÑOS DE INVERSIÓN:", 1, 30, 10)
ret = st.slider("RENDIMIENTO ANUAL (%)", 5, 50, 15)

# --- CÁLCULOS MATEMÁTICOS (CORRECTOS) ---
tc = 1500  # 1 Dólar = 1500 Pesos (Aproximado 2026)
capital_inicial_usd = 12450000
futuro_usd = capital_inicial_usd * ((1 + (ret/100))**años)
futuro_ars = futuro_usd * tc # ACÁ ESTÁ LA MONTAÑA DE PESOS

st.markdown("---")

# 5. RESULTADOS
res1, res2 = st.columns(2)
res1.metric("PROYECCIÓN DÓLARES (USD)", f"${futuro_usd:,.0f}")
res2.metric("PROYECCIÓN PESOS (ARS)", f"${futuro_ars:,.0f}")

st.markdown("---")

# 6. GRÁFICOS Y IA (YA NO DA ERROR)
c1, c2 = st.columns(2)
with c1:
    st.subheader("📊 DISTRIBUCIÓN")
    df_data = pd.DataFrame({"Activo": ["Casas", "Bolsa", "Cripto", "Arte"], "Valor": [60, 20, 10, 10]})
    st.bar_chart(df_data.set_index("Activo"))
with c2:
    st.subheader("🤖 ESTRATEGA IA")
    pregunta = st.text_input("CONSULTA TÉCNICA:")
    if pregunta:
        st.write(f"🏛️ **IA:** Dylan García, para '{pregunta}' la orden es MANTENER.")
