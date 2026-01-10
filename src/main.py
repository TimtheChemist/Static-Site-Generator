from textnode import TextType, TextNode
from pathlib import Path
import sys
sys.path.insert(0, str(Path(__file__).parent.parent))
from static.copy_static import copy_static
from generate_page import generate_page

def main():

    copy_static("static", "public")

    generate_page("content/index.md", "template.html", "public/index.html")


main()