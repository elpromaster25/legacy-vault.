import streamlit as st
import pandas as pd
import time

# --- 1. CONFIGURACIÓN DE SEGURIDAD ---
if 'auth' not in st.session_state: st.session_state.auth = False
if 'idioma_final' not in st.session_state: st.session_state.idioma_final = "🇦🇷 Argentina"

# --- 2. TU EMAIL DE CONTROL ---
MI_EMAIL = "dylanelpromaster25@gmail.com" 

# --- 3. DICCIONARIO BILINGÜE ---
textos = {
    "🇦🇷 Argentina": {
        "acceso_vip": "💎 ACCESO VIP RESTRINGIDO | 2.000.000 ARS",
        "btn_unlock": "DESBLOQUEAR BÓVEDA",
        "ticker": "🏦 MERCADO EN VIVO | USDT/ARS: 1.515 | BTC/USD: 96.850",
        "main_tit": "🏛️ COMMAND CENTER & EXCHANGE VIP",
        "ex_tit": "💹 MESA DE CAMBIO VIP (LIQUIDACIÓN P2P)",
        "ex_desc": "Solicite cotización oficial. Recibirá instrucciones en su email.",
        "ex_btn": "📩 SOLICITAR COTIZACIÓN POR EMAIL",
        "ia_tit": "🤖 ESTRATEGA IA ADVISOR",
        "ia_resp": "Dylan García, el análisis sugiere MANTENER POSICIONES.",
        "footer": "🔒 ENCRIPTACIÓN AES-256 | SEGURIDAD BANCARIA | BS. AS."
    },
    "🇺🇸 USA": {
        "acceso_vip": "💎 VIP ACCESS RESTRICTED | 12.000 USD",
        "btn_unlock": "UNLOCK VAULT",
        "ticker": "🏦 LIVE MARKET | BTC/USD: 96.850 | PROTOCOL: SECURED",
        "main_tit": "🏛️ COMMAND CENTER & OTC DESK",
        "ex_tit": "💹 GLOBAL OTC DESK (INSTITUTIONAL LIQUIDITY)",
        "ex_desc": "Request institutional quote. You will receive instructions via email.",
        "ex_btn": "📩 REQUEST QUOTE VIA EMAIL",
        "ia_tit": "🤖 STRATEGIC AI ADVISOR",
        "ia_resp": "Dylan Garcia, the analysis suggests HOLDING POSITIONS.",
        "footer": "🔒 MILITARY GRADE ENCRYPTION | NEW YORK, USA"
    }
}

# --- 4. DISEÑO IMPERIAL ---
st.set_page_config(page_title="LEGACY SECURE", layout="wide")
st.markdown("""
    <style>
    .stApp { background-color: #000000; border: 6px solid #d4af37; padding: 25px; }
    h1, h2, h3 { color: #d4af37 !important; text-align: center; font-family: 'serif'; }
    .gold-card { border: 2px solid #d4af37; padding: 20px; border-radius: 15px; background: rgba(212, 175, 55, 0.05); text-align: center; color: #d4af37; }
    [data-testid='stMetricValue'] { color: #d4af37 !important; font-size: 2.5rem !important; }
    </style>
    """, unsafe_allow_html=True)

# --- 5. PANTALLA DE ENTRADA (ARREGLADA) ---
if not st.session_state.auth:
    st.title("🏛️ LEGACY QUANTUM VAULT")
    col_iz, col_ce, col_de = st.columns([1, 1.5, 1])
    with col_ce:
        # AGREGAMOS KEY UNICA PARA QUE NO SE MEZCLE
        region_elegida = st.selectbox("🌎 REGION / REGIÓN:", ["🇦🇷 Argentina", "🇺🇸 USA"], key="region_select")
        t = textos[region_elegida]
        
        st.markdown(f"<div class='gold-card'>{t['acceso_vip']}</div>", unsafe_allow_html=True)
        
        # CONTRASEÑA CON KEY UNICA
        pw = st.text_input("PASSWORD:", type="password", key="pass_input")
        
        if st.button(t["btn_unlock"]):
            if pw == "LEGACY2026":
                st.session_state.idioma_final = region_elegida
                st.session_state.auth = True
                st.rerun()
            else:
                st.error("DENEGADO / DENIED")
    st.stop()

# --- 6. INTERFAZ INTERNA ---
t = textos[st.session_state.idioma_final]
st.markdown(f"<div style='background: #1a1a1a; color: #d4af37; padding: 10px; border-bottom: 2px solid #d4af37; font-weight: bold; text-align: center;'>{t['ticker']}</div>", unsafe_allow_html=True)

st.title(t["main_tit"])

# SIMULADOR
años = st.slider("HORIZONTE / HORIZON:", 1, 30, 10); ret = st.slider("RETORNO / RETURN %:", 5, 50, 15)
fut_usd = 12450000 * ((1 + (ret/100))**años)
m1, m2 = st.columns(2)
m1.metric("USD VALUE", f"${fut_usd:,.0f}")
if st.session_state.idioma_final == "🇦🇷 Argentina":
    m2.metric("VALOR ARS", f"${(fut_usd * 1515):,.0f}")

st.write("---")
# EXCHANGE SEGURO POR EMAIL
st.subheader(t["ex_tit"])
st.info(t["ex_desc"])
ex1, ex2 = st.columns(2)

with ex1:
    st.markdown("<div class='gold-card'>💰 CASH TO USDT (DOLLAR)</div>", unsafe_allow_html=True)
    m_ars = st.number_input("Monto / Amount:", min_value=1000000, value=5000000)
    asunto = "Legacy%20Vault%20-%20Request%20for%20Liquidity"
    cuerpo = f"Hello,%20I%20request%20a%20quote%20to%20liquidate%20funds%20worth%20{m_ars}%20for%20USDT."
    mail_url = f"mailto:{MI_EMAIL}?subject={asunto}&body={cuerpo}"
    st.markdown(f'<a href="{mail_url}"><button style="width:100%; height:50px; background-color:#d4af37; color:black; font-weight:bold; border:none; border-radius:10px; cursor:pointer;">{t["ex_btn"]}</button></a>', unsafe_allow_html=True)

with ex2:
    st.markdown("<div class='gold-card'>₿ BITCOIN TO CASH</div>", unsafe_allow_html=True)
    m_btc = st.number_input("Monto / Amount BTC:", min_value=0.01, value=0.1)
    asunto_btc = "Legacy%20Vault%20-%20BTC%20Liquidation"
    cuerpo_btc = f"Hello,%20I%20request%20a%20quote%20to%20sell%20{m_btc}%20BTC%20for%20cash."
    mail_url_btc = f"mailto:{MI_EMAIL}?subject={asunto_btc}&body={cuerpo_btc}"
    st.markdown(f'<a href="{mail_url_btc}"><button style="width:100%; height:50px; background-color:#d4af37; color:black; font-weight:bold; border:none; border-radius:10px; cursor:pointer;">{t["ex_btn"]}</button></a>', unsafe_allow_html=True)

st.write("---")
st.subheader(t["ia_tit"])
q = st.text_input("CONSULTA / QUERY:")
if q: st.write(f"🏛️ **IA:** {t['ia_resp']}")

st.write("---")
st.markdown(f"<div style='text-align: center; color: #d4af37; padding: 20px; font-weight: bold;'>{t['footer']}</div>", unsafe_allow_html=True)

if st.sidebar.button("🔒 LOGOUT"): st.session_state.auth = False; st.rerun()
