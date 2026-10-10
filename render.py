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


def render_graph_with_path(network, source, target, filename="semantic_network_path"):
    """Граф с выделенным путём."""
    dot = Digraph(comment="Семантическая сеть с выделенным путём")
    dot.attr(rankdir="LR", encoding="utf-8")

    path = network.find_path(source, target)
    path_nodes = set()
    if path:
        for item in path:
            if not item.startswith("--") and not item.startswith("<--"):
                path_nodes.add(item)

    colors = {"class": "lightblue", "instance": "lightgreen", "value": "lightyellow"}

    for node_id, node in network.nodes.items():
        if node_id in path_nodes:
            dot.node(node_id, node["name"], style="filled",
                     fillcolor="orange", penwidth="3")
        else:
            dot.node(node_id, node["name"], style="filled",
                     fillcolor=colors.get(node["type"], "white"))

    for t in network.triplets:
        if t["subject"] in path_nodes and t["object"] in path_nodes:
            dot.edge(t["subject"], t["object"], label=t["relation"],
                     color="red", penwidth="2")
        else:
            dot.edge(t["subject"], t["object"], label=t["relation"])

    dot.render(filename, format="png", cleanup=True)
    return f"{filename}.png"