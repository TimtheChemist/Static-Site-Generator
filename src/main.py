from textnode import TextType, TextNode
from pathlib import Path
import sys
sys.path.insert(0, str(Path(__file__).parent.parent))
from copy_static import copy_files_recursive, delete_directory_contents
from generate_page import generate_page, generate_pages_recursive
import os

dir_path_static = "./static"
dir_path_public = "./docs"
dir_path_content = "./content"
template_path = "./template.html"

def main():
    delete_directory_contents(dir_path_public)
    copy_files_recursive(dir_path_static, dir_path_public)

    base_path = sys.argv[1] if len(sys.argv) > 1 else "/"
    generate_pages_recursive(dir_path_content, template_path, dir_path_public, base_path)



main()