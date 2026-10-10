# main.py
from nodes import nodes
from network import SemanticNetwork, load_data
from render import render_graph


def main():

    nodes_data, triplets = load_data("nodes.py", "triplets.csv")
    net = SemanticNetwork(nodes_data, triplets)
    net.build()
    print(f"\nЗагружено узлов: {len(nodes_data)}")
    print(f"Загружено триплетов: {len(triplets)}")

    for msg in net.validate():
        print(f"  {msg}")

    print("\nЗапрос 1")
    print("neighbors('inst_turkey', 'подходит для')")
    for rel, obj in net.neighbors("inst_turkey", "подходит для"):
        print(f"  {nodes_data['inst_turkey']['name']} --{rel}--> {nodes_data[obj]['name']}")

    print("\nЗапрос 2")
    print("ancestors('inst_turkey')")
    result = net.ancestors("inst_turkey")
    if result:
        for obj in result:
            print(f"  → {nodes_data[obj]['name']}")
    else:
        print("  (пусто)")

    print("\nЗапрос 3")
    print("find_path('inst_egypt', 'inst_beach')")
    result = net.find_path("inst_egypt", "inst_beach")
    if result:
        print(f"  {' '.join(result)}")
    else:
        print("  Путь не найден")

    print("\nТесты")
    tests = [
        ("T-01", net.neighbors("inst_turkey", "подходит для"), "beach, culture"),
        ("T-02", net.ancestors("inst_turkey"), "cls_beach_country, cls_country"),
        ("T-03", net.find_path("inst_egypt", "inst_beach"), "egypt → beach"),
        ("T-04", net.find_path("inst_nature", "inst_thailand"), "None (путь не найден)"),
        ("T-05", net.validate(), "OK: ошибок не найдено"),
    ]
    for tid, fact, expected in tests:
        print(f"  {tid}: факт = {fact}")
        print(f"        ожидание = {expected}")

    print("\nВыделение пути")
    print(net.highlight_path("inst_egypt", "inst_beach"))

    print("\nЭкспорт pdf")
    print(f"  Файл сохранён: {net.export_rdf('network.ttl')}")

    print("\nКласификация стран")
    for c in ["inst_turkey", "inst_china", "inst_vietnam", "inst_egypt", "inst_thailand"]:
        print(f"  {nodes_data[c]['name']}: {net.classify_country(c)}")

if __name__ == "__main__":
    main()