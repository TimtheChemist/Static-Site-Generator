from markdown_to_html_node import markdown_to_html_node
import os

def extract_title(markdown):
    """Extract the title from a markdown string."""
    lines = markdown.split('\n')
    for line in lines:
        if line.startswith('# '):
            return line[2:].strip()
    raise ValueError("No title found in markdown.")


def generate_page(from_path, template_path, dest_path, base_path):
    print(f"Generating page from {from_path} to {dest_path} using {template_path}")

    with open(from_path,"r") as f:
        markdown_content = f.read()
    with open(template_path,"r") as f:
        template_content = f.read()

    page_title = extract_title(markdown_content)
    html_content = markdown_to_html_node(markdown_content).to_html()

    template_content = template_content.replace("{{ Title }}", page_title)
    template_content = template_content.replace("{{ Content }}", html_content)
    if base_path.endswith("/"):
        base_path = base_path[:-1]
    template_content = template_content.replace('href="/', f'href="{base_path}/')
    template_content = template_content.replace('src="/', f'src="{base_path}/')

    new_directory = os.path.dirname(dest_path)
    if not os.path.exists(new_directory):
        os.makedirs(new_directory)

    with open(dest_path, "w") as f:
        f.write(template_content)
        print(f"Page generated at {dest_path}")


def generate_pages_recursive(content_dir, template_path, public_dir, base_path):
    for root, dirs, files in os.walk(content_dir):
        for file in files:
            if file.endswith(".md"):
                from_path = os.path.join(root, file)
                relative_path = os.path.relpath(from_path, content_dir)
                dest_path = os.path.join(public_dir, relative_path[:-3] + ".html")
                generate_page(from_path, template_path, dest_path, base_path)