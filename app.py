import streamlit as st

# Configuración de la página
st.set_page_config(page_title="Servicios de Limpieza Profesional", page_icon="✨", layout="wide")

# Estilos CSS personalizados para mejorar el diseño
st.markdown("""
    <style>
    .main-title { font-size: 42px !important; font-weight: bold; color: #1E3A8A; text-align: center; margin-bottom: 10px; }
    .subtitle { font-size: 20px !important; text-align: center; color: #4B5563; margin-bottom: 30px; }
    .feature-box { padding: 20px; border-radius: 10px; background-color: #F3F4F6; margin-bottom: 20px; border-left: 5px solid #3B82F6; min-height: 150px; }
    </style>
""", unsafe_allow_html=True)

# --- HEADER / HERO SECTION ---
st.markdown('<p class="main-title">✨ Espacios impecables sin que muevas un dedo</p>', unsafe_allow_html=True)
st.markdown('<p class="subtitle">Servicio de limpieza profesional, confiable y garantizado por hora o mensual.</p>', unsafe_allow_html=True)

# --- CONFIGURACIÓN DE PESTAÑAS (NAVEGACIÓN) ---
tab1, tab2, tab3 = st.tabs(["🧮 Cotizador en Línea", "⚡ Nuestros Servicios", "📞 Contacto y Ubicación"])

# ==========================================
# PESTAÑA 1: COTIZADOR AUTOMATIZADO
# ==========================================
with tab1:
    st.header("🧮 Cotiza tu Servicio al Instante")
    st.write("Selecciona tus requerimientos para obtener un estimado personalizado de inmediato.")

    col_form, col_summary = st.columns(2)

    with col_form:
        tipo_servicio = st.selectbox(
            "1. Selecciona el tipo de servicio:", 
            ["Limpieza de Casas", "Limpieza de Edificios", "Limpieza de Oficinas", "Limpieza de Locales Comerciales", "Limpieza de Clínicas", "Limpieza de Fines de Obra"]
        )
        
        modalidad = st.radio("2. Modalidad de contratación:", ["Por Hora (Servicio Puntual)", "Plan Mensual (Contratación Recurrente)"])
        
        if modalidad == "Por Hora (Servicio Puntual)":
            horas = st.number_input("3. ¿Cuántas horas necesitas para el servicio?", min_value=3, max_value=48, value=4, step=1)
            frecuencia_texto = f"{horas} horas puntuales"
        else:
            horas_semana = st.selectbox("3. ¿Cuántas horas por semana necesitas?", [4, 8, 12, 16, 20, 24, 30, 40])
            frecuencia_texto = f"Plan Mensual ({horas_semana} hs/semana)"
            horas = horas_semana * 4

        # Tarifas actualizadas por hora en $U
        precios_por_hora = {
            "Limpieza de Casas": 350,
            "Limpieza de Oficinas": 400,
            "Limpieza de Locales Comerciales": 400,
            "Limpieza de Edificios": 420,
            "Limpieza de Fines de Obra": 420,
            "Limpieza de Clínicas": 450
        }
        
        precio_actual = precios_por_hora[tipo_servicio]
        subtotal = horas * precio_actual
        
        descuento = 0.15 if modalidad == "Plan Mensual (Contratación Recurrente)" else 0.0
        total = subtotal * (1 - descuento)

    with col_summary:
        st.subheader("📋 Resumen de tu Cotización")
        st.write(f"**Servicio seleccionado:** {tipo_servicio}")
        st.write(f"**Modalidad elegida:** {modalidad}")
        st.write(f"**Detalle del tiempo:** {frecuencia_texto}")
        st.write(f"**Tarifa base:** $U {precio_actual}/hora")
        st.markdown(f"### Estimado Total: **$U {total:,.2f}**")
        
        if descuento > 0:
            st.caption("¡Se aplicó un 15% de descuento exclusivo por contratación Mensual!")
        else:
            st.caption("Mínimo de contratación para servicios puntuales: 3 horas.")
        
        st.write("")
        nombre = st.text_input("Tu Nombre o Empresa")
        telefono = st.text_input("Tu Teléfono de Contacto")
        
        if st.button("Reservar y Enviar por WhatsApp", type="primary"):
            if nombre and telefono:
                mensaje_whatsapp = f"Hola! Me interesa el servicio de *{tipo_servicio}*. Modalidad: {modalidad} ({frecuencia_texto}). El presupuesto estimado de la web es de $U {total:,.2f}. Contacto: {nombre} (Tel: {telefono})."
                link_wa = f"https://wa.me{mensaje_whatsapp.replace(' ', '%20')}"
                st.success("¡Cotización generada correctamente!")
                st.markdown(f"[➡️ Haz clic aquí para enviar la orden por WhatsApp]({link_wa})")
            else:
                st.error("Por favor, completa los campos de nombre y teléfono antes de enviar.")

# ==========================================
# PESTAÑA 2: NUESTROS SERVICIOS
# ==========================================
with tab2:
    st.header("⚡ Soluciones de Limpieza Profesional")
    st.write("Nos adaptamos a las necesidades específicas de cada espacio con personal altamente calificado.")
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.markdown('<div class="feature-box"><h3>🏠 Casas y Edificios</h3><p>Mantenimiento integral para hogares particulares, complejos residenciales y limpieza profunda de áreas comunes en edificios.</p></div>', unsafe_allow_html=True)
        st.markdown('<div class="feature-box"><h3>🏥 Clínicas y Consultorios</h3><p>Protocolos estrictos de sanitización, desinfección profunda y manejo cuidadoso de entornos médicos.</p></div>', unsafe_allow_html=True)

    with col2:
        st.markdown('<div class="feature-box"><h3>🏢 Oficinas Corporativas</h3><p>Garantizamos un ambiente laboral óptimo, limpio y productivo. Flexibilidad absoluta para no interrumpir tus tareas.</p></div>', unsafe_allow_html=True)
        st.markdown('<div class="feature-box"><h3>🏗️ Fines de Obra</h3><p>Remoción profunda y técnica de polvo fino, restos de pintura, siliconas y residuos de construcción para entrega de llaves.</p></div>', unsafe_allow_html=True)

    with col3:
        st.markdown('<div class="feature-box"><h3>🛍️ Locales Comerciales</h3><p>Limpieza de vidrieras, salones de venta y showrooms. Hacemos que tu negocio brille para tus clientes.</p></div>', unsafe_allow_html=True)

# ==========================================
# PESTAÑA 3: CONTACTO Y UBICACIÓN
# ==========================================
with tab3:
    st.header("📞 Ponte en Contacto")
    st.write("¿Tienes alguna duda o un requerimiento especial? Comunícate directamente con nuestra administración.")
    
    c_info, c_form = st.columns(2)
    
    with c_info:
        st.subheader("📍 Datos de Contacto")
        st.markdown("""
        *   **Teléfono / WhatsApp:** [+598 091 295 245](https://wa.me)
        *   **Zona de Cobertura:** Montevideo y alrededores (consultar por otras zonas).
        *   **Horario de Atención:** Lunes a Sábados de 08:00 a 18:00 hs.
        """)
        st.info("🔒 **Nota de seguridad:** Todo nuestro personal trabaja debidamente asegurado y bajo rigurosos controles de confianza.")
        
    with c_form:
        st.subheader("✉️ Envíanos un mensaje directo")
        c_nombre = st.text_input("Nombre completo")
        c_correo = st.text_input("Correo electrónico")
        c_msg = st.text_area("¿En qué podemos ayudarte?")
        
        if st.button("Enviar Consulta General"):
            if c_nombre and c_msg:
                st.success(f"¡Gracias {c_nombre}! Tu consulta ha sido enviada. Te responderemos a la brevedad.")
            else:
                st.error("Por favor completa los campos mínimos (Nombre y Mensaje).")

st.write("---")

# --- PIE DE PÁGINA / CONFIANZA ---
c1, c2, c3 = st.columns(3)
with c1:
    st.markdown("🔒 **Seguridad Garantizada**\n\nFiltros estrictos de selección de personal y cobertura total ante imprevistos.")
with c2:
    st.markdown("⭐ **Satisfacción al 100%**\n\nSi algún detalle no cumple con tus expectativas, lo repasamos sin ningún costo adicional.")
with c3:
    st.markdown("🗓️ **Cancelación Flexible**\n\nModifica o reagenda tus jornadas contratadas avisando con 24 horas de anticipación.")
