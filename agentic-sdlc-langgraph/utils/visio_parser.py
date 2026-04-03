# Full graph parser
import zipfile
from lxml import etree
import networkx as nx

def parse_vsdx_to_graph(file_path):
    nodes = {}
    edges = []

    with zipfile.ZipFile(file_path, 'r') as z:
        page_files = [f for f in z.namelist() if f.startswith("visio/pages/") and f.endswith(".xml")]

        for file in page_files:
            root = etree.fromstring(z.read(file))

            for shape in root.findall(".//Shape"):
                shape_id = shape.get("ID")
                name = shape.get("NameU", "")
                text_elem = shape.find(".//Text")
                text = text_elem.text.strip() if text_elem is not None and text_elem.text else ""

                nodes[shape_id] = {"id": shape_id, "text": text, "type": "process"}

            for connect in root.findall(".//Connect"):
                from_id = connect.get("FromSheet")
                to_id = connect.get("ToSheet")
                if from_id and to_id:
                    edges.append({"from": from_id, "to": to_id})

    G = nx.DiGraph()
    for n in nodes.values():
        G.add_node(n["id"], **n)
    for e in edges:
        G.add_edge(e["from"], e["to"])

    return {"nodes": list(nodes.values()), "edges": edges}
