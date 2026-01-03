from enum import Enum

class BlockType(Enum):
    PARAGRAPH = "paragraph"
    HEADING = "heading"
    CODE = "code"
    QUOTE = "quote"
    UNORDERED_LIST = "unordered_list"
    ORDERED_LIST = "ordered_list"


def block_to_block_type(block):

    if block.startswith("```") and block.endswith("```"):
        return BlockType.CODE

    elif block.startswith("#"):
        count = 0
        for ch in block:
            if ch == "#":
                count += 1
            else:
                break
        if len(block) > count:
            if count < 7 and block[count] == " ":
                return BlockType.HEADING

    elif block.startswith(">"):
        lines = block.split("\n")
        tracker = True
        for line in lines:
            if line.startswith(">") == False:
                tracker = False
                break

        if tracker == True:
            return BlockType.QUOTE
        else:
            return BlockType.PARAGRAPH

    elif block.startswith("- "):
        lines = block.split("\n")
        tracker = True
        for line in lines:
            if line.startswith("- ") == False:
                tracker = False
                break

        if tracker == True:
            return BlockType.UNORDERED_LIST
        else:
            return BlockType.PARAGRAPH

    elif block.startswith("1. "):
        lines = block.split("\n")
        tracker = True
        for i in range(len(lines)):
            if lines[i].startswith(f"{i + 1}. ") == False:
                tracker = False
                break

        if tracker == True:    
            return BlockType.ORDERED_LIST
        else:
            return BlockType.PARAGRAPH

    else:
        return BlockType.PARAGRAPH


def markdown_to_blocks(markdown):
    list_of_blocks = []
    stripped_markdown = markdown.strip()
    unformatted_list = stripped_markdown.split("\n\n")

    for string in unformatted_list:
        if string == "":
            continue

        list_of_lines = string.split("\n")
        clean_lines = []

        for line in list_of_lines:
            stripped_string = line.strip()
            clean_lines.append(stripped_string)
           
        block = "\n".join(clean_lines)
        list_of_blocks.append(block)

    return list_of_blocks