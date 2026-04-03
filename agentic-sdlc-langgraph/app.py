import streamlit as st
from utils.visio_parser import parse_vsdx_to_graph
from main import run_pipeline
import os

st.title("LangGraph SDLC Generator")

uploaded_file = st.file_uploader("Upload Visio (.vsdx)", type=["vsdx"])

if uploaded_file:
    temp_path = f"temp_{uploaded_file.name}"
    with open(temp_path, "wb") as f:
        f.write(uploaded_file.read())

    if st.button("Run Pipeline"):
        graph_data = parse_vsdx_to_graph(temp_path)
        result = run_pipeline(graph_data)

        st.write(result)

    os.remove(temp_path)
