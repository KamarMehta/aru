from typing import TypedDict

class PipelineState(TypedDict):
    diagram_text: str
    technical_doc: str
    code: str
    unit_tests: str
    integration_tests: str
