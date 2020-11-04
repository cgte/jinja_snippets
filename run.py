from jinja2 import FileSystemLoader

file_loader = FileSystemLoader("templates")

print(f"templates: {file_loader.list_templates()}")
