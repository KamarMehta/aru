from langgraph.graph import StateGraph, END
from state import PipelineState
from nodes.diagram_node import diagram_node
from nodes.code_node import code_node
from nodes.unit_test_node import unit_test_node
from nodes.integration_node import integration_node

def build_graph():
    workflow = StateGraph(PipelineState)

    workflow.add_node("diagram", diagram_node)
    workflow.add_node("code", code_node)
    workflow.add_node("unit_tests", unit_test_node)
    workflow.add_node("integration", integration_node)

    workflow.set_entry_point("diagram")
    workflow.add_edge("diagram", "code")
    workflow.add_edge("code", "unit_tests")
    workflow.add_edge("unit_tests", "integration")
    workflow.add_edge("integration", END)

    return workflow.compile()
