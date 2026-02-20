import streamlit as st
import pandas as pd
import time

# --- 1. RESET DE SEGURIDAD ---
if 'auth' not in st.session_state: st.session_state.auth = False
if 'reg_final' not in st.session_state: st.session_state.reg_final = None

# --- 2. DISEÑO IMPERIAL ---
st.set_page_config(page_title="LEGACY GOLD", layout="wide")
st.markdown("""
    <style>
    .stApp { background-color: #000000; border: 6px solid #d4af37; padding: 20px; }
    h1, h2, h3 { color: #d4af37 !important; text-align: center; font-family: 'serif'; }
    .gold-card { border: 2px solid #d4af37; padding: 20px; border-radius: 15px; background: rgba(212, 175, 55, 0.05); text-align: center; color: #d4af37; }
    div.stButton > button { background-color: #1a1a1a; color: #d4af37; border: 2px solid #d4af37; width: 100%; font-weight: bold; height: 3em; }
    </style>
    """, unsafe_allow_html=True)

# --- 3. PANTALLA DE ENTRADA (BOTONES, NO LISTA) ---
if not st.session_state.auth:
    st.title("🏛️ LEGACY QUANTUM VAULT")
    col_iz, col_ce, col_de = st.columns([1, 1.5, 1])
    
    with col_ce:
        st.markdown("<div class='gold-card'>💎 ACCESO VIP | 2.000.000 ARS - 12.000 USD</div>", unsafe_allow_html=True)
        st.write("")
        
        # ACÁ ESTÁ EL CAMBIO MAESTRO: ELEGIR CON BOTÓN
        st.subheader("Seleccione Región / Select Region:")
        c1, c2 = st.columns(2)
        if c1.button("🇦🇷 ARGENTINA"): st.session_state.reg_final = "Argentina"
        if c2.button("🇺🇸 USA"): st.session_state.reg_final = "USA"
        
        if st.session_state.reg_final:
            st.success(f"Región: {st.session_state.reg_final}")
            pw = st.text_input("PASSWORD:", type="password", key="password_definitiva_99")
            
            if st.button("DESBLOQUEAR / UNLOCK"):
                if pw == "LEGACY2026":
                    st.session_state.auth = True
                    st.rerun()
                else:
                    st.error("DENEGADO / DENIED")
    st.stop()

# --- 4. INTERFAZ INTERNA ---
reg = st.session_state.reg_final
st.title(f"🏛️ COMMAND CENTER - {reg}")

# SIMULADOR
años = st.slider("AÑOS:", 1, 30, 10)
ret = st.slider("RETORNO %:", 5, 50, 15)
fut_usd = 12450000 * ((1 + (ret/100))**años)

m1, m2 = st.columns(2)
m1.metric("USD VALUE", f"${fut_usd:,.0f}")
if reg == "Argentina":
    m2.metric("VALOR ARS", f"${(fut_usd * 1515):,.0f}")

st.write("---")
# EXCHANGE SEGURO
st.subheader("💹 EXCHANGE VIP")
m_val = st.number_input("Monto / Amount:", min_value=1000000)
mail_url = f"mailto:dylanelpromaster25@://gmail.com{m_val}"
st.markdown(f'<a href="{mail_url}"><button style="width:100%; height:50px; background-color:#d4af37; color:black; font-weight:bold; border:none; border-radius:10px; cursor:pointer;">📩 SOLICITAR COTIZACIÓN</button></a>', unsafe_allow_html=True)

if st.sidebar.button("🔒 SALIR"):
    st.session_state.auth = False
    st.session_state.reg_final = None
    st.rerun()
