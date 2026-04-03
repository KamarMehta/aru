from utils.llm import call_llm

def code_node(state):
    code = call_llm("Generate C# code", state["technical_doc"])
    return {**state, "code": code}
