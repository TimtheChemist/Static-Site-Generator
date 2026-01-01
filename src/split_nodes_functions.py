from textnode import TextType, TextNode
import re


def split_nodes_delimiter(old_nodes, delimiter, text_type):
    list_of_nodes = []

    for old_node in old_nodes:
        if old_node.text_type != TextType.TEXT:
            list_of_nodes.append(old_node)

        else:
            list_of_strings = old_node.text.split(delimiter)

            if len(list_of_strings) % 2 == 0:
                raise Exception("Unmatched delimiter detected!")

            string_counter = 1
            for text_string in list_of_strings:

                if text_string == "":
                    string_counter += 1
                    continue

                if string_counter % 2 != 0:
                    new_node = TextNode(text_string, TextType.TEXT)
                    list_of_nodes.append(new_node)
                    string_counter += 1

                else:
                    new_node = TextNode(text_string, text_type)
                    list_of_nodes.append(new_node)
                    string_counter += 1


    return list_of_nodes


def split_nodes_image(old_nodes):
    pass


def split_nodes_link(old_nodes):
    list_of_nodes = []

    for old_node in old_nodes:
        if old_node.text_type != TextType.TEXT:
            list_of_nodes.append(old_node)

        else:
            list_of_urls = extract_markdown_links(old_node.text)
            matched_linked_text = list_of_urls[0][0]
            matched_url = list_of_urls[0][1]


            list_of_strings = old_node.text.split(f"![{matched_linked_text}]({matched_url})", 1)


            string_counter = 1
            for text_string in list_of_strings:

                if text_string == "":
                    string_counter += 1
                    continue

                if string_counter % 2 != 0:
                    new_node = TextNode(text_string, TextType.TEXT)
                    list_of_nodes.append(new_node)
                    string_counter += 1

                else:
                    new_node = TextNode(text_string, TextType.LINK)
                    list_of_nodes.append(new_node)
                    string_counter += 1
    
    return list_of_nodes


def extract_markdown_images(text):
    matches_alt_text = re.findall(r"!\[([^\[\]]*)\]\(([^\(\)]*)\)", text)
    return matches_alt_text


def extract_markdown_links(text):
    matches_url = re.findall(r"(?<!!)\[([^\[\]]*)\]\(([^\(\)]*)\)", text)
    return matches_url



