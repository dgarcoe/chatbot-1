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

    response = f"Sanxenxo es conocido por sus hermosas playas. Aquí tienes tres de las más destacadas:\n"+"Playa de Silgar: Esta es la playa más famosa y concurrida de Sanxenxo. Situada en el centro de la ciudad, es ideal para quienes buscan comodidad y servicios cercanos.\n"+"Playa de Areas: Un poco más tranquila que Silgar, esta playa ofrece aguas cristalinas y arena fina. Es perfecta para relajarse y disfrutar de un entorno más natural.\n"+"Playa de Montalvo: Ubicada en un entorno más rural, esta playa es conocida por su belleza natural y su ambiente más sereno. Es ideal para quienes buscan escapar del bullicio."
    # Display assistant response in chat message container
    with st.chat_message("assistant"):
        st.audio("./resources/cat.mp3",format="audio/mpeg",loop=True)
        st.markdown(response)
    # Add assistant response to chat history
    st.session_state.messages.append({"role": "assistant", "content": response})