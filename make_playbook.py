from jinja2 import FileSystemLoader

file_loader = FileSystemLoader("templates")

print(f"templates: {file_loader.list_templates()}")


from jinja2 import Environment  # noqa

env = Environment(loader=file_loader)


hosts_template = env.get_template("tagged_hosts.j2")
groups = {"group1": ["host1", "host2"], "group2": ["host2", "host3"]}


print(hosts_template.render(groups=groups))

import random  # noqa
import string  # noqa

tags = ["dev", "prepod", "integ", "valid", "prod"]


class DummyNode:
    def __init__(self):
        self.tags = random.choices(tags, k=random.randint(1, len(tags)))
        self.name = (
            "".join(random.choices(string.ascii_lowercase, k=10))
            + "_"
            + "-".join(self.tags)
        )

    pass


nodes = [DummyNode() for _ in range(10)]

import operator  # noqa

by_tags = operator.attrgetter("tags")

from collections import defaultdict  # noqa

groups = defaultdict(set)

for node in nodes:
    for tag in node.tags:
        groups[tag].add(node.name)

print("With many hosts")

print(hosts_template.render(groups=groups))
