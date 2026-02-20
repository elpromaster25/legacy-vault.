import streamlit as st
import pandas as pd
import time

# --- 1. LÓGICA DE SESIÓN ---
if 'auth' not in st.session_state: st.session_state.auth = False
if 'mensajes' not in st.session_state: st.session_state.mensajes = []

# --- 2. CONFIGURACIÓN CELULAR PAPÁ (PONELO ACÁ) ---
CEL_PAPA = "5491100000000" # <--- CAMBIÁ ESTO POR EL NÚMERO DE ÉL

# --- 3. DICCIONARIO BILINGÜE (EL CEREBRO) ---
textos = {
    "🇦🇷 Argentina": {
        "ticker": "🏦 MERCADO EN VIVO | USDT/ARS: 1.515 | BTC/USD: 96.850",
        "entrada": "💎 ACCESO VIP RESTRINGIDO | 2.000.000 ARS",
        "sim_tit": "🏛️ COMMAND CENTER & EXCHANGE",
        "sim_años": "PROYECCIÓN (AÑOS):",
        "sim_ret": "RENTABILIDAD (%):",
        "ex_tit": "💹 MESA DE CAMBIO VIP (P2P)",
        "ex_desc": "Un operador se contactará telefónicamente para la liquidación.",
        "ex_btn": "🚀 SOLICITAR COTIZACIÓN WHATSAPP",
        "ia_tit": "🤖 ESTRATEGA IA",
        "ia_resp": "Dylan García, el análisis sugiere MANTENER POSICIONES.",
        "footer": "🔒 ENCRIPTACIÓN AES-256 | BS. AS. ARGENTINA"
    },
    "🇺🇸 USA": {
        "ticker": "🏦 LIVE MARKET | BTC/USD: 96.850 | PROTOCOL: SECURED",
        "entrada": "💎 VIP ACCESS RESTRICTED | 12.000 USD",
        "sim_tit": "🏛️ COMMAND CENTER & OTC DESK",
        "sim_años": "PROJECTION (YEARS):",
        "sim_ret": "ANNUAL RETURN (%):",
        "ex_tit": "💹 GLOBAL OTC DESK (LIQUIDITY)",
        "ex_desc": "Direct settlement for Wire/ACH transfers. An operator will contact you.",
        "ex_btn": "🚀 REQUEST QUOTE VIA WHATSAPP",
        "ia_tit": "🤖 STRATEGIC AI ADVISOR",
        "ia_resp": "Dylan Garcia, the analysis suggests HOLDING POSITIONS.",
        "footer": "🔒 MILITARY GRADE ENCRYPTION | NEW YORK, USA"
    }
}

# --- 4. DISEÑO IMPERIAL ---
st.set_page_config(page_title="LEGACY GLOBAL", layout="wide")
st.markdown("<style>.stApp { background-color: #000000; border: 6px solid #d4af37; padding: 25px; } h1, h2, h3 { color: #d4af37 !important; text-align: center; } .gold-card { border: 2px solid #d4af37; padding: 20px; border-radius: 15px; background: rgba(212, 175, 55, 0.05); text-align: center; color: #d4af37; }</style>", unsafe_allow_html=True)

# --- 5. SELECTOR DE REGIÓN (SIDEBAR) ---
st.sidebar.title("🛂 REGION")
idioma = st.sidebar.selectbox("Select Country:", ["🇦🇷 Argentina", "🇺🇸 USA"])
t = textos[idioma]

# --- 6. TICKER ---
st.markdown(f"<div style='background: #1a1a1a; color: #d4af37; padding: 10px; border-bottom: 2px solid #d4af37; font-weight: bold; text-align: center;'>{t['ticker']}</div>", unsafe_allow_html=True)

# --- 7. ACCESO ---
if not st.session_state.auth:
    st.title("🏛️ LEGACY QUANTUM VAULT")
    col_iz, col_ce, col_de = st.columns([1, 1.5, 1])
    with col_ce:
        st.markdown(f"<div class='gold-card'>{t['entrada']}</div>", unsafe_allow_html=True)
        pw = st.text_input("PASSWORD:", type="password")
        if st.button("UNLOCK"):
            if pw == "LEGACY2026": st.session_state.auth = True; st.rerun()
    st.stop()

# --- 8. COMMAND CENTER BILINGÜE ---
st.title(t["sim_tit"])

# SIMULADOR
c_s1, c_s2 = st.columns(2)
años = c_s1.slider(t["sim_años"], 1, 30, 10)
ret = c_s2.slider(t["sim_ret"], 5, 50, 15)
fut_usd = 12450000 * ((1 + (ret/100))**años)
m1, m2 = st.columns(2)
m1.metric("USD VALUE", f"${fut_usd:,.0f}")
if idioma == "🇦🇷 Argentina":
    m2.metric("ARS VALUE", f"${(fut_usd * 1515):,.0f}")

st.write("---")
# EXCHANGE
st.subheader(t["ex_tit"])
st.info(t["ex_desc"])
ex1, ex2 = st.columns(2)
with ex1:
    m_val = st.number_input("CASH AMOUNT:", min_value=5000)
    ws_msg = f"https://wa.me{CEL_PAPA}?text=Client%20from%20{idioma}:%20Requesting%20quote%20for%20{m_val}"
    st.markdown(f'<a href="{ws_msg}" target="_blank"><button style="width:100%; height:50px; background-color:#d4af37; color:black; font-weight:bold; border:none; border-radius:10px; cursor:pointer;">{t["ex_btn"]}</button></a>', unsafe_allow_html=True)

st.write("---")
# IA
st.subheader(t["ia_tit"])
q = st.text_input("CONSULTA / QUERY:")
if q: st.write(f"🏛️ **IA:** {t['ia_resp']}")

# FOOTER
st.write("---")
c_t1, c_t2, c_t3 = st.columns(3)
with c_t1: st.markdown("<div class='gold-card'>🗽 NY: 11:14 AM</div>", unsafe_allow_html=True)
with c_t2: st.markdown("<div class='gold-card'>🏢 BA: 13:14 PM</div>", unsafe_allow_html=True)
with c_t3: st.markdown("<div class='gold-card'>🏰 LN: 16:14 PM</div>", unsafe_allow_html=True)
st.markdown(f"<div style='text-align: center; color: #d4af37; padding: 20px;'>{t['footer']}</div>", unsafe_allow_html=True)

if st.sidebar.button("🔒 EXIT"): st.session_state.auth = False; st.rerun()
