import streamlit as st
import pandas as pd
import time

# --- 1. LÓGICA DE SESIÓN ---
if 'auth' not in st.session_state: st.session_state.auth = False
if 'mensajes' not in st.session_state: st.session_state.mensajes = []

# --- 2. CONFIGURACIÓN CELULAR PAPÁ ---
CEL_PAPA = "5491100000000" # <--- TU NÚMERO ACÁ

# --- 3. DICCIONARIO BILINGÜE REFORZADO ---
textos = {
    "🇦🇷 Argentina": {
        "entrada_tit": "🏛️ LEGACY QUANTUM VAULT",
        "acceso_vip": "💎 ACCESO VIP RESTRINGIDO | 2.000.000 ARS",
        "label_pass": "LLAVE MAESTRA:",
        "btn_unlock": "DESBLOQUEAR BÓVEDA",
        "form_tit": "📩 CONTACTO DIRECTO CON EL FOUNDER",
        "form_mail": "Su Email Corporativo:",
        "form_msg": "Propuesta o Consulta:",
        "form_btn": "ENVIAR AL FOUNDER",
        "ticker": "🏦 MERCADO EN VIVO | USDT/ARS: 1.515 | BTC/USD: 96.850",
        "main_tit": "🏛️ COMMAND CENTER & EXCHANGE VIP",
        "sim_años": "PROYECCIÓN (AÑOS):",
        "sim_ret": "RENTABILIDAD (%):",
        "ex_tit": "💹 MESA DE CAMBIO VIP (P2P)",
        "ex_desc": "Un operador se contactará telefónicamente para la liquidación.",
        "ex_btn": "🚀 SOLICITAR COTIZACIÓN WHATSAPP",
        "ia_tit": "🤖 ESTRATEGA IA",
        "ia_resp": "Dylan García, el análisis sugiere MANTENER POSICIONES.",
        "footer": "🔒 ENCRIPTACIÓN AES-256 | BS. AS. ARGENTINA",
        "seg_tit": "🛡️ PROTOCOLOS DE SEGURIDAD ACTIVOS",
        "seg_node": "NODOS: BS.AS - MIAMI - NY - DUBAI"
    },
    "🇺🇸 USA": {
        "entrada_tit": "🏛️ LEGACY QUANTUM VAULT",
        "acceso_vip": "💎 VIP ACCESS RESTRICTED | 12.000 USD",
        "label_pass": "MASTER KEY:",
        "btn_unlock": "UNLOCK VAULT",
        "form_tit": "📩 DIRECT CONTACT WITH FOUNDER",
        "form_mail": "Corporate Email:",
        "form_msg": "Proposal or Inquiry:",
        "form_btn": "SEND TO FOUNDER",
        "ticker": "🏦 LIVE MARKET | BTC/USD: 96.850 | PROTOCOL: SECURED",
        "main_tit": "🏛️ COMMAND CENTER & OTC DESK",
        "sim_años": "PROJECTION (YEARS):",
        "sim_ret": "ANNUAL RETURN (%):",
        "ex_tit": "💹 GLOBAL OTC DESK (LIQUIDITY)",
        "ex_desc": "Direct settlement for Wire/ACH transfers. An operator will contact you.",
        "ex_btn": "🚀 REQUEST QUOTE VIA WHATSAPP",
        "ia_tit": "🤖 STRATEGIC AI ADVISOR",
        "ia_resp": "Dylan Garcia, the analysis suggests HOLDING POSITIONS.",
        "footer": "🔒 MILITARY GRADE ENCRYPTION | NEW YORK, USA",
        "seg_tit": "🛡️ ACTIVE SECURITY PROTOCOLS",
        "seg_node": "NODES: NY - MIAMI - LONDON - DUBAI"
    }
}

# --- 4. DISEÑO IMPERIAL ---
st.set_page_config(page_title="LEGACY GLOBAL", layout="wide")
st.markdown("""
    <style>
    .stApp { background-color: #000000; border: 6px solid #d4af37; padding: 25px; }
    h1, h2, h3 { color: #d4af37 !important; text-align: center; font-family: 'serif'; }
    .gold-card { border: 2px solid #d4af37; padding: 20px; border-radius: 15px; background: rgba(212, 175, 55, 0.05); text-align: center; color: #d4af37; }
    .ticker { background: #1a1a1a; color: #d4af37; padding: 10px; border-bottom: 2px solid #d4af37; font-weight: bold; text-align: center; }
    .security-badge { border: 1px solid #d4af37; padding: 10px; border-radius: 5px; font-size: 0.7rem; color: #d4af37; text-align: center; }
    </style>
    """, unsafe_allow_html=True)

# --- 5. PANTALLA DE ENTRADA ---
if not st.session_state.auth:
    st.title("🏛️ LEGACY QUANTUM VAULT")
    col_iz, col_ce, col_de = st.columns([1, 1.5, 1])
    with col_ce:
        idioma = st.selectbox("🌎 REGION:", ["🇦🇷 Argentina", "🇺🇸 USA"])
        t = textos[idioma]
        st.markdown(f"<div class='gold-card'>{t['acceso_vip']}</div>", unsafe_allow_html=True)
        pw = st.text_input(t["label_pass"], type="password")
        if st.button(t["btn_unlock"]):
            if pw == "LEGACY2026":
                st.session_state.idioma_final = idioma
                st.session_state.auth = True; st.rerun()
        st.write("---")
        st.subheader(t["form_tit"])
        with st.form("contacto_entrada"):
            m = st.text_input(t["form_mail"]); n = st.text_area(t["form_msg"])
            if st.form_submit_button(t["form_btn"]):
                st.session_state.mensajes.append({"mail": m, "nota": n, "reg": idioma, "hora": time.strftime('%H:%M')})
                st.success("✅ SENT")
    st.stop()

# --- 6. INTERFAZ INTERNA ---
t = textos[st.session_state.idioma_final]
st.markdown(f"<div class='ticker'>{t['ticker']}</div>", unsafe_allow_html=True)
st.title(t["main_tit"])

# SIMULADOR
c_s1, c_s2 = st.columns(2)
años = c_s1.slider(t["sim_años"], 1, 30, 10); ret = c_s2.slider(t["sim_ret"], 5, 50, 15)
fut_usd = 12450000 * ((1 + (ret/100))**años)
m1, m2 = st.columns(2)
m1.metric("USD VALUE", f"${fut_usd:,.0f}")
if st.session_state.idioma_final == "🇦🇷 Argentina": m2.metric("VALOR ARS", f"${(fut_usd * 1515):,.0f}")

st.write("---")
# EXCHANGE
st.subheader(t["ex_tit"])
st.info(t["ex_desc"])
m_val = st.number_input("AMOUNT / MONTO:", min_value=5000)
ws_url = f"https://wa.me{CEL_PAPA}?text=Client%20from%20{st.session_state.idioma_final}:%20Quote%20for%20{m_val}"
st.markdown(f'<a href="{ws_url}" target="_blank"><button style="width:100%; height:50px; background-color:#d4af37; color:black; font-weight:bold; border:none; border-radius:10px; cursor:pointer;">{t["ex_btn"]}</button></a>', unsafe_allow_html=True)

st.write("---")
# IA
st.subheader(t["ia_tit"])
q = st.text_input("CONSULTA / QUERY:")
if q: st.write(f"🏛️ **IA:** {t['ia_resp']}")

# --- 7. PANEL DE SEGURIDAD (LLENA EL ESPACIO FINAL) ---
st.write("---")
st.subheader(t["seg_tit"])
s1, s2, s3, s4 = st.columns(4)
with s1: st.markdown("<div class='security-badge'>🔐 AES-256 BIT<br>ENCRYPTION</div>", unsafe_allow_html=True)
with s2: st.markdown("<div class='security-badge'>🛡️ ISO 27001<br>CERTIFIED</div>", unsafe_allow_html=True)
with s3: st.markdown("<div class='security-badge'>🌐 CLOUD FLARE<br>DDoS PROTECT</div>", unsafe_allow_html=True)
with s4: st.markdown("<div class='security-badge'>🟢 SYSTEM STATUS<br>ONLINE</div>", unsafe_allow_html=True)

st.write("")
st.markdown(f"<p style='text-align: center; font-size: 0.8rem; color: #d4af37;'>{t['seg_node']}</p>", unsafe_allow_html=True)
st.markdown(f"<div style='text-align: center; color: #d4af37; padding: 15px; border-top: 1px solid #d4af37;'>{t['footer']}</div>", unsafe_allow_html=True)

if st.sidebar.button("🔒 EXIT"): st.session_state.auth = False; st.rerun()
