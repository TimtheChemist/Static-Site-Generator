from textnode import TextType, TextNode
from pathlib import Path
import sys
sys.path.insert(0, str(Path(__file__).parent.parent))
from static.copy_static import copy_static
from generate_page import generate_page, generate_pages_recursive
import os

def main():

    copy_static("static", "docs")

    base_path = sys.argv[1] if len(sys.argv) > 1 else "/"
    generate_pages_recursive("content", "template.html", "docs", base_path)



main()