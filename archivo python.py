import streamlit as st
import pandas as pd
import time

# --- 1. MEMORIA DEL SISTEMA (Acá se guardan los mensajes) ---
if 'mensajes' not in st.session_state:
    st.session_state.mensajes = []
if 'autenticado' not in st.session_state:
    st.session_state.autenticado = False

# --- 2. PANTALLA DE ENTRADA ---
if not st.session_state.autenticado:
    st.set_page_config(page_title="ACCESO PRIVADO", page_icon="🔐")
    st.markdown("<style>.stApp { background-color: #000000; } h1, h3 { color: #d4af37; text-align: center; }</style>", unsafe_allow_html=True)
    st.title("🔐 ACCESO RESTRINGIDO: LEGACY VAULT")
    
    password = st.text_input("LLAVE MAESTRA:", type="password")
    if st.button("DESBLOQUEAR BÓVEDA"):
        if password == "LEGACY2026":
            st.session_state.autenticado = True
            st.rerun()
    
    st.write("---")
    st.subheader("📩 ¿No tiene una llave? Deje su contacto aquí:")
    with st.form("contacto_vip"):
        perfil = st.radio("Usted es:", ["Empresario / CEO", "Inversor Independiente"])
        mail = st.text_input("Su Email:")
        nota = st.text_area("Mensaje para el Founder:")
        if st.form_submit_button("SOLICITAR ACCESO VIP"):
            if mail:
                # Se guarda en la lista secreta
                st.session_state.mensajes.append({"perfil": perfil, "mail": mail, "nota": nota, "hora": time.strftime('%H:%M')})
                st.success("✅ SOLICITUD ENVIADA. Un analista revisará su perfil.")
            else:
                st.warning("Por favor, ingrese su email.")
    st.stop()

# --- 3. CONFIGURACIÓN DE LUJO ---
st.set_page_config(page_title="LEGACY VAULT", page_icon="🏛️", layout="wide")
st.markdown("""
    <style>
    .stApp { background-color: #050505; border: 4px solid #d4af37; padding: 20px; }
    h1, h2, h3 { color: #d4af37 !important; text-align: center; }
    [data-testid="stMetricValue"] { color: #d4af37 !important; font-size: 2.2rem !important; font-weight: bold; }
    .pay-banner { background-color: rgba(212, 175, 55, 0.1); border: 2px solid #d4af37; color: #d4af37; padding: 10px; text-align: center; font-weight: bold; border-radius: 10px; margin-bottom: 10px; }
    </style>
    """, unsafe_allow_html=True)

# --- 4. PANEL DE CONTROL (ADMIN & TRADUCTOR) ---
st.sidebar.title("🛂 DASHBOARD")
es_admin = st.sidebar.checkbox("🔓 MODO ADMIN (DYLAN)")
idioma = st.sidebar.selectbox("Region:", ["🇦🇷 Argentina", "🇺🇸 USA / International"]) if not es_admin else "Admin"

# --- 5. INTERFAZ DINÁMICA ---
if idioma == "Admin":
    st.title("👨‍💻 PANEL CENTRAL DE DYLAN")
    st.subheader("📬 MENSAJES RECIBIDOS DE EMPRESARIOS")
    if st.session_state.mensajes:
        st.table(pd.DataFrame(st.session_state.mensajes))
    else:
        st.write("Aún no hay mensajes. ¡Mañana a las 11 AM llegarán!")
else:
    # Versión para el cliente (la que ya teníamos)
    banner = "🇦🇷 Pago: 2 millones/mes" if "Argentina" in idioma else "🇺🇸 Cost: 12k USD/month"
    st.markdown(f"<div class='pay-banner'>{banner}</div>", unsafe_allow_html=True)
    st.title("🏛️ CENTRO DE MANDO LEGACY")
    
    # Simulador y el resto de tu código pro...
    años = st.slider("AÑOS / YEARS:", 1, 30, 10)
    ret = st.slider("RETORNO / RETURN %:", 5, 50, 15)
    fut_usd = 12450000 * ((1 + (ret/100))**años)
    fut_ars = fut_usd * 1500 # TC 2026
    
    st.markdown("---")
    r1, r2 = st.columns(2)
    r1.metric("FORTUNA USD", f"${fut_usd:,.0f}")
    r2.metric("FORTUNA ARS", f"${fut_ars:,.0f}")
    
    st.markdown("---")
    st.subheader("📊 DISTRIBUCIÓN")
    df = pd.DataFrame({"Activo": ["RE", "Stocks", "Crypto", "Art"], "Valor": [50, 25, 15, 10]})
    st.bar_chart(df.set_index("Activo"))

if st.sidebar.button("🔒 CERRAR"):
    st.session_state.autenticado = False
    st.rerun()
