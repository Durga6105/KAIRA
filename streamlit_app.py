"""
KAIRA

Enterprise Knowledge Graph &
Hybrid GraphRAG Platform
"""

import streamlit as st
import requests

# ---------------------------------------------------
# Configuration
# ---------------------------------------------------

st.set_page_config(
    page_title="KAIRA",
    page_icon="🧠",
    layout="wide",
    initial_sidebar_state="expanded"
)

API_URL = "http://127.0.0.1:8000"

# ---------------------------------------------------
# Session State
# ---------------------------------------------------

if "messages" not in st.session_state:
    st.session_state.messages = []

if "documents" not in st.session_state:
    st.session_state.documents = 0

if "nodes" not in st.session_state:
    st.session_state.nodes = 0

if "relationships" not in st.session_state:
    st.session_state.relationships = 0

if "chunks" not in st.session_state:
    st.session_state.chunks = 0
# ---------------------------------------------------
# Sidebar
# ---------------------------------------------------

with st.sidebar:

    st.title("🧠 KAIRA")

    st.caption(
        "Enterprise Knowledge Graph\n"
        "Hybrid GraphRAG Platform"
    )

    st.divider()

    st.subheader("System Status")

    st.success("🟢 FastAPI")

    st.success("🟢 Neo4j")

    st.success("🟢 ChromaDB")

    st.divider()

    st.subheader("Statistics")

    c1, c2 = st.columns(2)

    c1.metric(
        "Documents",
        st.session_state.documents
    )

    c2.metric(
        "Chunks",
        st.session_state.chunks
    )

    c1.metric(
        "Nodes",
        st.session_state.nodes
    )

    c2.metric(
        "Relations",
        st.session_state.relationships
    )

    st.divider()

    st.caption("KAIRA Version 1.0.0")
# ---------------------------------------------------
# Header
# ---------------------------------------------------

st.title("🧠 KAIRA")

st.markdown(
    "### Enterprise Knowledge Graph & Hybrid GraphRAG Platform"
)

st.divider()

left, right = st.columns(
    [1,2]
)
# ---------------------------------------------------
# Upload Section
# ---------------------------------------------------

with left:

    st.subheader("📂 Upload Document")

    uploaded_file = st.file_uploader(

        "Select a document",

        type=[
            "pdf",
            "docx",
            "pptx",
            "xlsx",
            "xls",
            "csv",
            "json",
            "txt"
        ]
    )

    upload = st.button(
        "📤 Upload",
        use_container_width=True
    )

    if upload:

        if uploaded_file is None:

            st.warning(
                "Please select a document."
            )

        else:

            file_path = (
                f"uploads/{uploaded_file.name}"
            )

            try:

                response = requests.post(

                    f"{API_URL}/ingestion/",

                    json={
                        "file_path": file_path
                    }

                )

                if response.status_code == 200:

                    data = response.json()

                    st.success(
                        data["message"]
                    )

                    st.session_state.documents += 1

                    st.session_state.nodes += data["nodes"]

                    st.session_state.relationships += data["relationships"]

                else:

                    st.error(
                        response.json()["detail"]
                    )

            except Exception as e:

                st.error(str(e))
with right:

    st.subheader("💬 Ask KAIRA")

    question = st.chat_input(
        "Ask anything about your enterprise..."
    )
st.divider()

st.subheader("Conversation")

for message in st.session_state.messages:

    with st.chat_message(
        message["role"]
    ):

        st.markdown(
            message["content"]
        )

if question:

    st.session_state.messages.append(
        {
            "role":"user",
            "content":question
        }
    )

    with st.chat_message("user"):

        st.markdown(question)

    response = "Waiting for FastAPI integration..."

    with st.chat_message("assistant"):

        st.markdown(response)

    st.session_state.messages.append(
        {
            "role":"assistant",
            "content":response
        }
    )