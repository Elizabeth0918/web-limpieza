import streamlit as st

# Configuración de la página oficial de KMG Elizabeth
st.set_page_config(page_title="KMG Elizabeth - Servicio Independiente de Limpieza", page_icon="✨", layout="wide")

# Estilos CSS con tu paleta real: Blanco, Celeste (#0284C7) y Detalles Dorados (#D97706)
st.markdown("""
    <style>
    /* Fondo celeste muy claro y limpio con textos oscuros para máxima legibilidad */
    .stApp { background-color: #F0F9FF; color: #0F172A; }
    
    /* Encabezados y títulos principales */
    .main-title { font-size: 34px !important; font-weight: 800; color: #0284C7; text-align: center; margin-top: 10px; margin-bottom: 5px; }
    .subtitle { font-size: 20px !important; text-align: center; color: #475569; margin-bottom: 30px; font-weight: 600; }
    
    /* Cajas de servicios en blanco puro con bordes celestes y dorados */
    .feature-box { padding: 22px; border-radius: 12px; background-color: #FFFFFF; margin-bottom: 20px; border-left: 6px solid #0284C7; border-top: 2px solid #D97706; min-height: 160px; box-shadow: 0 4px 6px -1px rgba(0,0,0,0.05); }
    .feature-box h3 { color: #0284C7 !important; margin-top: 0px; font-weight: bold; }
    .feature-box p { color: #334155 !important; font-size: 15px; }
    
    /* Formulario y textos de selección */
    h1, h2, h3, .stSelectbox label, .stRadio label, .stTextInput label, .stTextArea label { color: #0284C7 !important; font-weight: bold; }
    
    /* Contenedor del resumen con estética Dorada */
    .summary-box { background-color: #FFFFFF; padding: 25px; border-radius: 12px; border: 3px solid #D97706; box-shadow: 0 10px 15px -3px rgba(0,0,0,0.05); }
    
    /* Botones dorados elegantes */
    div.stButton > button:first-child { background-color: #D97706 !important; color: white !important; font-weight: bold !important; border: none !important; padding: 10px 20px !important; border-radius: 8px !important; width: 100%; }
    div.stButton > button:first-child:hover { background-color: #B45309 !important; }
    </style>
""", unsafe_allow_html=True)

# --- HEADER CON TU LOGOTIPO INTEGRADO DESDE INTERNET ---
st.markdown('<div style="text-align:center;"><img src="https://ibb.co" width="320" style="margin-bottom:15px; border-radius:15px;"></div>', unsafe_allow_html=True)
st.markdown('<p class="main-title">KMG ELIZABETH</p>', unsafe_allow_html=True)
st.markdown('<p class="subtitle">LIMPIEZA · SERVICIO INDEPENDIENTE EN URUGUAY</p>', unsafe_allow_html=True)

# --- CONFIGURACIÓN DE PESTAÑAS DE NAVEGACIÓN ---
tab1, tab2, tab3 = st.tabs(["🧮 Cotizador de Jornadas", "⚡ Nuestros Servicios Especializados", "📞 Contacto Directo"])

# ==========================================
# PESTAÑA 1: COTIZADOR AUTOMATIZADO
# ==========================================
with tab1:
    st.markdown("<h3 style='color:#D97706 !important; margin-top:0px;'>🧮 Calcula tu Presupuesto Express</h3>", unsafe_allow_html=True)
    st.write("Selecciona tu modalidad y las horas exactas de tu jornada para recibir tu cotización.")
    st.write("")

    col_form, col_summary = st.columns(2)

    with col_form:
        tipo_servicio = st.selectbox(
            "1. Selecciona el tipo de espacio a limpiar:", 
            ["Limpieza de Casas", "Limpieza de Edificios", "Limpieza de Oficinas", "Limpieza de Locales Comerciales", "Limpieza de Clínicas", "Limpieza de Fines de Obra"]
        )
        
        modalidad = st.radio("2. Modalidad de contratación:", ["Por Hora (Servicio Puntual)", "Plan Mensual (Contratación Recurrente)"])
        
        # Filtro estricto solicitado de 4, 6 u 8 horas aplicados a ambas opciones
        if modalidad == "Por Hora (Servicio Puntual)":
            horas_opcion = st.selectbox("3. Horas requeridas para la jornada puntual:", [4, 6, 8])
            horas = horas_opcion
            frecuencia_texto = f"Jornada puntual de {horas} horas"
        else:
            horas_semana = st.selectbox("3. Horas fijas de limpieza por semana:", [4, 6, 8])
            frecuencia_texto = f"Plan Mensual ({horas_semana} hs/semana)"
            horas = horas_semana * 4

        # Precios base en Pesos Uruguayos ($U) por hora
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
        
        # Descuento exclusivo del 15% para planes mensuales recurrentes
        descuento = 0.15 if modalidad == "Plan Mensual (Contratación Recurrente)" else 0.0
        total = subtotal * (1 - descuento)

    with col_summary:
        st.markdown(f"""
        <div class="summary-box">
            <h3 style="color:#D97706 !important; margin-top:0px;">📋 Tu Presupuesto KMG</h3>
            <p style="color:#334155;"><b>Servicio contratado:</b> {tipo_servicio}</p>
            <p style="color:#334155;"><b>Modalidad elegida:</b> {modalidad}</p>
            <p style="color:#334155;"><b>Duración de jornada:</b> {frecuencia_texto}</p>
            <p style="color:#334155;"><b>Costo base:</b> $U {precio_actual} / hora</p>
            <hr style="border-color:#D97706;">
            <h2 style="color:#0284C7 !important; margin-bottom:0px; font-size:28px;">Total Estimado: $U {total:,.2f}</h2>
        </div>
        """, unsafe_allow_html=True)
        
        if descuento > 0:
            st.caption("✨ ¡Incluye un 15% de descuento exclusivo por contratación Mensual!")
        
        st.write("")
        nombre = st.text_input("Tu Nombre o Empresa:")
        telefono = st.text_input("Tu Teléfono de Contacto (WhatsApp):")
        
        if st.button("Reservar Jornada por WhatsApp"):
            if nombre and telefono:
                # Estructura de mensaje directo para tu WhatsApp 091295245
                mensaje_whatsapp = f"Hola KMG Elizabeth! Me interesa contratar el servicio de *{tipo_servicio}*. Modalidad: {modalidad} ({frecuencia_texto}). El presupuesto estimado de la web es de $U {total:,.2f}. Mi nombre es {nombre} y mi teléfono es {telefono}."
                link_wa = f"https://wa.me{mensaje_whatsapp.replace(' ', '%20')}"
                st.success("¡Cotización generada correctamente!")
                st.markdown(f"[➡️ Presiona aquí para agendar directamente en nuestro WhatsApp]({link_wa})")
            else:
                st.error("Por favor, completa tu nombre y teléfono para enviar la orden.")

# ==========================================
# PESTAÑA 2: NUESTROS SERVICIOS
# ==========================================
with tab2:
    st.markdown("<h3 style='color:#D97706 !important; margin-top:0px;'>⚡ Soluciones Profesionales KMG Elizabeth</h3>", unsafe_allow_html=True)
    st.write("Servicios con un alto estándar de confianza, pulcritud y detalle.")
    st.write("")
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.markdown('<div class="feature-box"><h3>🏠 Casas y Hogares</h3><p>Mantenimiento profundo, orden y limpieza de espacios residenciales con absoluta discreción y confianza.</p></div>', unsafe_allow_html=True)
        st.markdown('<div class="feature-box"><h3>🏥 Clínicas y Consultorios</h3><p>Sanitización rigurosa bajo estrictas normas de higiene para la seguridad de entornos médicos.</p></div>', unsafe_allow_html=True)

    with col2:
        st.markdown('<div class="feature-box"><h3>🏢 Oficinas Corporativas</h3><p>Ambientes laborales impecables que potencian la productividad. Flexibilidad total de horarios.</p></div>', unsafe_allow_html=True)
        st.markdown('<div class="feature-box"><h3>🏗️ Fines de Obra</h3><p>Eliminación profunda de restos de obra, pintura y polvo fino para dejar la propiedad lista para habitar.</p></div>', unsafe_allow_html=True)

    with col3:
        st.markdown('<div class="feature-box"><h3>🛍️ Locales Comerciales</h3><p>Limpieza de vidrieras, salones y showrooms para que tu negocio destaque frente a tus clientes.</p></div>', unsafe_allow_html=True)
        st.markdown('<div class="feature-box"><h3>🏢 Edificios y Complejos</h3><p>Mantenimiento óptimo de palieres, pasillos, escaleras y áreas comunes de copropiedades.</p></div>', unsafe_allow_html=True)

# ==========================================
# PESTAÑA 3: CONTACTO DIRECTO
# ==========================================
with tab3:
    st.markdown("<h3 style='color:#D97706 !important; margin-top:0px;'>📞 Vías de Comunicación</h3>", unsafe_allow_html=True)
    st.write("Atención personalizada e inmediata para presupuestos especiales.")
    st.write("")
    
    c_info, c_form = st.columns(2)
    
    with c_info:
        st.markdown(f"""
        <div style="background-color:#FFFFFF; padding:20px; border-radius:12px; border-left:6px solid #D97706; box-shadow: 0 4px 6px -1px rgba(0,0,0,0.05);">
            <h4 style="color:#0284C7 !important; margin-top:0px; font-weight:bold;">📍 Canales Oficiales</h4>
            <p style="color:#334155;"><b>Empresa:</b> KMG Elizabeth - Limpieza</p>
            <p style="color:#334155;"><b>Administración Directa:</b> <a href="https://wa.me" style="color:#0284C7; font-weight:bold;">091 295 245</a></p>
            <p style="color:#334155;"><b>Área de Cobertura:</b> Montevideo y alrededores.</p>
            <p style="color:#334155;"><b>Horario administrativo:</b> Lunes a Sábados de 08:00 a 18:00 hs.</p>
        </div>
        """, unsafe_allow_html=True)
        
    with c_form:
        st.write("**¿Tienes un requerimiento especial? Déjanos un aviso:**")
        c_nombre = st.text_input("Nombre completo u Organización:")
        c_msg = st.text_area("Cuéntanos qué necesitas resolver:")
        
        if st.button("Enviar Mensaje Express"):
            if c_nombre and c_msg:
