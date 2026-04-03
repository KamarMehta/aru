from graph import build_graph

def run_pipeline(graph_data):
    app = build_graph()
    return app.invoke({
        "diagram_text": str(graph_data),
        "technical_doc": "",
        "code": "",
        "unit_tests": "",
        "integration_tests": ""
    })
