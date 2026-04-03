from utils.llm import call_llm

def unit_test_node(state):
    tests = call_llm("Generate unit tests", state["code"])
    return {**state, "unit_tests": tests}
