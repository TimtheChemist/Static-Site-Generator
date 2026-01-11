from textnode import TextType, TextNode
from pathlib import Path
import sys
sys.path.insert(0, str(Path(__file__).parent.parent))
from static.copy_static import copy_files_recursive
from generate_page import generate_page, generate_pages_recursive
import os

dir_path_public = "docs"

def main():
    copy_files_recursive("static", dir_path_public)

    base_path = sys.argv[1] if len(sys.argv) > 1 else "/"
    generate_pages_recursive("content", "template.html", dir_path_public, base_path)



main()