import streamlit as st
import pandas as pd
import time

# --- 1. SEGURIDAD Y PANTALLA DE ENTRADA ---
if 'autenticado' not in st.session_state:
    st.session_state.autenticado = False

if not st.session_state.autenticado:
    st.set_page_config(page_title="LEGACY | LOGIN", page_icon="🔐")
    st.markdown("<style>.stApp { background-color: #000000; } h1, h3 { color: #d4af37; text-align: center; }</style>", unsafe_allow_html=True)
    
    st.title("🔐 ACCESO PRIVADO: LEGACY VAULT")
    
    # LOGIN NORMAL
    password = st.text_input("LLAVE MAESTRA:", type="password")
    if st.button("DESBLOQUEAR BÓVEDA"):
        if password == "LEGACY2026":
            st.session_state.autenticado = True
            st.rerun()
        else:
            st.error("LLAVE INVÁLIDA.")
    
    st.write("---")
    
    # --- TU IDEA: EL CANAL PARA NUEVOS SOCIOS ---
    st.subheader("¿No tiene una llave? Solicite una entrevista.")
    
    opcion = st.radio("Seleccione su perfil profesional:", 
                      ["💼 Soy Empresario / CEO", "🦈 Soy Inversor Independiente (High-Net-Worth)"])
    
    email_contacto = st.text_input("Ingrese su Email Corporativo / Privado:")
    
    if st.button("ENVIAR SOLICITUD DE ACCESO"):
        if email_contacto:
            with st.spinner("Enviando reporte a la central..."):
                time.sleep(2)
                # AQUÍ SE SIMULA LA NOTIFICACIÓN
                if "Empresario" in opcion:
                    st.success(f"NOTIFICACIÓN ENVIADA: Un Analista Senior de Legacy se contactará con usted, CEO.")
                    # Dylan, aquí verías en tus 'logs' que un Empresario te busca.
                else:
                    st.success(f"NOTIFICACIÓN ENVIADA: El departamento de Wealth Management revisará su perfil de inversor.")
        else:
            st.warning("Por favor, ingrese un email válido.")
            
    st.stop()

# --- 2. CONFIGURACIÓN POST-LOGIN (DISEÑO DORADO) ---
st.set_page_config(page_title="LEGACY VAULT", page_icon="🏛️", layout="wide")
st.markdown("""
    <style>
    .stApp { background-color: #050505; border: 4px solid #d4af37; padding: 20px; }
    h1, h2, h3 { color: #d4af37 !important; font-family: 'serif'; text-align: center; }
    [data-testid="stMetricValue"] { color: #d4af37 !important; font-size: 2.2rem !important; font-weight: bold; }
    .pay-banner { background-color: rgba(212, 175, 55, 0.1); border: 2px solid #d4af37; color: #d4af37; padding: 15px; text-align: center; font-weight: bold; border-radius: 10px; margin-bottom: 10px; }
    </style>
    """, unsafe_allow_html=True)

# (Aquí sigue el resto de tu código de 12 millones, IA y traductor que ya teníamos)
st.title("🏛️ CENTRO DE MANDO LEGACY")
st.info(f"Sessión activa: Administrador Dylan García")
# ... resto del código ...
