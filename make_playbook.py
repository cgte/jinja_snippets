from jinja2 import FileSystemLoader

file_loader = FileSystemLoader("templates")

print(f"templates: {file_loader.list_templates()}")


from jinja2 import Environment  # noqa

env = Environment(loader=file_loader)

hosts_template = env.get_template("tagged_hosts.j2")
groups = {"group1": ["host1", "host2"], "group2": ["host2", "host3"]}

print(hosts_template.render(groups=groups))
