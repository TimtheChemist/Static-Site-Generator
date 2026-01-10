from textnode import TextType, TextNode
from pathlib import Path
import sys
sys.path.insert(0, str(Path(__file__).parent.parent))
from static.copy_static import copy_static

def main():
    new_object = TextNode("Placeholder text", TextType.BOLD)
    print(new_object)
    copy_static("/home/timot/workspace/github.com/Static-Site-Generator/static","/home/timot/workspace/github.com/Static-Site-Generator/public")


main()