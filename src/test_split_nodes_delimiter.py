import unittest
from split_nodes_delimiter import split_nodes_delimiter
from textnode import TextNode, TextType


class TestSplitNodesDelimiter(unittest.TestCase):
    def test_TEXT_CODE(self):
        node = TextNode("This is text with a `code block` word", TextType.TEXT)
        new_nodes = split_nodes_delimiter([node], "`", TextType.CODE)
        converted_new_nodes_ref = [
            TextNode("This is text with a ", TextType.TEXT),
            TextNode("code block", TextType.CODE),
            TextNode(" word", TextType.TEXT),
        ]
        self.assertEqual(new_nodes, converted_new_nodes_ref)


    def test_TEXT_ITALIC(self):
        node = TextNode("This is text with a _italicised block_ word", TextType.TEXT)
        new_nodes = split_nodes_delimiter([node], "_", TextType.ITALIC)
        converted_new_nodes_ref = [
            TextNode("This is text with a ", TextType.TEXT),
            TextNode("italicised block", TextType.ITALIC),
            TextNode(" word", TextType.TEXT),
        ]
        self.assertEqual(new_nodes, converted_new_nodes_ref)
        

    def test_TEXT_BOLD(self):
        node = TextNode("This is text with a **bold block** word", TextType.TEXT)
        new_nodes = split_nodes_delimiter([node], "**", TextType.BOLD)
        converted_new_nodes_ref = [
            TextNode("This is text with a ", TextType.TEXT),
            TextNode("bold block", TextType.BOLD),
            TextNode(" word", TextType.TEXT),
        ]
        self.assertEqual(new_nodes, converted_new_nodes_ref)


    def test_multiple_BOLD(self):
        node_1 = TextNode("This is text with a **bold block** word", TextType.TEXT)
        node_2 = TextNode("This is text with a second **bold block** word", TextType.TEXT)
        new_nodes = split_nodes_delimiter([node_1, node_2], "**", TextType.BOLD)
        converted_new_nodes_ref = [
            TextNode("This is text with a ", TextType.TEXT),
            TextNode("bold block", TextType.BOLD),
            TextNode(" word", TextType.TEXT),
            TextNode("This is text with a second ", TextType.TEXT),
            TextNode("bold block", TextType.BOLD),
            TextNode(" word", TextType.TEXT),
        ]
        self.assertEqual(new_nodes, converted_new_nodes_ref)


    def test_TEXT_BOLD_front(self):
        node = TextNode("**This** is text with a **bold block** word", TextType.TEXT)
        new_nodes = split_nodes_delimiter([node], "**", TextType.BOLD)
        converted_new_nodes_ref = [
            TextNode("This", TextType.BOLD),
            TextNode(" is text with a ", TextType.TEXT),
            TextNode("bold block", TextType.BOLD),
            TextNode(" word", TextType.TEXT),
        ]
        self.assertEqual(new_nodes, converted_new_nodes_ref)


    def test_TEXT_BOLD_end(self):
        node = TextNode("This is text with a bold block **word**", TextType.TEXT)
        new_nodes = split_nodes_delimiter([node], "**", TextType.BOLD)
        converted_new_nodes_ref = [
            TextNode("This is text with a bold block ", TextType.TEXT),
            TextNode("word", TextType.BOLD),
        ]
        self.assertEqual(new_nodes, converted_new_nodes_ref)