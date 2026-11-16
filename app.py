
import streamlit as st

from search_documents import search_documents
from generate_answer import generate_answer


st.title("GenAI Document Assistant")

# Store conversation history
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display previous messages
for message in st.session_state.messages:

    with st.chat_message(message["role"]):
        st.write(message["content"])


# Chat input
question = st.chat_input("Ask a question about your PDF")

if question:

    # Display and store user question
    st.session_state.messages.append({
        "role": "user",
        "content": question
    })

    with st.chat_message("user"):
        st.write(question)

    # Generate answer
    with st.chat_message("assistant"):

        with st.spinner("Searching and generating answer..."):

            results = search_documents(question)

            if not results["documents"][0]:
                answer = "No relevant documents found."

            elif results["distances"][0][0] > 0.8:
                answer = "I don't know based on the provided document."

            else:
                context = "\n\n".join(results["documents"][0])
                
                history = st.session_state.messages[:-1]

                answer = generate_answer(question, context, history)

        st.write(answer)

    # Store assistant answer
    st.session_state.messages.append({
        "role": "assistant",
        "content": answer
    })
