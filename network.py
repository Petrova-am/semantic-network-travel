import csv
from collections import defaultdict, deque


class SemanticNetwork:
    def __init__(self, nodes, triplets):
        self.nodes = nodes
        self.triplets = triplets
        self.adj = defaultdict(list)
        self.rev = defaultdict(list)

    def build(self):
        for t in self.triplets:
            self.adj[t["subject"]].append((t["relation"], t["object"]))
            self.rev[t["object"]].append((t["relation"], t["subject"]))

    def neighbors(self, node, relation=None):
        result = []
        for rel, obj in self.adj.get(node, []):
            if relation is None or rel == relation:
                result.append((rel, obj))
        return result

    def ancestors(self, node):

        result = []
        queue = deque([node])
        visited = {node}
        while queue:
            current = queue.popleft()
            for rel, obj in self.adj.get(current, []):
                if rel in ("подкласс", "экземпляр") and obj not in visited:
                    visited.add(obj)
                    result.append(obj)
                    queue.append(obj)
        return result

    def descendants(self, node):
        result = []
        queue = deque([node])
        visited = {node}
        while queue:
            current = queue.popleft()
            for rel, obj in self.rev.get(current, []):
                if rel in ("подкласс", "экземпляр") and obj not in visited:
                    visited.add(obj)
                    result.append(obj)
                    queue.append(obj)
        return result

    def find_path(self, source, target):
        """Семантическая цепочка между узлами (только вперёд по стрелкам)."""
        queue = deque([(source, [source])])
        visited = {source}
        while queue:
            current, path = queue.popleft()
            if current == target:
                return path
            for rel, obj in self.adj.get(current, []):
                if obj not in visited:
                    visited.add(obj)
                    queue.append((obj, path + [f"--{rel}-->", obj]))
        return None

    def validate(self):
        errors = []
        for t in self.triplets:
            if t["subject"] not in self.nodes:
                errors.append(f"Неизвестный субъект: {t['subject']}")
            if t["object"] not in self.nodes:
                errors.append(f"Неизвестный объект: {t['object']}")
        for node in self.nodes:
            if node in self.ancestors(node):
                errors.append(f"Цикл в иерархии: {node}")
        return errors if errors else ["OK: ошибок не найдено"]

    def highlight_path(self, source, target):
        path = self.find_path(source, target)
        if path:
            return f"Найден путь: {' '.join(path)}"
        return "Путь не найден"

    def export_rdf(self, filename="network.ttl"):
        with open(filename, "w", encoding="utf-8") as f:
            f.write("@prefix ex: <http://example.org/> .\n\n")
            for t in self.triplets:
                s = f"ex:{t['subject']}"
                p = f"ex:{t['relation'].replace(' ', '_')}"
                o = f"ex:{t['object']}"
                f.write(f"{s} {p} {o} .\n")
        return filename

    def classify_country(self, country):
        interests = [obj for rel, obj in self.neighbors(country, "подходит для")]
        country_name = self.nodes[country]["name"]

        if "inst_beach" in interests:
            return {
                "class": "Пляжная страна",
                "rule": "ЕСЛИ страна подходит для пляжа, ТО она — Пляжная страна",
                "reason": f"{country_name} имеет связь 'подходит для' → Пляж (K-11, K-13, K-14, K-15)",
                "facts": [f"{country_name} — подходит для → Пляж"],
            }
        if "inst_culture" in interests:
            return {
                "class": "Культурная страна",
                "rule": "ЕСЛИ страна подходит для культуры, ТО она — Культурная страна",
                "reason": f"{country_name} имеет связь 'подходит для' → Культура (K-11, K-12, K-14, K-15)",
                "facts": [f"{country_name} — подходит для → Культура"],
            }
        if "inst_exotic" in interests:
            return {
                "class": "Экзотическая страна",
                "rule": "ЕСЛИ страна подходит для экзотики, ТО она — Экзотическая страна",
                "reason": f"{country_name} имеет связь 'подходит для' → Экзотика (K-13)",
                "facts": [f"{country_name} — подходит для → Экзотика"],
            }
        return {
            "class": "Не классифицирована",
            "rule": "Нет связей 'подходит для'",
            "reason": f"У {country_name} нет связей 'подходит для' ни с одним интересом",
            "facts": [],
        }


def load_data(nodes_file, triplets_file):
    from nodes import nodes
    triplets = []
    with open(triplets_file, "r", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for row in reader:
            triplets.append(row)
    return nodes, triplets

