from utils.llm import call_llm

def diagram_node(state):
    doc = call_llm("Convert graph JSON into technical document", str(state["diagram_text"]))
    return {**state, "technical_doc": doc}
