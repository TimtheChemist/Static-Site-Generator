


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