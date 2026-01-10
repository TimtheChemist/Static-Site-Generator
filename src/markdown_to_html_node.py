from blocks_functions import BlockType, block_to_block_type, markdown_to_blocks
from htmlnode import HTMLNode, ParentNode
from text_node_to_html_node import text_node_to_html_node
from split_nodes_functions import text_to_textnodes
from textnode import TextType, TextNode



def markdown_to_html_node(markdown_doc):
    blocks = markdown_to_blocks(markdown_doc)
    list_of_nodes = []

    for block in blocks:
        block_type = block_to_block_type(block)

        if block_type == BlockType.ORDERED_LIST:
            new_html_node = ParentNode("ol", ol_block_to_children_nodes(block))
            list_of_nodes.append(new_html_node)

        elif block_type == BlockType.UNORDERED_LIST:
            new_html_node = ParentNode("ul", ul_block_to_children_nodes(block))
            list_of_nodes.append(new_html_node)

        elif block_type == BlockType.QUOTE:
            new_html_node = ParentNode("blockquote", quote_block_to_children_nodes(block))
            list_of_nodes.append(new_html_node)

        elif block_type == BlockType.PARAGRAPH:
            new_block_list = block.split("\n")
            new_block = " ".join(new_block_list)
            new_html_node = ParentNode("p", text_to_children(new_block))
            list_of_nodes.append(new_html_node)

        elif block_type == BlockType.HEADING:
            count = 0
            for ch in block:
                if ch == "#":
                    count += 1
                else:
                    break

            inner_text = block[count:].lstrip()
            children = text_to_children(inner_text)

            new_html_node = ParentNode(f"h{count}", children)
            list_of_nodes.append(new_html_node)

        elif block_type == BlockType.CODE:
            new_block_list = block.split("\n")
            trimmed_block_list = new_block_list[1:-1]
            new_block = "\n".join(trimmed_block_list) + "\n"

            new_text_node = TextNode(new_block, TextType.CODE)
            new_html_node = text_node_to_html_node(new_text_node)
            new_html_node = ParentNode("pre" , [new_html_node])
            list_of_nodes.append(new_html_node)

    parent_html_node = ParentNode("div", list_of_nodes)
    return parent_html_node



def ol_block_to_children_nodes(block):
    li_nodes = []
    lines = block.split("\n")
    for line in lines:
        line = line.strip()
        if not line:
            continue

        line_index = line.find(". ") + 2
        item_text = line[line_index:]

        # parse inline markdown into children nodes
        children = text_to_children(item_text)

        li_nodes.append(ParentNode("li", children))

    return li_nodes


def ul_block_to_children_nodes(block):
    li_nodes = []
    lines = block.split("\n")
    for line in lines:
        line = line.strip()
        if not line:
            continue

        line_index = line.find("-") + 2
        item_text = line[line_index:]

        # parse inline markdown into children nodes
        children = text_to_children(item_text)

        li_nodes.append(ParentNode("li", children))

    return li_nodes


def quote_block_to_children_nodes(block):
    quote_nodes = []
    lines = block.split("\n")
    for line in lines:
        line = line.strip()
        if not line:
            continue

        item_text = line[1:].lstrip()

        # parse inline markdown into children nodes
        children = text_to_children(item_text)

        quote_nodes.extend(children)

    return quote_nodes



def text_to_children(text):
    # 1. use your inline parsing function to get TextNodes
    text_nodes = text_to_textnodes(text)

    # 2. convert each TextNode to an HTMLNode
    children = []
    for tn in text_nodes:
        children.append(text_node_to_html_node(tn))

    return children