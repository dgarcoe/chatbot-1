import streamlit as st
from openai import OpenAI

st.image("./resources/sendeiro-maxico-a-lanzada-im.jpg")

# Show title and description.
st.title("🏖️ Asistente Inteligente de Turismo de Sanxenxo")
st.write(
    "Soy tu asistente inteligente para responder consultas turísticas acerca del Concello de Sanxenxo."
)


# Create a session state variable to store the chat messages. This ensures that the
# messages persist across reruns.
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display the existing chat messages via `st.chat_message`.
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# Create a chat input field to allow the user to enter a message. This will display
# automatically at the bottom of the page.
if prompt := st.chat_input("¡Pregúntame cualquier duda que tengas!"):

    # Display user message in chat message container
    with st.chat_message("user"):
        st.markdown(prompt)
    # Add user message to chat history
    st.session_state.messages.append({"role": "user", "content": prompt})

    response="¡Hola!"
    audio="None"
    if "playa" in prompt:
        audio="playas"
        response = '''
        Sanxenxo es conocido por sus hermosas playas. Aquí tienes tres de las más destacadas:
        - Playa de Silgar: Esta es la playa más famosa y concurrida de Sanxenxo. Situada en el centro de la ciudad, es ideal para quienes buscan comodidad y servicios cercanos.
        - Playa de Areas: Un poco más tranquila que Silgar, esta playa ofrece aguas cristalinas y arena fina. Es perfecta para relajarse y disfrutar de un entorno más natural.
        - Playa de Montalvo: Ubicada en un entorno más rural, esta playa es conocida por su belleza natural y su ambiente más sereno. Es ideal para quienes buscan escapar del bullicio.'''
    elif "personajes" in prompt:
        audio="personajes"
        response='''
        Algunos personajes históricos de Sanxenxo incluyen:
        - Ramón Cabanillas Enríquez: Poeta gallego vinculado a Sanxenxo, fue una figura clave del renacimiento literario gallego, conocido por su obra de inspiración patriótica y social.
        - Luis Rocafort: Pintor gallego, su obra está relacionada con Sanxenxo y la región de Pontevedra. Su estilo se asocia con el paisaje y las costumbres de Galicia.
        Sanxenxo también se ha destacado por atraer a personajes de relevancia en la actualidad, como la familia real española y empresarios influyentes.
        '''
    elif ("comer" in prompt) or ("restaurantes" in prompt):
        audio="comer"
        response='''
        Aquí tienes tres sitios recomendados para comer en Sanxenxo, Galicia:
        - Restaurante Sabino: Ofrecen cocina gallega moderna con especial enfoque en pescados y mariscos frescos de la ría. Es conocido por su calidad y servicio.
        - A Taberna do Varadoiro: Un restaurante acogedor junto al puerto, con una excelente carta de mariscos y platos típicos gallegos. Ideal para disfrutar de vistas al mar mientras comes.
        - Restaurante O Barco – Ubicado en la playa de Silgar, es un sitio popular por sus vistas al mar y su variada oferta de platos de mariscos y pescados frescos. Además, tienen una buena selección de vinos gallegos.
        '''
    elif ("historia" in prompt) or ("sitios históricos" in prompt):
        audio="historia"
        response='''
        Aquí tienes tres sitios históricos interesantes para visitar en Sanxenxo:
        - Pazo de Quintáns: Una casa señorial del siglo XVII situada en Noalla, cerca de Sanxenxo. Es un edificio histórico rodeado de jardines, que refleja la arquitectura típica de los pazos gallegos.
        - Ermita de A Lanzada: Ubicada en la playa de A Lanzada, esta pequeña ermita data del siglo XII y es un lugar emblemático de la zona. Además de su valor histórico, es conocida por las leyendas y tradiciones vinculadas a la fertilidad.
        - Iglesia de San Xinés de Padriñán: Un templo del siglo XV que destaca por su arquitectura gótica, situado en el núcleo antiguo de Sanxenxo. Es una de las iglesias más antiguas de la zona.
        '''

    # Display assistant response in chat message container
    with st.chat_message("assistant"):
        match audio:
            case "playas":
                st.audio("./resources/playas.mp3",format="audio/mpeg",loop=False)
            #case "personajes":
                #st.audio("./resources/personajes.mp3",format="audio/mpeg",loop=False)
            #case "comer":
                #st.audio("./resources/personajes.mp3",format="audio/mpeg",loop=False)
            #case "historia":
                #st.audio("./resources/personajes.mp3",format="audio/mpeg",loop=False)
        st.markdown(response)
    # Add assistant response to chat history
    st.session_state.messages.append({"role": "assistant", "content": response})