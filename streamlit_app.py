# --- PANEL DE CONTROL FINAL (COPIAR DESDE ACÁ) ---
st.sidebar.write("---")
st.sidebar.markdown("### 🛡️ CONTROL FUNDADOR")
pin_adm = st.sidebar.text_input("INGRESE PIN:", type="password", key="panel_dylan")

if pin_adm == "DYLAN777":
    st.sidebar.success("SISTEMA ONLINE. BIENVENIDO DYLAN.")
    # Mostramos los ingresos que el sistema capturó en memoria
    if 'reg' in st.session_state and st.session_state.reg:
        for r in st.session_state.reg:
            st.sidebar.info(r)
    else:
        st.sidebar.warning("ESPERANDO IMPACTOS... (Nodo en escucha)")

if st.sidebar.button("🔒 LOGOUT / SALIR"):
    st.session_state.auth = False
    st.rerun()
