import unittest
from generate_page import extract_title

class TestGeneratePage(unittest.TestCase):
    def test_heading(self):
        md = "# The quick brown fox jumps over the lazy dog."
        title = extract_title(md)
        self.assertEqual(title, "The quick brown fox jumps over the lazy dog.")
       