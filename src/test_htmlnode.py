import unittest

from htmlnode import HTMLNode, LeafNode, ParentNode


class TestHTMLNode(unittest.TestCase):
    def test_tag_p(self):
        node = HTMLNode(tag="p", value=None, children=None, props=None)
        self.assertEqual(node.tag, "p")

    def test_implicit_none(self):
        node = HTMLNode()
        self.assertIsNone(node.value)

    def test_explicit_none(self):
        node = HTMLNode(tag=None, value=None, children=None, props=None)
        self.assertIsNone(node.children)

    def test_value_unequal(self):
        node = HTMLNode(tag="p", value="This is paragraph text.")
        node_ref = HTMLNode(tag='p', value='This is another paragraph text.', children=None, props=None)
        self.assertNotEqual(node.value, node_ref.value)

    def test_props_to_html(self):
        node = HTMLNode(tag="p", value="This is paragraph text.", props={
        "href": "https://www.google.com",
        "target": "_blank",
        })
        node_ref =' href="https://www.google.com" target="_blank"'
        self.assertEqual(node.props_to_html(), node_ref)

    def test_props_to_html_blank(self):
        node = HTMLNode(tag="p", value="This is paragraph text.", props={})
        node_ref = ""
        self.assertEqual(node.props_to_html(), node_ref)

    def test_leaf_to_html_p(self):
        node = LeafNode("p", "Hello, world!")
        self.assertEqual(node.to_html(), "<p>Hello, world!</p>")

    def test_leaf_to_html_value_none(self):
        node = LeafNode("p", None)
        with self.assertRaises(ValueError):
            node.to_html()

    def test_leaf_to_html_href(self):
        node = LeafNode("a", "Click me!", {"href": "https://www.google.com"})
        self.assertEqual(node.to_html(), '<a href="https://www.google.com">Click me!</a>')

    def test_to_html_with_no_children(self):
        parent_node = ParentNode("div", None)
        with self.assertRaises(ValueError):
            parent_node.to_html()

    def test_to_html_with_children(self):
        child_node = LeafNode("span", "child")
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(parent_node.to_html(), "<div><span>child</span></div>")

    def test_to_html_with_children_no_value(self):
        child_node = LeafNode("span", None)
        parent_node = ParentNode("div", [child_node])
        with self.assertRaises(ValueError):
            parent_node.to_html()

    def test_to_html_with_grandchildren(self):
        grandchild_node = LeafNode("b", "grandchild")
        child_node = ParentNode("span", [grandchild_node])
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(
            parent_node.to_html(),
            "<div><span><b>grandchild</b></span></div>",
        )


if __name__ == "__main__":
    unittest.main()