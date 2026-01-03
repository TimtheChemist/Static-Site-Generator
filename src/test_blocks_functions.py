import unittest
from blocks_functions import markdown_to_blocks, block_to_block_type, BlockType


class TestBlocksFunctions(unittest.TestCase):

    def test_markdown_to_blocks(self):
        md = """
        This is **bolded** paragraph

        This is another paragraph with _italic_ text and `code` here
        This is the same paragraph on a new line

        - This is a list
        - with items
        """
        blocks = markdown_to_blocks(md)
        self.assertEqual(
            blocks,
            [
                "This is **bolded** paragraph",
                "This is another paragraph with _italic_ text and `code` here\nThis is the same paragraph on a new line",
                "- This is a list\n- with items",
            ],
        )

    def test_block_to_block_type_Heading_one(self):
        block = "# Heading one"
        block_type = block_to_block_type(block)
        self.assertEqual(block_type, BlockType.HEADING)


    def test_block_to_block_type_Heading_six(self):
        block = "###### Heading six"
        block_type = block_to_block_type(block)
        self.assertEqual(block_type, BlockType.HEADING)


    def test_block_to_block_type_Code(self):
        block = "```Code Text Here```"
        block_type = block_to_block_type(block)
        self.assertEqual(block_type, BlockType.CODE)

    def test_block_to_block_type_ordered_list(self):
        block = "1. one\n2. two\n3. three"
        block_type = block_to_block_type(block)
        self.assertEqual(block_type, BlockType.ORDERED_LIST)

    def test_block_to_block_type_ordered_list_wrong_number(self):
        block = "1. one\n3. three\n2. two"
        block_type = block_to_block_type(block)
        self.assertEqual(block_type, BlockType.PARAGRAPH)

    def test_block_to_block_type_unordered_list(self):
        block = "- one\n- two\n- three"
        block_type = block_to_block_type(block)
        self.assertEqual(block_type, BlockType.UNORDERED_LIST)

    def test_block_to_block_type_unordered_list_interrupted(self):
        block = "- one\n-two\n- three"
        block_type = block_to_block_type(block)
        self.assertEqual(block_type, BlockType.PARAGRAPH)