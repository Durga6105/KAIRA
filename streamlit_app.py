"""
KAIRA

Enterprise Knowledge Graph &
Hybrid GraphRAG Platform
"""

from pathlib import Path

import requests
import streamlit as st

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

    st.markdown(
        """
Enterprise Knowledge Graph

Hybrid GraphRAG Platform
"""
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

    st.caption("KAIRA v1.0.0")

# ---------------------------------------------------
# Header
# ---------------------------------------------------

st.title("🧠 KAIRA")

st.markdown(
    """
### Enterprise Knowledge Graph & Hybrid GraphRAG Platform
"""
)

st.divider()

left, right = st.columns(
    [1, 2]
)

# ---------------------------------------------------
# Document Explorer
# ---------------------------------------------------

with left:

    st.subheader("📂 Enterprise Documents")

    structured_path = Path(
        "uploads/structured"
    )

    unstructured_path = Path(
        "uploads/unstructured"
    )

    files = []

    if structured_path.exists():

        for file in sorted(
            structured_path.glob("*")
        ):

            files.append(str(file))

    if unstructured_path.exists():

        for file in sorted(
            unstructured_path.glob("*")
        ):

            files.append(str(file))

    if files:

        selected_file = st.selectbox(

            "Select Document",

            files

        )

        if st.button(

            "🚀 Ingest Document",

            use_container_width=True

        ):

            with st.spinner(
                "Building Knowledge Graph..."
            ):

                try:

                    response = requests.post(

                        f"{API_URL}/ingestion/",

                        json={

                            "file_path": selected_file

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

    else:

        st.warning(
            "No documents found inside uploads folder."
        )

# ---------------------------------------------------
# Chat Section
# ---------------------------------------------------

with right:

    st.subheader("💬 Ask KAIRA")

    question = st.chat_input(
        "Ask anything about your enterprise..."
    )
# ---------------------------------------------------
# Conversation
# ---------------------------------------------------

st.divider()

st.subheader("📖 Conversation")

if len(st.session_state.messages) == 0:

    st.info(
        "Start a conversation with KAIRA."
    )

for message in st.session_state.messages:

    with st.chat_message(
        message["role"]
    ):

        st.markdown(
            message["content"]
        )

# ---------------------------------------------------
# Query API
# ---------------------------------------------------

if question:

    st.session_state.messages.append(

        {

            "role": "user",

            "content": question

        }

    )

    with st.chat_message("user"):

        st.markdown(question)

    with st.chat_message("assistant"):

        with st.spinner(
            "Thinking..."
        ):

            try:

                response = requests.post(

                    f"{API_URL}/query/",

                    json={

                        "question": question

                    }

                )

                if response.status_code == 200:

                    answer = response.json().get(

                        "answer",

                        "No answer returned."

                    )

                else:

                    answer = response.json().get(

                        "detail",

                        "Unknown error."

                    )

            except Exception as e:

                answer = str(e)

            st.markdown(answer)

    st.session_state.messages.append(

        {

            "role": "assistant",

            "content": answer

        }

    )
# ---------------------------------------------------
# Footer
# ---------------------------------------------------

st.divider()

col1, col2, col3 = st.columns(3)

with col1:

    st.caption(
        "🧠 KAIRA"
    )

with col2:

    st.caption(
        "Enterprise Knowledge Graph"
    )

with col3:

    st.caption(
        "Version 1.0.0"
    )
