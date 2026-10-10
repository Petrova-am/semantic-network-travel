# render.py
from graphviz import Digraph


def render_graph(network, filename="semantic_network"):
    dot = Digraph(comment="Семантическая сеть: страны для путешествий")
    dot.attr(rankdir="LR", encoding="utf-8")
    dot.attr("node", fontname="Arial")
    dot.attr("edge", fontname="Arial")
    dot.attr(size="20,20")
    dot.attr(dpi="150")

    colors = {
        "class": "lightblue",
        "instance": "lightgreen",
        "value": "lightyellow",
    }

    for node_id, node in network.nodes.items():
        dot.node(
            node_id,
            node["name"],
            style="filled",
            fillcolor=colors.get(node["type"], "white"),
        )

    for t in network.triplets:
        dot.edge(t["subject"], t["object"], label=t["relation"])

    dot.render(filename, format="png", cleanup=True)
    return f"{filename}.png"