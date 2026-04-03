from utils.llm import call_llm

def integration_node(state):
    integration = call_llm("Generate integration tests", state["code"] + "\n" + state["unit_tests"])
    return {**state, "integration_tests": integration}
