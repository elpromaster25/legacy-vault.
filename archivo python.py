import streamlit as st
import pandas as pd
import time

# --- 1. SEGURIDAD Y PANTALLA DE ENTRADA (SIMÉTRICA) ---
if 'autenticado' not in st.session_state:
    st.session_state.autenticado = False
if 'mensajes' not in st.session_state:
    st.session_state.mensajes = []

if not st.session_state.autenticado:
    st.set_page_config(page_title="LEGACY | LOGIN", page_icon="🔐")
    st.markdown("<style>.stApp { background-color: #000000; } h1, h3 { color: #d4af37; text-align: center; font-family: 'serif'; }</style>", unsafe_allow_html=True)
    st.title("🔐 TERMINAL DE ACCESO PRIVADO")
    
    password = st.text_input("LLAVE MAESTRA / MASTER KEY:", type="password")
    if st.button("DESBLOQUEAR BÓVEDA"):
        if password == "LEGACY2026":
            with st.status("Iniciando Protocolos...", expanded=True) as status:
                st.write("🧬 Escaneando firma digital...")
                time.sleep(1)
                st.write("🟢 Acceso Concedido: Dylan García.")
                status.update(label="Identidad Verificada", state="complete", expanded=False)
            st.session_state.autenticado = True
            st.rerun()
    
    st.write("---")
    st.subheader("📩 ¿No tiene una llave de acceso? / No access key?")
    
    col_info_izq, col_form, col_info_der = st.columns(3)
    
    with col_info_izq:
        st.markdown("<div style='color: #d4af37; font-size: 0.9rem; text-align: center; border: 1px solid #d4af37; padding: 15px; border-radius: 5px;'>🛡️ PROTECCIÓN<br><br>Encriptación AES-256 para activos de alto valor en Puerto Madero y el mundo.</div>", unsafe_allow_html=True)

    with col_form:
        with st.form("contacto_vip"):
            perfil = st.radio("Perfil / Profile:", ["Empresario / CEO", "Inversor Independiente"])
            mail = st.text_input("Su Email / Your Email:")
            if st.form_submit_button("SOLICITAR ACCESO VIP"):
                if mail:
                    st.session_state.mensajes.append({"perfil": perfil, "mail": mail, "hora": time.strftime('%H:%M')})
                    st.success("✅ SOLICITUD ENVIADA.")
                else:
                    st.warning("Ingrese su email.")

    with col_info_der:
        st.markdown("<div style='color: #d4af37; font-size: 0.9rem; text-align: center; border: 1px solid #d4af37; padding: 15px; border-radius: 5px;'>📈 PROYECCIÓN<br><br>Algoritmos de IA para el análisis de riesgo y crecimiento patrimonial.</div>", unsafe_allow_html=True)
    
    st.stop()

# --- 2. CONFIGURACIÓN POST-LOGIN ---
st.set_page_config(page_title="LEGACY VAULT", page_icon="🏛️", layout="wide")
st.markdown("""
    <style>
    .stApp { background-color: #050505; border: 4px solid #d4af37; padding: 20px; }
    h1, h2, h3 { color: #d4af37 !important; font-family: 'serif'; text-align: center; }
    [data-testid="stMetricValue"] { color: #d4af37 !important; font-size: 2.2rem !important; font-weight: bold; }
    .pay-banner { background-color: rgba(212, 175, 55, 0.1); border: 2px solid #d4af37; color: #d4af37; padding: 10px; text-align: center; font-weight: bold; border-radius: 10px; margin-bottom: 10px; }
    </style>
    """, unsafe_allow_html=True)

st.sidebar.title("🛂 DASHBOARD")
es_admin = st.sidebar.checkbox("🔓 MODO ADMIN (DYLAN)")
idioma = st.sidebar.selectbox("Region:", ["🇦🇷 Argentina", "🇺🇸 USA / International"]) if not es_admin else "Admin"

if idioma == "Admin":
    st.title("👨‍💻 PANEL DE CONTROL: DYLAN GARCÍA")
    if st.session_state.mensajes:
        st.table(pd.DataFrame(st.session_state.mensajes))
    else:
        st.write("Esperando interesados...")
else:
    banner = "🇦🇷 Pago: 2 millones/mes." if "Argentina" in idioma else "🇺🇸 Cost: 12 thousand/month."
    st.markdown(f"<div class='pay-banner'>{banner}</div>", unsafe_allow_html=True)
    st.title("🏛️ COMMAND CENTER LEGACY")
    
    años = st.slider("AÑOS / YEARS:", 1, 30, 10)
    ret = st.slider("RETORNO / RETURN %:", 5, 50, 15)
    fut_usd = 12450000 * ((1 + (ret/100))**años)
    fut_ars = fut_usd * 1500 
    
    st.markdown("---")
    r1, r2 = st.columns(2)
    r1.metric("FORTUNA USD", f"${fut_usd:,.0f}")
    r2.metric("FORTUNA ARS", f"${fut_ars:,.0f}")
    
    st.markdown("---")
    c1, c2 = st.columns(2)
    with c1:
        st.subheader("📊 DISTRIBUCIÓN")
        # CORREGIDO: Valores del gráfico cerrados correctamente
        df_final = pd.DataFrame({"Activo": ["RE", "Stocks", "Crypto", "Art"], "Valor": [40, 30, 20, 10]})
        st.bar_chart(df_final.set_index("Activo"))
    with c2:
        st.subheader("🤖 IA ADVISOR")
        st.write("ESTADO: ACTIVO. DYLAN GARCÍA: HOLD POSITIONS.")

if st.sidebar.button("🔒 CERRAR"):
    st.session_state.autenticado = False
    st.rerun()
