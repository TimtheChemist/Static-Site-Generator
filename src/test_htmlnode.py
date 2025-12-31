import unittest

from htmlnode import HTMLNode


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




if __name__ == "__main__":
    unittest.main()