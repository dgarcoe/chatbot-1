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

    response = f"Test"
    # Display assistant response in chat message container
    with st.chat_message("assistant"):
        st.audio()
        st.markdown(response)
    # Add assistant response to chat history
    st.session_state.messages.append({"role": "assistant", "content": response})