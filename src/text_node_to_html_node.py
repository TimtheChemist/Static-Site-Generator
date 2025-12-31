from htmlnode import HTMLNode, LeafNode, ParentNode
from textnode import TextType, TextNode


def text_node_to_html_node(text_node):

    if text_node.text_type == TextType.TEXT:
        leaf_node_object = LeafNode(None, text_node.text)
        return leaf_node_object

    if text_node.text_type == TextType.BOLD:
        leaf_node_object = LeafNode("b", text_node.text)
        return leaf_node_object

    if text_node.text_type == TextType.ITALIC:
        leaf_node_object = LeafNode("i", text_node.text)
        return leaf_node_object

    if text_node.text_type == TextType.CODE:
        leaf_node_object = LeafNode("code", text_node.text)
        return leaf_node_object

    if text_node.text_type == TextType.LINK:
        leaf_node_object = LeafNode("a", text_node.text, {"href":text_node.url}) 
        return leaf_node_object

    if text_node.text_type == TextType.IMAGE:
        leaf_node_object = LeafNode("img", "", {"src":text_node.url, "alt":text_node.text}) 
        return leaf_node_object

    else:
        raise Exception("unknown text type")



