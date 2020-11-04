from jinja2 import FileSystemLoader

file_loader = FileSystemLoader("templates")

print(f"templates: {file_loader.list_templates()}")


from jinja2 import Environment  # noqa

env = Environment(loader=file_loader)

hello = env.get_template("montemplate.j2")
name = "colin"

print(hello.render(name=name))
