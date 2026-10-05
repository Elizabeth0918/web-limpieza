import streamlit as st

# Configuración de la página con el nombre de tu marca oficial
st.set_page_config(page_title="KMG Elizabeth - Servicio Independiente de Limpieza", page_icon="✨", layout="wide")

# Estilos CSS con la paleta exacta: Blanco, Celeste (#38BDF8) y Detalles Dorados (#EAB308)
st.markdown("""
    <style>
    /* Fondo general oscuro elegante para resaltar los colores del logo */
    .stApp { background-color: #0F172A; color: #FFFFFF; }
    
    .brand-title { font-size: 55px !important; font-weight: 900; color: #38BDF8; text-align: center; margin-bottom: 0px; letter-spacing: 2px; }
    .brand-subtitle { font-size: 26px !important; font-weight: bold; color: #EAB308; text-align: center; margin-bottom: 5px; font-style: italic; }
    .main-title { font-size: 32px !important; font-weight: normal; color: #FFFFFF; text-align: center; margin-bottom: 25px; }
    
    /* Cajas de servicios en azul oscuro con bordes celestes y dorados */
    .feature-box { padding: 22px; border-radius: 12px; background-color: #1E293B; margin-bottom: 20px; border-left: 5px solid #38BDF8; border-top: 1px solid #EAB308; min-height: 160px; box-shadow: 0 4px 6px rgba(0,0,0,0.2); }
    .feature-box h3 { color: #38BDF8 !important; margin-top: 0px; }
    .feature-box p { color: #E2E8F0 !important; }
    
    /* Textos de títulos en pestañas y formularios */
    h1, h2, h3, .stSelectbox label, .stRadio label, .stNumberInput label, .stTextInput label, .stTextArea label { color: #38BDF8 !important; font-weight: bold; }
    p, span, div { color: #FFFFFF; }
    
    /* Estilo del contenedor del resumen */
    .summary-box { background-color: #1E293B; padding: 25px; border-radius: 12px; border: 2px solid #EAB308; }
    </style>
""", unsafe_allow_html=True)

# --- HEADER / HERO SECTION CON TU IDENTIDAD ---
st.markdown('<p class="brand-title">✨ KMG ✨</p>', unsafe_allow_html=True)
st.markdown('<p class="brand-subtitle">Elizabeth</p>', unsafe_allow_html=True)
st.markdown('<p class="main-title">LIMPIEZA · SERVICIO INDEPENDIENTE</p>', unsafe_allow_html=True)

# --- CONFIGURACIÓN DE PESTAÑAS (NAVEGACIÓN) ---
tab1, tab2, tab3 = st.tabs(["🧮 Cotizador de Jornadas", "⚡ Nuestros Servicios", "📞 Contacto Directo"])

# ==========================================
# PESTAÑA 1: COTIZADOR AUTOMATIZADO
# ==========================================
with tab1:
    st.markdown("<h2 style='color:#EAB308 !important;'>🧮 Calcula tu Presupuesto al Instante</h2>", unsafe_allow_html=True)
    st.write("Selecciona el tipo de servicio y las horas requeridas para obtener un estimado detallado.")
    
    col_form, col_summary = st.columns(2)

    with col_form:
        tipo_servicio = st.selectbox(
            "1. Selecciona el tipo de servicio profesional:", 
            ["Limpieza de Casas", "Limpieza de Edificios", "Limpieza de Oficinas", "Limpieza de Locales Comerciales", "Limpieza de Clínicas", "Limpieza de Fines de Obra"]
        )
        
        modalidad = st.radio("2. Modalidad de contratación:", ["Por Hora (Servicio Puntual)", "Plan Mensual (Contratación Recurrente)"])
        
        if modalidad == "Por Hora (Servicio Puntual)":
            horas_opcion = st.selectbox("3. ¿Cuántas horas necesitas para la jornada?", [4, 6, 8])
            horas = horas_opcion
            frecuencia_texto = f"Jornada puntual de {horas} horas"
        else:
            horas_semana = st.selectbox("3. ¿Cuántas horas de limpieza por semana necesitas?", [4, 6, 8])
            frecuencia_texto = f"Plan Mensual ({horas_semana} hs/semana)"
            horas = horas_semana * 4

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
        st.markdown(f"""
        <div class="summary-box">
            <h3 style="color:#EAB308 !important; margin-top:0px;">📋 Resumen de Cotización KMG</h3>
            <p><b>Servicio:</b> {tipo_servicio}</p>
            <p><b>Modalidad:</b> {modalidad}</p>
            <p><b>Tiempo Estipulado:</b> {frecuencia_texto}</p>
            <p><b>Tarifa Base:</b> $U {precio_actual} / hora</p>
            <hr style="border-color:#EAB308;">
            <h2 style="color:#38BDF8 !important; margin-bottom:0px;">Total Estimado: $U {total:,.2f}</h2>
        </div>
        """, unsafe_allow_html=True)
        
        if descuento > 0:
            st.caption("✨ ¡Se aplicó un 15% de descuento exclusivo por contratación Mensual!")
        
        st.write("")
        nombre = st.text_input("Tu Nombre / Empresa:")
        telefono = st.text_input("Tu Teléfono de Contacto:")
        
        if st.button("Reservar Jornada por WhatsApp", type="primary"):
            if nombre and telefono:
                mensaje_whatsapp = f"Hola KMG Elizabeth! Me interesa contratar el servicio de *{tipo_servicio}*. Modalidad: {modalidad} ({frecuencia_texto}). El presupuesto estimado de la web es de $U {total:,.2f}. Mi nombre es {nombre} y mi teléfono es {telefono}."
                link_wa = f"https://wa.me{mensaje_whatsapp.replace(' ', '%20')}"
                st.success("¡Cotización generada con éxito!")
                st.markdown(f"[➡️ Haz clic aquí para enviar la orden al WhatsApp de KMG Elizabeth]({link_wa})")
            else:
                st.error("Por favor, completa los campos de nombre y teléfono antes de enviar la reserva.")

# ==========================================
# PESTAÑA 2: NUESTROS SERVICIOS
# ==========================================
with tab2:
    st.markdown("<h2 style='color:#EAB308 !important;'>⚡ Especialidades de Limpieza KMG Elizabeth</h2>", unsafe_allow_html=True)
    st.write("Soluciones profesionales independientes con un alto estándar de confianza y pulcritud.")
    st.write("")
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.markdown('<div class="feature-box"><h3>🏠 Casas y Hogares</h3><p>Mantenimiento profundo y orden de espacios residenciales con absoluta discreción y cuidado.</p></div>', unsafe_allow_html=True)
        st.markdown('<div class="feature-box"><h3>🏥 Clínicas y Consultorios</h3><p>Sanitización rigurosa bajo estrictas normas de higiene para la seguridad de tus pacientes.</p></div>', unsafe_allow_html=True)

    with col2:
        st.markdown('<div class="feature-box"><h3>🏢 Oficinas Corporativas</h3><p>Ambientes de trabajo limpios que impulsan la productividad. Flexibilidad de horarios.</p></div>', unsafe_allow_html=True)
        st.markdown('<div class="feature-box"><h3>🏗️ Fines de Obra</h3><p>Eliminación impecable de restos de obra, pintura y polvo fino para dejar la propiedad lista para habitar.</p></div>', unsafe_allow_html=True)

    with col3:
        st.markdown('<div class="feature-box"><h3>🛍️ Locales Comerciales</h3><p>Limpieza de vidrieras, pisos y salones para garantizar una excelente primera impresión a tus clientes.</p></div>', unsafe_allow_html=True)
        st.markdown('<div class="feature-box"><h3>🏢 Edificios y Complejos</h3><p>Mantenimiento óptimo de palieres, pasillos, escaleras y áreas comunes de copropiedades.</p></div>', unsafe_allow_html=True)

# ==========================================
# PESTAÑA 3: CONTACTO Y UBICACIÓN
# ==========================================
with tab3:
    st.markdown("<h2 style='color:#EAB308 !important;'>📞 Contacto y Detalles de Servicio</h2>", unsafe_allow_html=True)
    st.write("Comunícate directamente con la administración del servicio independiente.")
    st.write("")
    
    c_info, c_form = st.columns(2)
    
    with c_info:
        st.markdown(f"""
        <div style="background-color:#1E293B; padding:20px; border-radius:12px; border-left:5px solid #EAB308;">
            <h3 style="color:#38BDF8 !important; margin-top:0px;">📍 Información de Atención</h3>
            <p><b>Empresa:</b> KMG Elizabeth - Limpieza</p>
            <p><b>Servicio:</b> Profesional Independiente</p>
            <p><b>WhatsApp de Reservas:</b> <a href="https://wa.me" style="color:#38BDF8;">091 295 245</a></p>
            <p><b>Cobertura:</b> Montevideo y zonas de influencia.</p>
            <p><b>Horarios:</b> Lunes a Sábados de 08:00 a 18:00 hs.</p>
        </div>
        """, unsafe_allow_html=True)
        
    with c_form:
        st.write("**¿Tienes requerimientos especiales?**")
        c_nombre = st.text_input("Nombre Completo:")
        c_msg = st.text_area("Cuéntanos qué necesitas limpiar:")
        
        if st.button("Enviar Consulta Express"):
            if c_nombre and c_msg:
                st.success(f"¡Muchas gracias {c_nombre}! Tu consulta ha sido registrada. Nos comunicaremos contigo a la brevedad.")
            else:
                st.error("Por favor completa tu nombre y el mensaje para poder ayudarte.")

st.write("---")

# --- PIE DE PÁGINA DE ALTA CONFIANZA COMPLETAMENTE REESTRUCTURADO SIN ERRORES ---
st.markdown("""
<div style="display: flex; justify-content: space-between; gap: 20px; margin-top: 20px;">
    <div style="flex: 1;">
        <p style="color:#38BDF8; font-weight: bold; margin-bottom: 5px;">🔒 Garantía de Confianza Elizabeth</p>
        <p style="font-size:14px; color:#94A3B8; margin-top: 0px;">Filtros rigurosos de seguridad y personal totalmente calificado para tu tranquilidad.</p>
    </div>
    <div style="flex: 1;">
        <p style="color:#EAB308; font-weight: bold; margin-bottom: 5px;">⭐ Compromiso de Calidad 100%</p>
